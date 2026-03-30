---
name: landing-page-pipeline
description: End-to-end landing page creation pipeline for any business. Runs keyword research, competitor analysis, content brief, developer-ready landing page, SEO optimisation, and automated QA in a single invocation. Use this skill whenever the user asks to create a landing page, build a product page, make a service page, run the LP pipeline, generate a landing page for a product or service, or says anything about landing page content creation. Works for manufacturing, SaaS, e-commerce, and service businesses in any country.
---

# Landing Page Pipeline

Create SEO-optimised, developer-ready landing pages from scratch. This pipeline takes a product or service topic and produces a complete landing page file with keyword research, structured content, schema markup, and QA — ready for a frontend developer to build.

---

## Prerequisites

Before running this pipeline, the following must be available:

1. **DataForSEO API credentials** — login (email) and password. Get them at [app.dataforseo.com](https://app.dataforseo.com).
2. **Product/service knowledge files** — markdown, text, or document files describing the product or service in detail (specs, features, certifications, etc.).
3. **Python 3.6+** — for running the keyword research script (uses only standard library).

---

## Onboarding

Check if `landing-page-config.json` exists in the project working directory.

- **If it exists:** Load it and proceed to the pipeline. If any required fields are missing, prompt for those fields only.
- **If it does not exist:** Read `references/onboarding.md` and follow the 5-phase guided onboarding flow. Save the completed config as `landing-page-config.json` in the project working directory.

Do not repeat onboarding questions or config field definitions here — `references/onboarding.md` is the single authority.

---

## The 11-Step Pipeline

### Overview

| Step | Name | Type | Reference |
|------|------|------|-----------|
| 1 | Product Knowledge Audit | Research | Inline |
| 2 | Keyword Research | Research + API | Inline + `scripts/dataforseo_keywords.py` |
| 3 | Competitor Page Analysis | Research | Inline |
| 4 | Existing Content Review | Research | Inline |
| 5 | Content Brief | Synthesis | Inline |
| **CHECKPOINT 1** | *Keyword research and brief approved by user* | | |
| 6 | Page Architecture | Writing | `references/lp-template.md` |
| 7 | Copywriting | Writing | Config (style rules) + template (structure) |
| 8 | Image Planning | Writing | `references/lp-template.md` (image spec format) |
| **CHECKPOINT 2** | *Draft reviewed by user* | | |
| 9 | SEO Optimisation | QA | `references/seo-and-qa.md` (SEO checklist) |
| 10 | Quality Assurance | QA | `references/seo-and-qa.md` (30-point QA checklist) |
| 11 | Final Output | Deliverable | Inline |
| **CHECKPOINT 3** | *Final output approved by user* | | |

---

### Step 1: Product Knowledge Audit

Read all files in `config.products.knowledge_paths[]`. Build a facts sheet:

- Product/service name and category
- All specifications (dimensions, materials, capacity, performance metrics)
- Certifications and standards compliance
- Manufacturing process or service delivery method
- Unique features or differentiators
- Existing claims that can be verified

Mark each fact as **verified** (found in knowledge files) or **unverified** (needs confirmation). Unverified facts get flagged in Step 10.

### Step 2: Keyword Research

1. Determine 2-4 seed keywords based on the product/service topic and target audience.
2. Run the DataForSEO keyword research script:

```bash
python scripts/dataforseo_keywords.py \
  --login "{{config.dataforseo.login}}" \
  --password "{{config.dataforseo.password}}" \
  --keywords "seed keyword 1,seed keyword 2" \
  --location-code {{config.dataforseo.location_code}} \
  --output data/lp_keywords_[topic].json
```

3. From the results, identify:
   - **Primary keyword**: Highest volume keyword that matches the page's intent
   - **Secondary keywords**: 5-10 related keywords with volume > 100/mo
   - **Long-tail keywords**: FAQ candidates and niche queries
   - **Price-intent keywords**: Any keywords containing "price", "cost", "rate" — note their volume (determines whether a pricing table is needed in the body)
   - **Local-intent keywords**: Keywords containing "near me", city names, or regional terms

4. Build a keyword table:

| Keyword | Volume | Intent | Target Section | Include? |
|---------|--------|--------|---------------|----------|
| [keyword] | [vol] | [info/comm/trans] | [section #] | Yes/No + reason |

### Step 3: Competitor Page Analysis

1. Web search for the primary keyword. Identify the top 3 ranking pages.
2. For each competitor page, note:
   - Word count (approximate)
   - Sections/structure
   - Unique content they have that the knowledge base supports
   - Gaps (topics they miss that the company can cover)
   - Schema markup (if visible in search results — rich snippets, FAQ, etc.)

3. Summarise as a competitor comparison table.

### Step 4: Existing Content Review

1. Check if the company has existing content on this topic (blogs, current website pages).
2. Search `config.technical.internal_links[]` for related pages.
3. Note content that should be linked to (not duplicated).
4. Flag any content overlap risks.

### Step 5: Content Brief

Compile Steps 1-4 into a content brief:

- **Page goal**: One sentence describing what action the page should drive
- **Target audience**: Primary, secondary, tertiary (from config + topic analysis)
- **Search intent split**: % informational / commercial / transactional
- **Primary keyword**: keyword (volume/mo)
- **Secondary keywords**: table with volumes
- **Keyword table**: Full table from Step 2
- **Recommended section structure**: Which of the 11 template sections to include, with suggested H2 headings and target keywords per section
- **Verified facts sheet**: From Step 1
- **Competitor insights**: Key findings from Step 3
- **Internal linking opportunities**: From Step 4
- **Proof/trust elements**: Projects, stats, certifications relevant to this topic
- **Missing information**: Anything needed from the client, flagged with `[INFORMATION REQUIRED]`

---

### CHECKPOINT 1: User Approval

Present the keyword research summary and content brief to the user. Ask:

> "Here is the keyword research and content brief for [topic]. The primary keyword is '[keyword]' with [volume]/mo. The page will target [audience] with [intent] intent. Review the brief — should I proceed to writing, or would you like to adjust the keyword targets or section structure?"

Wait for user approval before proceeding.

---

### Step 6: Page Architecture

Read `references/lp-template.md` for the full 11-section template.

Decide which sections to include based on the content brief:
- Sections 1, 2, 4, 5, 7, 8, 9, 10, 11 are mandatory for all pages.
- Section 3 (Definition) is optional — include if the product/service needs explaining.
- Section 6 (Variants/Finishes/Plans) is optional — include if the product has meaningful variants.

Map each section to a specific H2 heading that includes target keywords from the brief.

### Step 7: Copywriting

Write the content for each section following:
- **Structure**: From `references/lp-template.md` (layout types, required elements, content guidelines)
- **Style**: From config (`config.style.*` — English variant, tone, em dash rule, emoji rule, forbidden terms)
- **Facts**: From the verified facts sheet (Step 1)
- **Keywords**: From the keyword table (Step 2)

Style rules applied from config:
- English variant: Use spellings matching `config.style.english_variant`
- Tone: Match `config.style.tone`
- Em dashes: Allowed only if `config.style.allow_em_dashes` is true
- Emojis: Allowed only if `config.style.allow_emojis` is true
- Forbidden terms: None of `config.style.forbidden_terms[]` may appear
- Company name: Follow `config.company.name_rules`
- First person ("we", "our"): Only in Sections 9 (Why Choose Us) and 10 (Get in Touch)
- Standards: Reference `config.style.standards_body` where applicable
- Currency: Use `config.style.currency_symbol` + `config.style.currency`
- Units: Use `config.style.units`

Target word count: 1,400-2,000 words.

### Step 8: Image Planning

For each section with visuals, write an image spec following the format in `references/lp-template.md`:

```
**Image:** [TYPE] | [DESCRIPTION] | Alt: "[alt text]" | [WxH] | [position]
```

Suggest 4-6 images per page. Alt text must be descriptive and include the primary keyword where natural.

---

### CHECKPOINT 2: User Review

Present the complete draft to the user. Ask:

> "Here is the complete landing page draft for [topic]. It includes [N] sections, [N] images specs, and targets [primary keyword] ([volume]/mo). Review the content — should I proceed to SEO optimisation and QA, or would you like to revise any sections?"

Wait for user approval before proceeding.

---

### Step 9: SEO Optimisation

Read the SEO On-Page Checklist in `references/seo-and-qa.md` (11 items). Run each check against the draft. Insert inline flags (format defined in `references/seo-and-qa.md`) for any failures.

Then generate schema markup using the templates in `references/seo-and-qa.md`, selecting the appropriate schemas based on the business type (see Schema Selection Guide in that file).

### Step 10: Quality Assurance

Read the 30-Point QA Checklist in `references/seo-and-qa.md`. Run every check. Insert inline flags for any failures.

Apply the 13 Error Correction Rules (below) as the final QA pass.

If any flags remain after the QA pass, resolve them before proceeding. If resolution requires information from the user, leave the flag in place and note it in the final output summary.

### Step 11: Final Output

The deliverable is a single markdown file containing:

1. **Meta block**: Title, description, URL slug, primary keyword, word count
2. **Sections 1-11**: Developer-ready content with layout types, image specs, and content per section
3. **Schema Markup**: JSON-LD code blocks ready to embed in the page head
4. **Internal Linking Map**: Table of all internal links used
5. **Developer Notes**: Responsive behaviour, image formats, CWV targets, heading hierarchy
6. **Unresolved Flags Summary** (if any): List of `[INFORMATION REQUIRED]` or `[TESTIMONIAL REQUIRED]` items still pending

Save the file as `LP-[Topic-Slug].md` in the project working directory.

---

### CHECKPOINT 3: Final Approval

Present a summary to the user:

> "The landing page for [topic] is complete. Summary:
> - Primary keyword: [keyword] ([volume]/mo)
> - Sections: [N] included, [N] optional sections omitted
> - Word count: [N] words
> - Schema: [list of schemas included]
> - Internal links: [N]
> - Unresolved flags: [N] (list them)
>
> The file has been saved as `LP-[Topic-Slug].md`. Would you like to revise anything, or is this approved for developer handoff?"

---

## 13 Error Correction Rules

These rules are the single canonical list — learned from real production errors. Apply them during Step 10 QA. They are not repeated in any reference file.

### Rule 1: Developer-Ready Format, Not Blog Style
Every section must include: section number + name, layout type, image spec (if visual), and content. Never write a landing page as a flowing blog article. A frontend team must be able to build directly from this file.

### Rule 2: Compact Product Definition
Section 3 (Product/Service Definition) must be 2-3 lines maximum. Detailed explanations belong in a linked blog post or resource. Landing page visitors have already searched for the product — they know what it is.

### Rule 3: Social Proof Is Mandatory
Every landing page must include a social proof section (Section 8) with verified project/client references from `config.social_proof.projects[]`, a stat line from `config.social_proof.stats[]`, and a testimonial placeholder if testimonials are not yet available.

### Rule 4: Pricing Must Be Visible When Search Volume Justifies It
If keyword research shows price-intent keywords with volume above 1,000/mo, include a pricing table in the body (Section 5 or a dedicated section). Always mark prices as approximate with a date stamp and a link to the contact page for exact quotes.

### Rule 5: Include Processing/Installation Methods When Applicable
For products that require installation, assembly, or processing, include a compact methods comparison table in the Specifications section. This is core product information, not a FAQ afterthought.

### Rule 6: Company USPs Lead, Partner Credentials Follow
In Why Choose Us (Section 9), always lead with the company's own USP cards. Partner or manufacturer credentials go in a compact supporting strip below. The first USP should be the strongest conversion reason, not company history.

### Rule 7: Cover All High-Volume Keywords
After writing the draft, run a keyword coverage check against all keywords with volume >= 500/mo from the keyword research. For each missing keyword: (a) add it naturally to an existing section, (b) exclude competitor brand names, (c) note American/British spelling variants but do not force them.

### Rule 8: FAQ Answers Must Be Unique
Each FAQ answer must provide information not already present in the body content. Cross-check every FAQ answer against the body. If the answer repeats information already visible on the page, replace the question with one that adds new value.

### Rule 9: Meta Description Must Match Page Intent
If the page is informational/commercial, the meta description should describe what the user will find. Do not use "Buy" or "Order" language unless the page is genuinely transactional. Mismatched intent causes high bounce rates.

### Rule 10: Verify All Claims and References
Every factual claim must trace to the product knowledge base. Every project/client name must exist in `config.social_proof.projects[]`. Never claim facilities, operations, or achievements belonging to separate legal entities. Check all internal links to ensure none are self-referencing.

### Rule 11: No Embedded Contact Forms
Product/service landing pages use CTA buttons only (Section 10). No embedded contact forms. CTA buttons link to the dedicated contact page. The contact page itself should have the form.

### Rule 12: Use Tables for Structured Data
Whenever content can be structured as a table, use a table. Paragraphs are for context and explanation. Lists of options, specifications, variants, or categories should always be tables. This applies to colours/finishes, specifications, comparisons, and pricing.

### Rule 13: FAQ After Contact, Always Last
Section order must be: Why Choose Us (9) → Get in Touch (10) → FAQ (11). FAQ is always the last content section. The conversion point (Get in Touch) must not be buried after FAQ content.

---

## Missing Information Handling

When information is needed but not available, use these placeholders. They appear in the final output so the client knows what to provide.

| Scenario | Placeholder | Action |
|----------|-------------|--------|
| Specification not in knowledge files | `[INFORMATION REQUIRED: specific detail needed]` | Do not guess values. Leave the placeholder. |
| Claim from external source, not in knowledge files | `[UNVERIFIED CLAIM: "claim text" — source: where you found it]` | Cross-check against industry standards. If plausible, include with the flag. |
| Pricing data requested but not available | `[PRICING: Contact for current rates]` + disclaimer | Include a pricing section structure with placeholder rows. |
| Client testimonial needed | `[TESTIMONIAL REQUIRED: Add client testimonial when available]` | Leave as HTML comment in the section. |
| Project photo needed | Use image spec format with description | `**Image:** Application photo | [Description of ideal photo] | Alt: "[alt text]" | 400x300 | [position]` |
| Certification status unclear | Default to what is verifiable in config | Flag unclear certifications with `[VERIFICATION REQUIRED: certification name]`. |
| Data discrepancy between sources | `[VERIFICATION REQUIRED: detail — Source A says X, Source B says Y]` | List both values. Do not pick one without verification. |

---

## Section Summary (Quick Reference)

For orientation only — full section details, layout types, and content guidelines are in `references/lp-template.md`.

| # | Section | Required? | Layout |
|---|---------|-----------|--------|
| 1 | Hero Banner | Yes | Full-width hero |
| 2 | Trust Bar | Yes | Horizontal stat bar |
| 3 | Product/Service Definition | Optional | Compact strip |
| 4 | Categories / Types | Yes | Card grid |
| 5 | Specifications | Yes | Stacked tables |
| 6 | Variants / Finishes / Plans | Optional | Table or swatch grid |
| 7 | Applications / Use Cases | Yes | Card grid + CTA |
| 8 | Projects and Social Proof | Yes | Scrollable tiles + stat line |
| 9 | Why Choose Us | Yes | USP cards + partner strip |
| 10 | Get in Touch | Yes | Dark background, centred |
| 11 | FAQ | Yes | Accordion |
