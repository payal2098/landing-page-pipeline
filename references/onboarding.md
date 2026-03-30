# Landing Page Pipeline — Onboarding Guide

This file is the single authority for the onboarding flow, config schema, and field validation. SKILL.md points here — no onboarding logic is repeated elsewhere.

---

## Table of Contents

1. [Before You Start](#before-you-start)
2. [Phase 1: Company Identity](#phase-1-company-identity)
3. [Phase 2: Products and Trust Signals](#phase-2-products-and-trust-signals)
4. [Phase 3: Target Audience](#phase-3-target-audience)
5. [Phase 4: Style and Localisation](#phase-4-style-and-localisation)
6. [Phase 5: DataForSEO and Technical](#phase-5-dataforseo-and-technical)
7. [Config Schema Reference](#config-schema-reference)
8. [Validation Rules](#validation-rules)

---

## Before You Start

The onboarding creates a `landing-page-config.json` file in the project's working directory. This file is the single source of truth for all company-specific details used throughout the pipeline.

If a config file already exists, load it and skip onboarding. If fields are missing (e.g., from an older version), prompt only for the missing fields.

---

## Phase 1: Company Identity

Ask the user these questions in order. Accept free-text answers.

| # | Question | Config Field | Example |
|---|----------|-------------|---------|
| 1.1 | What is the full legal name of the company? | `company.name` | "Karnataka Metal Company" |
| 1.2 | Are there any rules for how the company name must appear in content? (e.g., never abbreviate, always use full name, specific capitalisation) | `company.name_rules` | "Always write 'Karnataka Metal Company' — never 'KMC'" |
| 1.3 | What is the primary phone number for sales enquiries? | `company.phone` | "+91 80 2670 9928" |
| 1.4 | What is the primary email for sales enquiries? | `company.email` | "sales@karnatakametal.com" |
| 1.5 | What is the website URL? | `company.website` | "https://karnatakametal.com" |
| 1.6 | What is the WhatsApp number (if available)? | `company.whatsapp` | "+918026709928" or null |
| 1.7 | List all office/plant addresses (one per line). | `company.addresses[]` | [{"label": "Head Office", "address": "...", "city": "Bangalore"}] |
| 1.8 | What year was the company founded? | `company.founded` | 1974 |
| 1.9 | Approximate number of employees? | `company.employees` | "250+" |
| 1.10 | One-line company description for schema markup. | `company.description` | "Integrated aluminium extrusion and glass processing company" |

---

## Phase 2: Products and Trust Signals

| # | Question | Config Field | Example |
|---|----------|-------------|---------|
| 2.1 | Where are the product/service knowledge files located? (directory path or list of files) | `products.knowledge_paths[]` | ["/path/to/products/"] |
| 2.2 | List the company's certifications (one per line). | `products.certifications[]` | ["ISO 9001:2015", "BIS/ISI"] |
| 2.3 | What are the company's top 3-6 unique selling points? | `products.usps[]` | ["Only integrated glass + aluminium company in South India"] |
| 2.4 | List key projects or clients that can be referenced publicly. | `social_proof.projects[]` | [{"name": "AAI Shimoga Airport", "type": "Commercial"}] |
| 2.5 | Are there any stat-line numbers to display? (e.g., "250+ clients", "50+ years") | `social_proof.stats[]` | [{"number": "250+", "label": "Clients Served"}] |
| 2.6 | Are client logos available for display? If yes, which ones? | `social_proof.client_logos[]` | ["Prestige", "Sobha", "Embassy"] |
| 2.7 | Are client testimonials available? | `social_proof.testimonials_available` | false |
| 2.8 | List any partner/supplier brands to mention. | `products.partners[]` | [{"name": "Aludecor", "relationship": "Authorised distributor"}] |

---

## Phase 3: Target Audience

| # | Question | Config Field | Example |
|---|----------|-------------|---------|
| 3.1 | Is the business B2B, B2C, or both? | `audience.type` | "both" |
| 3.2 | Describe the primary audience segments (one per line: segment name + who they are). | `audience.segments[]` | [{"name": "Fabricators", "description": "Small aluminium fabrication shops"}] |
| 3.3 | What is the primary geographic market? | `audience.geography` | "South India (Karnataka, Kerala, Tamil Nadu, Telangana, AP)" |
| 3.4 | What industries do you serve? | `audience.industries[]` | ["Construction", "Solar Energy", "Automotive"] |
| 3.5 | What is the typical purchase decision process? (quick quote vs long sales cycle) | `audience.decision_process` | "Phone/WhatsApp enquiry, quote within 24 hours, order on approval" |

---

## Phase 4: Style and Localisation

| # | Question | Config Field | Default | Example |
|---|----------|-------------|---------|---------|
| 4.1 | Which English variant? (British, American, Australian) | `style.english_variant` | "british" | "british" |
| 4.2 | What is the content tone? (technical, conversational, formal, friendly) | `style.tone` | "technical" | "technical" |
| 4.3 | Are em dashes allowed in content? | `style.allow_em_dashes` | false | false |
| 4.4 | Are emojis allowed in content? | `style.allow_emojis` | false | false |
| 4.5 | List any words or phrases that must NEVER appear in content. | `style.forbidden_terms[]` | — | ["KMC", "Saint-Gobain Propel"] |
| 4.6 | What standards body governs your industry? (e.g., BIS/IS, ASTM, BS EN) | `style.standards_body` | — | "BIS/IS" |
| 4.7 | What currency should be used for pricing? | `style.currency` | "INR" | "INR" |
| 4.8 | What currency symbol or prefix? | `style.currency_symbol` | "Rs" | "Rs" |
| 4.9 | What measurement units? (metric, imperial, both) | `style.units` | "metric" | "metric" |
| 4.10 | Any claims that must NOT be made without verification? | `style.restricted_claims[]` | — | ["Only integrated glass + aluminium company"] |

---

## Phase 5: DataForSEO and Technical

| # | Question | Config Field | Example |
|---|----------|-------------|---------|
| 5.1 | DataForSEO login (email) | `dataforseo.login` | "user@example.com" |
| 5.2 | DataForSEO password (API key) | `dataforseo.password` | "abc123..." |
| 5.3 | What country are you targeting for SEO? | `dataforseo.location_code` | 2356 |
| 5.4 | What language code? | `dataforseo.language_code` | "en" |
| 5.5 | List existing pages/blogs the pipeline can link to internally. | `technical.internal_links[]` | [{"url": "/blog/acp-sheets-guide", "topic": "ACP buying guide"}] |
| 5.6 | Is the website currently using HTTPS? | `technical.https_active` | true |
| 5.7 | What CMS/platform is the website built on? | `technical.cms` | "Custom HTML" |

### Location Code Lookup Table

Present this table when asking question 5.3. If the user's country is not listed, they can look up their code at [DataForSEO locations API](https://api.dataforseo.com/v3/keywords_data/google_ads/locations).

| Country | Code |
|---------|------|
| India | 2356 |
| United States | 2840 |
| United Kingdom | 2826 |
| Australia | 2036 |
| Canada | 2124 |
| UAE | 2784 |
| Singapore | 2702 |
| Germany | 2276 |
| France | 2250 |
| South Africa | 2710 |

---

## Config Schema Reference

The complete `landing-page-config.json` structure. All fields marked `(required)` must be populated before the pipeline can run. Fields marked `(optional)` can be null or omitted.

```json
{
  "company": {
    "name": "string (required)",
    "name_rules": "string (optional) — free text rules for name usage",
    "phone": "string (required)",
    "email": "string (required)",
    "website": "string (required)",
    "whatsapp": "string or null (optional)",
    "addresses": [
      {
        "label": "string — e.g. 'Head Office', 'Plant 1'",
        "address": "string — full street address",
        "city": "string",
        "state": "string (optional)",
        "country": "string",
        "postal_code": "string (optional)"
      }
    ],
    "founded": "integer or null (optional)",
    "employees": "string or null (optional)",
    "description": "string (required) — one-line for schema markup"
  },
  "products": {
    "knowledge_paths": ["string (required) — at least one path"],
    "certifications": ["string (optional)"],
    "usps": ["string (required) — at least 3"],
    "partners": [
      {
        "name": "string",
        "relationship": "string — e.g. 'Authorised distributor'"
      }
    ]
  },
  "social_proof": {
    "projects": [
      {
        "name": "string",
        "type": "string — e.g. 'Commercial', 'Residential', 'Airport'"
      }
    ],
    "stats": [
      {
        "number": "string — e.g. '250+'",
        "label": "string — e.g. 'Clients Served'"
      }
    ],
    "client_logos": ["string (optional)"],
    "testimonials_available": "boolean (default: false)"
  },
  "audience": {
    "type": "string (required) — 'b2b', 'b2c', or 'both'",
    "segments": [
      {
        "name": "string",
        "description": "string"
      }
    ],
    "geography": "string (required)",
    "industries": ["string (optional)"],
    "decision_process": "string (optional)"
  },
  "style": {
    "english_variant": "string (required) — 'british', 'american', or 'australian'",
    "tone": "string (required) — 'technical', 'conversational', 'formal', 'friendly'",
    "allow_em_dashes": "boolean (default: false)",
    "allow_emojis": "boolean (default: false)",
    "forbidden_terms": ["string (optional)"],
    "standards_body": "string or null (optional)",
    "currency": "string (default: 'USD')",
    "currency_symbol": "string (default: '$')",
    "units": "string (default: 'metric') — 'metric', 'imperial', or 'both'",
    "restricted_claims": ["string (optional)"]
  },
  "dataforseo": {
    "login": "string (required)",
    "password": "string (required)",
    "location_code": "integer (required)",
    "language_code": "string (default: 'en')"
  },
  "technical": {
    "internal_links": [
      {
        "url": "string",
        "topic": "string"
      }
    ],
    "https_active": "boolean (default: true)",
    "cms": "string or null (optional)"
  }
}
```

---

## Validation Rules

Run these checks after onboarding completes. If any required field is missing, prompt the user for it before saving.

### Required Fields (pipeline will not run without these)

| Field | Validation |
|-------|-----------|
| `company.name` | Non-empty string |
| `company.phone` | Non-empty string |
| `company.email` | Contains `@` |
| `company.website` | Starts with `http://` or `https://` |
| `company.description` | Non-empty string, max 200 characters |
| `products.knowledge_paths` | At least one valid file or directory path |
| `products.usps` | At least 3 items |
| `audience.type` | One of: `b2b`, `b2c`, `both` |
| `audience.geography` | Non-empty string |
| `style.english_variant` | One of: `british`, `american`, `australian` |
| `style.tone` | One of: `technical`, `conversational`, `formal`, `friendly` |
| `dataforseo.login` | Non-empty string containing `@` |
| `dataforseo.password` | Non-empty string |
| `dataforseo.location_code` | Positive integer |

### Format Checks

| Field | Rule |
|-------|------|
| `company.whatsapp` | If provided, must be digits only (no spaces, dashes, or plus sign after cleaning) |
| `company.founded` | If provided, must be integer between 1800 and current year |
| `dataforseo.location_code` | Must be a known code from the lookup table, or user confirms custom code |
| `style.currency` | 3-letter ISO 4217 code (INR, USD, GBP, EUR, AUD, AED, SGD, etc.) |
| `technical.internal_links[].url` | Must start with `/` (relative) or `http` (absolute) |

### Default Values

If the user skips an optional field, apply these defaults:

| Field | Default |
|-------|---------|
| `style.allow_em_dashes` | `false` |
| `style.allow_emojis` | `false` |
| `style.currency` | `"USD"` |
| `style.currency_symbol` | `"$"` |
| `style.units` | `"metric"` |
| `dataforseo.language_code` | `"en"` |
| `technical.https_active` | `true` |
| `social_proof.testimonials_available` | `false` |

---

## Onboarding Flow Summary

1. Greet the user and explain what the pipeline does (one sentence).
2. Walk through Phases 1-5 in order. Use `AskUserQuestion` for each phase.
3. After each phase, confirm the answers before moving on.
4. After Phase 5, validate all required fields.
5. Save `landing-page-config.json` to the project working directory.
6. Print a summary of the config and confirm the pipeline is ready.

If the user wants to update an existing config, load the file, show current values, and let them edit specific fields without re-running the full onboarding.
