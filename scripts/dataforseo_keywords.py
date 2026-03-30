#!/usr/bin/env python3
"""
DataForSEO Keyword Research Script
Fetches keyword suggestions using the keywords_for_keywords/live endpoint.
Uses only Python standard library — no pip installs required.

Usage:
    python dataforseo_keywords.py \
        --login "your@email.com" \
        --password "your_api_password" \
        --keywords "aluminium profiles,aluminium extrusion" \
        --location-code 2356 \
        --output keywords_result.json

Location codes (common):
    India=2356, USA=2840, UK=2826, Australia=2036,
    Canada=2124, UAE=2784, Singapore=2702
"""

import argparse
import base64
import csv
import json
import sys
import urllib.error
import urllib.request

ENDPOINT = "https://api.dataforseo.com/v3/keywords_data/google_ads/keywords_for_keywords/live"


def build_auth_header(login: str, password: str) -> str:
    """Build HTTP Basic auth header from credentials."""
    credentials = f"{login}:{password}"
    encoded = base64.b64encode(credentials.encode()).decode()
    return f"Basic {encoded}"


def fetch_keywords(login: str, password: str, keywords: list[str],
                   location_code: int, language_code: str = "en",
                   limit: int = 100) -> dict:
    """Call DataForSEO keywords_for_keywords/live endpoint."""
    payload = json.dumps([{
        "keywords": keywords,
        "location_code": location_code,
        "language_code": language_code,
        "sort_by": "search_volume",
        "limit": limit,
    }]).encode("utf-8")

    request = urllib.request.Request(
        ENDPOINT,
        data=payload,
        headers={
            "Authorization": build_auth_header(login, password),
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        if e.code == 401:
            print("ERROR: Authentication failed. Check your DataForSEO login and password.", file=sys.stderr)
        elif e.code == 402:
            print("ERROR: Insufficient balance. Top up your DataForSEO account.", file=sys.stderr)
        elif e.code == 429:
            print("ERROR: Rate limit exceeded. Wait a moment and try again.", file=sys.stderr)
        else:
            print(f"ERROR: HTTP {e.code} — {body[:500]}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Network error — {e.reason}", file=sys.stderr)
        sys.exit(1)


def extract_keywords(response: dict) -> list[dict]:
    """Extract keyword records from API response, handling empty/error cases."""
    tasks = response.get("tasks", [])
    if not tasks:
        print("WARNING: No tasks in API response.", file=sys.stderr)
        return []

    task = tasks[0]
    status_code = task.get("status_code", 0)
    status_message = task.get("status_message", "")

    if status_code != 20000:
        print(f"ERROR: Task failed — {status_code}: {status_message}", file=sys.stderr)
        sys.exit(1)

    results = task.get("result", [])
    if not results:
        print("WARNING: API returned zero results. Try different seed keywords.", file=sys.stderr)
        return []

    keywords = []
    for result in results:
        for item in result.get("result", []) or []:
            keywords.append({
                "keyword": item.get("keyword", ""),
                "search_volume": item.get("search_volume") or 0,
                "competition": item.get("competition") or 0,
                "competition_level": item.get("competition_level") or "",
                "cpc": item.get("cpc") or 0,
                "low_bid": (item.get("keyword_info", {}) or {}).get("low_top_of_page_bid") or 0,
                "high_bid": (item.get("keyword_info", {}) or {}).get("high_top_of_page_bid") or 0,
            })

    return keywords


def print_summary(keywords: list[dict], seed_keywords: list[str]) -> None:
    """Print a human-readable summary of the results."""
    print(f"\n{'=' * 60}")
    print(f"KEYWORD RESEARCH RESULTS")
    print(f"{'=' * 60}")
    print(f"Seed keywords:    {', '.join(seed_keywords)}")
    print(f"Total keywords:   {len(keywords)}")

    if not keywords:
        print("No keywords found.")
        return

    sorted_kw = sorted(keywords, key=lambda x: x["search_volume"], reverse=True)
    total_volume = sum(k["search_volume"] for k in keywords)
    print(f"Total volume:     {total_volume:,}")
    print(f"\nTop 10 by search volume:")
    print(f"{'Keyword':<45} {'Volume':>8} {'CPC':>6} {'Competition':>12}")
    print(f"{'-' * 45} {'-' * 8} {'-' * 6} {'-' * 12}")

    for kw in sorted_kw[:10]:
        name = kw["keyword"][:44]
        print(f"{name:<45} {kw['search_volume']:>8,} {kw['cpc']:>6.2f} {kw['competition_level']:>12}")

    print(f"{'=' * 60}\n")


def save_csv(keywords: list[dict], output_path: str) -> None:
    """Save keywords as CSV alongside the JSON output."""
    csv_path = output_path.rsplit(".", 1)[0] + ".csv"
    if not keywords:
        return

    fieldnames = ["keyword", "search_volume", "competition", "competition_level", "cpc", "low_bid", "high_bid"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for kw in sorted(keywords, key=lambda x: x["search_volume"], reverse=True):
            writer.writerow(kw)

    print(f"CSV saved:  {csv_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Fetch keyword suggestions from DataForSEO API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Location codes: India=2356, USA=2840, UK=2826, AU=2036, CA=2124, UAE=2784, SG=2702",
    )
    parser.add_argument("--login", required=True, help="DataForSEO account email")
    parser.add_argument("--password", required=True, help="DataForSEO API password")
    parser.add_argument("--keywords", required=True, help="Comma-separated seed keywords")
    parser.add_argument("--location-code", type=int, default=2356, help="Location code (default: 2356 India)")
    parser.add_argument("--language-code", default="en", help="Language code (default: en)")
    parser.add_argument("--limit", type=int, default=100, help="Max keywords per seed (default: 100)")
    parser.add_argument("--output", default="keywords_result.json", help="Output JSON file path")

    args = parser.parse_args()

    seed_keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    if not seed_keywords:
        print("ERROR: Provide at least one seed keyword.", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching keywords for: {', '.join(seed_keywords)}")
    print(f"Location code: {args.location_code} | Language: {args.language_code} | Limit: {args.limit}")

    response = fetch_keywords(
        login=args.login,
        password=args.password,
        keywords=seed_keywords,
        location_code=args.location_code,
        language_code=args.language_code,
        limit=args.limit,
    )

    # Save raw JSON
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2, ensure_ascii=False)
    print(f"JSON saved: {args.output}")

    # Extract, summarise, and save CSV
    keywords = extract_keywords(response)
    print_summary(keywords, seed_keywords)
    save_csv(keywords, args.output)


if __name__ == "__main__":
    main()
