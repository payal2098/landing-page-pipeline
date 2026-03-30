# SEO Checklist, QA Checklist, and Schema Templates

This file is the single authority for SEO on-page checks, the 30-point QA checklist, inline flag format, and schema markup templates. SKILL.md points here for Steps 9 and 10 — no SEO or QA specifics are repeated elsewhere.

---

## Table of Contents

1. [SEO On-Page Checklist](#seo-on-page-checklist)
2. [30-Point QA Checklist](#30-point-qa-checklist)
3. [Inline Flag Format](#inline-flag-format)
4. [Schema Markup Templates](#schema-markup-templates)

---

## SEO On-Page Checklist

Run these 11 checks during Step 9 (SEO Optimisation). Each item is pass/fail.

| # | Check | Rule | Flag if Failed |
|---|-------|------|----------------|
| 1 | **Meta title length** | 51-55 characters, includes primary keyword | `[META TITLE TOO LONG: X chars, max 55]` or `[META TITLE TOO SHORT: X chars, min 51]` |
| 2 | **Meta description length** | 150-160 characters, includes primary keyword and a CTA phrase | `[META DESCRIPTION TOO LONG: X chars, max 160]` or `[META DESCRIPTION TOO SHORT: X chars, min 150]` |
| 3 | **URL slug** | Lowercase, hyphenated, includes primary keyword, no stop words | `[URL SLUG MISSING KEYWORD: "primary keyword"]` |
| 4 | **H1 tag** | Exactly one H1 per page, includes primary keyword, unique to this page | `[H1 MISSING PRIMARY KEYWORD: "keyword"]` or `[MULTIPLE H1 TAGS FOUND]` |
| 5 | **H2 tags** | Include secondary keywords naturally. No H3 tags anywhere. | `[H3 TAG FOUND: convert to H2]` or `[KEYWORD MISSING FROM H2S: "keyword" X/mo]` |
| 6 | **Primary keyword in first 100 words** | Primary keyword appears in the first 100 words of body content | `[PRIMARY KEYWORD NOT IN FIRST 100 WORDS]` |
| 7 | **Keyword density** | Primary keyword density 1-2% (not stuffed, not absent) | `[KEYWORD DENSITY TOO HIGH: X%]` or `[KEYWORD DENSITY TOO LOW: X%]` |
| 8 | **Internal links** | Minimum 3 internal links (to related blog, related LP, contact page). No self-referencing links. | `[INSUFFICIENT INTERNAL LINKS: X found, min 3]` or `[SELF-REFERENCING LINK: "anchor text"]` |
| 9 | **Image alt text** | All images have descriptive alt text. Primary keyword included where natural. | `[MISSING ALT TEXT: Section X image]` |
| 10 | **FAQ section** | Minimum 5 FAQ questions. Based on actual search queries from keyword research. | `[INSUFFICIENT FAQS: X found, min 5]` |
| 11 | **Schema markup** | Product/Service, FAQPage, BreadcrumbList, and Organization/LocalBusiness schemas included | `[MISSING SCHEMA: schema_type]` |

---

## 30-Point QA Checklist

Run these 30 checks during Step 10 (Quality Assurance). Every item must pass before the landing page is approved. If any item fails, return to the relevant step with specific revision instructions.

### Content and Accuracy (13 checks)

| # | Check | How to Verify |
|---|-------|---------------|
| 1 | Every factual claim traces to a verified source in the product knowledge base | Cross-reference each claim against files in `config.products.knowledge_paths[]` |
| 2 | Company name follows `config.company.name_rules` throughout | Search for forbidden abbreviations or name variants |
| 3 | No forbidden terms appear anywhere in the content | Search for all terms in `config.style.forbidden_terms[]` |
| 4 | English variant is consistent throughout | Check spelling matches `config.style.english_variant` (e.g., "colours" not "colors" for British) |
| 5 | Em dash rule followed | If `config.style.allow_em_dashes` is false, search for `—` (em dash). Use commas, semicolons, or full stops instead. |
| 6 | Emoji rule followed | If `config.style.allow_emojis` is false, no emojis appear anywhere in the content |
| 7 | No H3 tags in the document | All section headings use H2. Sub-sections use bold text or sub-labels, not H3. |
| 8 | Standards references are correct and current | Verify against `config.style.standards_body` and product knowledge base |
| 9 | All capacity/performance figures match the product knowledge base | Cross-reference numbers (capacity, dimensions, weights) against source files |
| 10 | All certification claims are verified | Check against `config.products.certifications[]` |
| 11 | No content duplicated from existing blogs or pages | Content is original. If information overlaps with a blog, link to the blog instead of repeating it. |
| 12 | Project/client names are verified | Every project name appears in `config.social_proof.projects[]` |
| 13 | No claims about entities outside the company's scope | Do not claim facilities, operations, or achievements belonging to separate legal entities, subsidiaries, or competitors |

### Structure and Format (9 checks)

| # | Check | How to Verify |
|---|-------|---------------|
| 14 | Written in developer-ready section format | Every section has: section number + name, Layout type, Image spec (if visual), Content. Not blog-style flowing text. |
| 15 | Every section has a Layout type described | Compare against layout types in `references/lp-template.md` |
| 16 | Every visual section has an Image spec inline | Image specs follow format: Type, Description, Alt text, Dimensions, Position |
| 17 | Product/service definition is compact | Section 3 (if present) is 2-3 lines max, not a full explainer |
| 18 | Social proof section meets requirements | Minimum 6 verified projects (or flagged if fewer) + stat line + testimonial placeholder |
| 19 | Why Choose Us leads with company USPs | Company's own value proposition comes first. Partner/supplier credentials in supporting strip below, not as headline. |
| 20 | No embedded contact form | Section 10 has CTA buttons only, no form fields |
| 21 | Section order is correct | Sections follow the order in `references/lp-template.md`: Hero → Trust Bar → Definition → Categories → Specs → Variants → Applications → Social Proof → Why Choose Us → Get in Touch → FAQ |
| 22 | FAQ answers add unique value | Each FAQ answer provides information not already present in the body content |

### SEO and Conversion (8 checks)

| # | Check | How to Verify |
|---|-------|---------------|
| 23 | Keyword coverage is complete | All keywords with volume >= 500/mo from the keyword research are either included in the text or excluded with a documented reason |
| 24 | Meta description intent matches page content | If page is informational/commercial, description describes what the user will find. If transactional, "Buy" or "Order" language is appropriate. |
| 25 | No self-referencing internal links | No internal link on the page points back to the same page |
| 26 | Pricing table visible if price keywords are high-volume | If keyword research shows price-intent keywords > 1,000/mo, a pricing table is visible in the body (not just in FAQ) |
| 27 | Minimum 3 CTAs with correct contact details | CTAs include correct phone, email, and/or WhatsApp from config. Minimum 3 CTA placements across the page. |
| 28 | Meta title and description within character limits | Meta title: 51-55 chars. Meta description: 150-160 chars. |
| 29 | Word count is within target range | Landing page: 1,400-2,000 words. Shorter than a blog, more conversion-focused. |
| 30 | First-person usage is restricted | "We" and "our" only in Why Choose Us (Section 9) and Get in Touch (Section 10). Third person elsewhere. |

---

## Inline Flag Format

When a QA check fails, insert an inline flag directly in the landing page content at the point of failure. Flags use square brackets and ALL CAPS label, followed by details.

### Flag Types

| Flag | When to Use | Example |
|------|-------------|---------|
| `[META TITLE TOO LONG: X chars, max 55]` | Meta title exceeds 55 characters | `[META TITLE TOO LONG: 62 chars, max 55]` |
| `[META TITLE TOO SHORT: X chars, min 51]` | Meta title below 51 characters | `[META TITLE TOO SHORT: 45 chars, min 51]` |
| `[META DESCRIPTION TOO LONG: X chars, max 160]` | Description exceeds 160 characters | `[META DESCRIPTION TOO LONG: 172 chars, max 160]` |
| `[META DESCRIPTION TOO SHORT: X chars, min 150]` | Description below 150 characters | `[META DESCRIPTION TOO SHORT: 130 chars, min 150]` |
| `[UNVERIFIED CLAIM]` | Factual claim not in knowledge base | `[UNVERIFIED CLAIM: "largest in South India" — not in product files]` |
| `[KEYWORD MISSING: "term" X/mo]` | High-volume keyword not in page text | `[KEYWORD MISSING: "aluminium profiles" 6,600/mo]` |
| `[FORBIDDEN TERM: "term"]` | Term from forbidden list found | `[FORBIDDEN TERM: "KMC" found — use full company name]` |
| `[SELF-REFERENCING LINK: "anchor"]` | Internal link points to current page | `[SELF-REFERENCING LINK: "aluminium profiles" links to this page]` |
| `[H3 TAG FOUND: convert to H2]` | H3 tag found in content | `[H3 TAG FOUND: "Installation Methods" — convert to H2]` |
| `[INFORMATION REQUIRED]` | Data needed from client | `[INFORMATION REQUIRED: Monthly fabrication capacity]` |
| `[TESTIMONIAL REQUIRED]` | Testimonial placeholder | `[TESTIMONIAL REQUIRED: Add client testimonial when available]` |
| `[PRICING DISCLAIMER REQUIRED]` | Pricing shown without disclaimer | `[PRICING DISCLAIMER REQUIRED: Add approximate date stamp]` |
| `[ENGLISH VARIANT ERROR: "word"]` | Wrong English variant used | `[ENGLISH VARIANT ERROR: "color" should be "colour" per British English setting]` |
| `[EM DASH FOUND]` | Em dash used when not allowed | `[EM DASH FOUND: Replace with comma, semicolon, or full stop]` |
| `[MISSING SCHEMA: type]` | Required schema not included | `[MISSING SCHEMA: FAQPage]` |
| `[INSUFFICIENT INTERNAL LINKS: X, min 3]` | Fewer than 3 internal links | `[INSUFFICIENT INTERNAL LINKS: 2 found, min 3]` |
| `[KEYWORD DENSITY: X%]` | Density outside 1-2% range | `[KEYWORD DENSITY TOO HIGH: 3.2%, max 2%]` |

### Flag Rules

1. Place the flag inline, immediately after (or instead of) the problematic content.
2. Flags are temporary — they must be resolved before final output.
3. After resolving all flags, do a final search for `[` to ensure none remain.
4. Flags from the error correction rules (in SKILL.md) take precedence over general QA flags.

---

## Schema Markup Templates

Use these JSON-LD templates for the Schema Markup block in each landing page. Replace `{{config.field}}` placeholders with values from the config file.

### Product Schema

Use for physical products, manufactured goods, materials.

```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "{{page.h1_title}}",
  "description": "{{page.meta_description}}",
  "brand": {
    "@type": "Brand",
    "name": "{{config.company.name}}"
  },
  "manufacturer": {
    "@type": "Organization",
    "name": "{{config.company.name}}",
    "url": "{{config.company.website}}"
  },
  "url": "{{config.company.website}}/{{page.url_slug}}",
  "image": "{{page.hero_image_url}}",
  "category": "{{page.product_category}}",
  "areaServed": "{{config.audience.geography}}",
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "{{config.style.currency}}",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "{{config.company.name}}"
    }
  }
}
```

### Service Schema

Use for professional services, SaaS products, consulting.

```json
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "{{page.h1_title}}",
  "description": "{{page.meta_description}}",
  "provider": {
    "@type": "Organization",
    "name": "{{config.company.name}}",
    "url": "{{config.company.website}}"
  },
  "url": "{{config.company.website}}/{{page.url_slug}}",
  "areaServed": "{{config.audience.geography}}",
  "serviceType": "{{page.service_type}}"
}
```

### FAQPage Schema

Use for every landing page that has a FAQ section.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{{faq.question_1}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{faq.answer_1}}"
      }
    },
    {
      "@type": "Question",
      "name": "{{faq.question_2}}",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "{{faq.answer_2}}"
      }
    }
  ]
}
```

*Repeat the Question/Answer block for each FAQ item. Minimum 5, maximum 10.*

### BreadcrumbList Schema

```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "{{config.company.website}}"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "{{page.category_name}}",
      "item": "{{config.company.website}}/{{page.category_slug}}"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "{{page.h1_title}}",
      "item": "{{config.company.website}}/{{page.url_slug}}"
    }
  ]
}
```

### Organization Schema

Use when the company is a national/international brand without a single local storefront.

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{{config.company.name}}",
  "url": "{{config.company.website}}",
  "logo": "{{config.company.website}}/logo.png",
  "description": "{{config.company.description}}",
  "foundingDate": "{{config.company.founded}}",
  "numberOfEmployees": {
    "@type": "QuantitativeValue",
    "value": "{{config.company.employees}}"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "{{config.company.phone}}",
    "email": "{{config.company.email}}",
    "contactType": "sales"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{config.company.addresses[0].address}}",
    "addressLocality": "{{config.company.addresses[0].city}}",
    "addressRegion": "{{config.company.addresses[0].state}}",
    "addressCountry": "{{config.company.addresses[0].country}}"
  },
  "sameAs": []
}
```

### LocalBusiness Schema

Use when the company has a physical location that serves walk-in or local customers.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "{{config.company.name}}",
  "url": "{{config.company.website}}",
  "logo": "{{config.company.website}}/logo.png",
  "description": "{{config.company.description}}",
  "telephone": "{{config.company.phone}}",
  "email": "{{config.company.email}}",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "{{config.company.addresses[0].address}}",
    "addressLocality": "{{config.company.addresses[0].city}}",
    "addressRegion": "{{config.company.addresses[0].state}}",
    "addressCountry": "{{config.company.addresses[0].country}}",
    "postalCode": "{{config.company.addresses[0].postal_code}}"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "{{lookup_or_leave_placeholder}}",
    "longitude": "{{lookup_or_leave_placeholder}}"
  },
  "areaServed": "{{config.audience.geography}}",
  "priceRange": "{{page.price_range_indicator}}"
}
```

### Schema Selection Guide

| Business Type | Use These Schemas |
|--------------|-------------------|
| Physical product manufacturer | Product + FAQPage + BreadcrumbList + LocalBusiness |
| SaaS / digital service | Service + FAQPage + BreadcrumbList + Organization |
| E-commerce (physical goods) | Product + FAQPage + BreadcrumbList + Organization |
| Local service provider | Service + FAQPage + BreadcrumbList + LocalBusiness |
| Multi-location manufacturer | Product + FAQPage + BreadcrumbList + Organization (use LocalBusiness per location page) |
