# Landing Page Pipeline

A Claude Code skill that creates SEO-optimised, developer-ready landing pages from scratch — for any business type, in any country.

Give it a product or service topic and it runs the full pipeline: keyword research, competitor analysis, content brief, 11-section landing page, schema markup, and 30-point QA — in a single invocation.

## What It Does

| Step | What Happens |
|------|-------------|
| 1. Product Knowledge Audit | Reads your product/service files and builds a verified facts sheet |
| 2. Keyword Research | Calls DataForSEO API to find primary, secondary, and long-tail keywords |
| 3. Competitor Analysis | Analyses top-ranking pages for structure, word count, and content gaps |
| 4. Existing Content Review | Checks for blogs or pages to link to (not duplicate) |
| 5. Content Brief | Compiles research into an actionable brief with keyword table and section plan |
| 6. Page Architecture | Structures the page using an 11-section template with layout types |
| 7. Copywriting | Writes conversion-focused content following your brand's style rules |
| 8. Image Planning | Creates image specs (type, alt text, dimensions) for each section |
| 9. SEO Optimisation | Runs an 11-point on-page checklist and generates schema markup |
| 10. Quality Assurance | Runs a 30-point QA checklist with inline flags for any failures |
| 11. Final Output | Delivers a developer-ready markdown file with schema, internal links, and dev notes |

Three user checkpoints pause the pipeline for approval: after the brief, after the draft, and after the final output.

## Works For

- **B2B Manufacturing** — aluminium extrusions, CNC machining, industrial components
- **B2B SaaS** — project management tools, analytics platforms, developer tools
- **B2C E-commerce** — handmade goods, fashion, home decor
- **Professional Services** — consulting, legal, accounting
- Any business with a product or service that needs a landing page

## Requirements

- [Claude Code](https://claude.ai/claude-code) CLI
- Python 3.6+ (for the keyword research script — uses only standard library)
- [DataForSEO](https://app.dataforseo.com) API credentials (login + password)

## Installation

```bash
npx skills add payal2098/landing-page-pipeline -g -y
```

Or clone manually:

```bash
git clone https://github.com/payal2098/landing-page-pipeline.git ~/.claude/skills/landing-page-pipeline
```

## Usage

Open Claude Code in any project and say:

```
Create a landing page for [your product or service]
```

Or be more specific:

```
Build a product page for our aluminium window profiles. We target architects and fabricators in South India.
```

```
Run the LP pipeline for our project management SaaS tool. We're based in London, UK.
```

### First Run — Onboarding

On the first run, the skill detects that no config exists and walks you through a 5-phase onboarding:

1. **Company identity** — name, contact details, addresses
2. **Products & trust signals** — knowledge file paths, certifications, USPs, projects
3. **Target audience** — B2B/B2C, segments, geography, industries
4. **Style & localisation** — English variant, tone, forbidden terms, currency, units
5. **DataForSEO & technical** — API credentials, location code, internal links

This creates a `landing-page-config.json` in your project. Subsequent runs skip onboarding.

### Subsequent Runs

The pipeline loads your config and jumps straight into keyword research for the topic you specify.

## Output

Each run produces a single markdown file (`LP-[Topic-Slug].md`) containing:

- Meta block (title, description, URL slug, primary keyword)
- 11 developer-ready sections with layout types, image specs, and content
- Schema markup (Product/Service, FAQPage, BreadcrumbList, Organization/LocalBusiness)
- Internal linking map
- Developer notes (responsive behaviour, image formats, Core Web Vitals targets)

Every section follows this format so a frontend team can build directly from it:

```markdown
## SECTION 4: PRODUCT CATEGORIES
**Layout:** 4-card grid, 2x2 on desktop, stacked on mobile
**Image:** Product icons | [description] | Alt: "..." | 400x300 | centred
**Mobile:** Single column, full-width cards

[Content: headings, body text, CTAs]
```

## File Structure

```
landing-page-pipeline/
├── SKILL.md                          # Main skill — pipeline orchestrator
├── scripts/
│   └── dataforseo_keywords.py        # Keyword research via DataForSEO API
├── references/
│   ├── onboarding.md                 # 5-phase onboarding + config schema
│   ├── lp-template.md               # 11-section landing page template
│   └── seo-and-qa.md                # SEO checklist, 30-point QA, schema templates
└── evals/
    └── evals.json                    # 3 test cases
```

Each file owns specific content with no overlap:

| File | Authority Over |
|------|---------------|
| `SKILL.md` | Pipeline steps, checkpoints, 13 error correction rules, missing info handling |
| `onboarding.md` | Config schema, field validation, onboarding flow |
| `lp-template.md` | Section structure, layout types, image specs, content guidelines |
| `seo-and-qa.md` | SEO checklist (11 items), QA checklist (30 items), inline flags, schema templates |
| `dataforseo_keywords.py` | API endpoint, auth, request format, error handling |

## DataForSEO Location Codes

| Country | Code |
|---------|------|
| India | 2356 |
| United States | 2840 |
| United Kingdom | 2826 |
| Australia | 2036 |
| Canada | 2124 |
| UAE | 2784 |
| Singapore | 2702 |

Full list: [DataForSEO Locations API](https://api.dataforseo.com/v3/keywords_data/google_ads/locations)

## License

MIT
