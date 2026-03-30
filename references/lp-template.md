# Landing Page Template — 11-Section Structure

This file is the single authority for landing page structure, layout types, image specs, and content guidelines. SKILL.md and seo-and-qa.md reference this file but do not repeat its contents.

---

## Table of Contents

1. [Section Format Standard](#section-format-standard)
2. [Section 1: Hero Banner](#section-1-hero-banner)
3. [Section 2: Trust Bar](#section-2-trust-bar)
4. [Section 3: Product/Service Definition](#section-3-productservice-definition)
5. [Section 4: Categories / Types](#section-4-categories--types)
6. [Section 5: Specifications](#section-5-specifications)
7. [Section 6: Variants / Finishes / Plans](#section-6-variants--finishes--plans)
8. [Section 7: Applications / Use Cases](#section-7-applications--use-cases)
9. [Section 8: Projects and Social Proof](#section-8-projects-and-social-proof)
10. [Section 9: Why Choose Us](#section-9-why-choose-us)
11. [Section 10: Get in Touch](#section-10-get-in-touch)
12. [Section 11: FAQ](#section-11-faq)
13. [Schema Markup Block](#schema-markup-block)
14. [Internal Linking Map](#internal-linking-map)
15. [Developer Notes](#developer-notes)

---

## Section Format Standard

Every section in the landing page must follow this format. This makes the output developer-ready — a frontend team can build directly from this structure.

```
## SECTION [N]: [SECTION NAME]
**Layout:** [layout type — e.g., "Full-width hero banner", "4-card grid, 2x2 desktop, stacked mobile"]
**Image:** [type] | [description] | Alt: "[alt text]" | [dimensions] | [position]
**Mobile:** [responsive behaviour if different from desktop]

[Content: headlines, body text, CTAs, tables]
```

### Layout Types Reference

| Layout Type | When to Use |
|-------------|-------------|
| Full-width hero banner | Section 1 only |
| Horizontal stat bar | Trust bar (Section 2), stat lines |
| Compact strip | Short definitions, partner credentials |
| Card grid (3-4 columns) | Categories, applications, USPs |
| Stacked tables | Specifications, pricing, comparisons |
| Table with columns | Variants, finishes, plans, features |
| Scrollable tiles | Project gallery, portfolio |
| Dark background centred | Contact/CTA sections |
| Accordion/collapsible | FAQ only |

### Image Spec Format

Every section that includes visuals must have an inline image spec:

```
**Image:** [TYPE] | [DESCRIPTION] | Alt: "[keyword-rich alt text]" | [WxH or aspect ratio] | [position]
```

- **TYPE**: Hero photo, Product close-up, Icon set, Application photo, Infrastructure photo, Logo strip, Team photo
- **DESCRIPTION**: What the image shows, specific enough for a photographer or stock search
- **ALT TEXT**: Descriptive, includes primary keyword where natural, includes company name for brand images
- **DIMENSIONS**: Suggested pixel dimensions or aspect ratio (e.g., 1920x600, 16:9, 400x300)
- **POSITION**: left, right, centred, background, inline

---

## Section 1: Hero Banner

**Purpose:** First impression. Communicate what the company offers for this product/service and prompt action.

**Layout:** Full-width hero banner with overlay text.

**Required elements:**
- **H1 heading**: Includes primary keyword. Max 70 characters. Format: "[Product/Service]: [Value Proposition] in [Location]"
- **Subheadline**: One sentence expanding on the H1. Includes a secondary keyword.
- **Primary CTA**: Action button (e.g., "Request a Quote", "Get Started", "Book a Demo")
- **Secondary CTA**: Lower-commitment action (e.g., "Call Now", "View Catalogue", "Learn More")
- **Hero image**: Full-width background or split layout. Product/application photo preferred over stock.

**Image:** Hero photo | [Product in use or hero application shot] | Alt: "[Product] [application] by [Company], [City]" | 1920x600 min | background

**Mobile:** Stack heading above image. CTAs full-width buttons. Reduce image height to 300px.

**Content guidelines:**
- H1 is the only H1 on the page. All other headings are H2.
- Primary keyword must appear in the first 100 words of page content (which starts here).
- Do not use generic headlines like "Welcome" or "Your Trusted Partner". Be specific to the product.
- Include location if the business serves a specific geography.

---

## Section 2: Trust Bar

**Purpose:** Instant credibility through numbers and credentials.

**Layout:** Horizontal stat bar — 4 items in a row, each with an icon and number.

**Required elements:**
- Exactly 4 stats from `config.social_proof.stats[]`
- Each stat: icon + number + label (e.g., "50+ Years Experience")
- Certification logos strip below (if available)

**Image:** Icon set | 4 stat icons (e.g., calendar, factory, handshake, map pin) | Alt: "[Company] key statistics" | 64x64 per icon | inline

**Mobile:** 2x2 grid. Certification logos scroll horizontally.

**Content guidelines:**
- Use real numbers from the config — never fabricate stats.
- Keep labels to 2-3 words maximum.
- If certification logos are available, display as a scrolling strip below the stats.

---

## Section 3: Product/Service Definition

**Purpose:** Compact explanation of what the product/service is. NOT a full explainer — that belongs in a blog post.

**Layout:** Compact strip — background colour or light border. Max 2-3 lines of text.

**Optional:** This section can be omitted if the product is self-explanatory to the target audience.

**Required elements:**
- One-line definition of the product/service
- Optional: small inline diagram or icon
- Link to blog post for detailed information (if one exists)

**Image:** Product diagram or icon | [Simple visual explaining the product] | Alt: "[Product] diagram" | 200x150 | inline-right

**Mobile:** Image above text. Full width.

**Content guidelines:**
- Maximum 2-3 sentences. If you need more, the content belongs in a blog.
- Include primary keyword naturally.
- For manufacturing/products: "what it is + what it's made of + key property"
- For SaaS/services: "what it does + who it's for + key benefit"
- For e-commerce: "what it is + key feature + why customers love it"

---

## Section 4: Categories / Types

**Purpose:** Show the range of product categories, service types, or plan tiers.

**Layout:** Card grid — 3-4 cards per row on desktop, stacked on mobile.

**Required elements:**
- Category/type name as card heading
- 2-3 line description per card
- Icon or small image per card
- Optional: "Learn More" link per card (to dedicated sub-page if it exists)

**Image:** Product category icons or photos | [One image per card showing the category] | Alt: "[Category name] — [Company]" | 400x300 per card | centred in card

**Mobile:** Single column, full-width cards.

**Content guidelines:**
- Use the company's own product/service categorisation from their knowledge base.
- Each card description should highlight what makes that category distinct.
- If there are more than 6 categories, group them or show top 4-6 with a "View All" link.
- Adapt section H2 heading to the industry:
  - Manufacturing: "Product Categories", "Our Product Range"
  - SaaS: "Plans and Pricing", "Features", "Solutions"
  - E-commerce: "Our Collections", "Shop by Category"
  - Services: "Our Services", "What We Offer"

---

## Section 5: Specifications

**Purpose:** Detailed technical data in scannable table format.

**Layout:** Full-width stacked tables. Each sub-table has its own sub-heading.

**Required sub-tables (include all that apply):**
1. **Sizes/Dimensions**: Available sizes, weight, dimensions
2. **Performance/Materials**: Materials, grades, alloys, performance metrics
3. **Standards/Compliance**: Applicable standards (BIS/IS, ASTM, BS EN, etc.)
4. **Pricing Guide** (conditional): Include ONLY if keyword research shows price-intent keywords with volume above 1,000/mo. Mark all prices as approximate with a date stamp.
5. **Installation/Processing Methods** (conditional): Include if the product requires installation or processing. Compact comparison table.

**Image:** Product close-up or technical diagram | [Detail shot showing a specification-relevant feature] | Alt: "[Product] specifications — [Company]" | 800x400 | above tables

**Mobile:** Tables scroll horizontally. Sub-headings remain visible.

**Content guidelines:**
- Use tables, not paragraphs, for spec data.
- All specifications must be verified against the product knowledge base. Never guess specifications.
- For pricing tables: always include a disclaimer ("Prices are approximate as of [Month Year]. Contact us for exact quotes.") and link to contact page.
- Adapt section H2 heading:
  - Manufacturing: "Specifications", "Technical Data"
  - SaaS: "Features and Capabilities", "Technical Specs"
  - E-commerce: "Product Details", "Materials and Care"
  - Services: "Service Details", "Scope and Deliverables"

---

## Section 6: Variants / Finishes / Plans

**Purpose:** Display product variants, finishes, colour options, or service/pricing tiers.

**Optional:** Omit if the product has no meaningful variants.

**Layout:** Table with columns or swatch grid (for colours/finishes).

**Required elements:**
- Table columns: Variant/Finish Name, Key Details, Best For / Popular Use Case
- Or: Swatch grid with colour/finish name and hover/tap detail

**Mobile:** Table scrolls horizontally. Swatch grid wraps to 3 columns.

**Content guidelines:**
- Link to full catalogue or colour chart if available (as downloadable PDF or page).
- Use actual product names from the knowledge base — never invent variant names.
- Adapt section H2 heading:
  - Manufacturing: "Colours and Finishes", "Available Variants"
  - SaaS: "Pricing Plans", "Editions"
  - E-commerce: "Available Options", "Colours and Sizes"

---

## Section 7: Applications / Use Cases

**Purpose:** Show how the product/service is used in real scenarios. Drive conversion through relevance.

**Layout:** Card grid with background images — 3 cards per row.

**Required elements:**
- Application/use case name as card heading
- 1-2 sentence description
- Background image showing the application
- Optional: name of a real project/client using this application (from `config.social_proof.projects[]`)

**CTA:** After the card grid, include a CTA block: Primary button + phone number or secondary action.

**Image:** Application photos | [Product/service in use in each application context] | Alt: "[Product] used in [application] — [project name if available]" | 400x300 per card | card background

**Mobile:** Single column cards. CTA full width.

**Content guidelines:**
- Use real project names from the config where available. If none exist for a specific application, describe the application without naming a project.
- Group applications by industry or use case, not by product variant.
- Adapt section H2 heading:
  - Manufacturing: "Applications", "Industries We Serve"
  - SaaS: "Use Cases", "Who Uses [Product]"
  - E-commerce: "How Customers Use [Product]", "Styling Ideas"
  - Services: "Case Studies", "Where We've Helped"

---

## Section 8: Projects and Social Proof

**Purpose:** Build trust through demonstrated experience. Most important conversion driver for B2B.

**Layout:** Scrollable project tiles (horizontal scroll or masonry grid) + stat line below.

**Required elements:**
- Minimum 6 project tiles from `config.social_proof.projects[]`
- Each tile: project name, type/category, optional image
- Stat line below tiles: pull from `config.social_proof.stats[]`
- Testimonial placeholder: if `config.social_proof.testimonials_available` is false, include a developer note: `<!-- [TESTIMONIAL REQUIRED] Add client testimonials when available -->`

**Image:** Project photos | [Completed project showing the company's work] | Alt: "[Project name] — [product/service] by [Company]" | 300x200 per tile | tile background

**Mobile:** Tiles scroll horizontally. Stat line stacks vertically.

**Content guidelines:**
- Only include projects that are verified in the config. Never fabricate project names.
- If fewer than 6 projects exist, include what is available and add `[INFORMATION REQUIRED: Additional project references needed]`.
- For B2C businesses, this section can show customer reviews, ratings, or Instagram-style user photos instead of project tiles.
- Adapt section H2 heading:
  - B2B: "Our Projects", "Selected Work"
  - B2C: "What Our Customers Say", "Customer Stories"
  - SaaS: "Trusted By", "Customer Success Stories"

---

## Section 9: Why Choose Us

**Purpose:** Answer "Why should I buy from THIS company?" Lead with the company's own value — not partner credentials.

**Layout:** 6 USP cards (2x3 grid on desktop) + optional partner/credential strip below.

**Required elements:**
- 6 USP cards from `config.products.usps[]` (supplement with knowledge base if fewer than 6)
- Each card: icon + headline (3-5 words) + 1-2 sentence description
- First USP should be the strongest conversion reason (e.g., "Ready Stock", "Same-Day Shipping", "Free Trial"), not company history
- Optional partner strip below: compact row of partner logos + one-line description

**Image:** Icon set | [6 icons representing each USP] | Alt: "Why choose [Company] — [USP summary]" | 80x80 per icon | centred in card

**Mobile:** 2-column grid for USP cards. Partner strip scrolls horizontally.

**Content guidelines:**
- Always lead with the company's own value proposition, not partner/supplier credentials.
- Partner/manufacturer credentials go in a supporting strip below the USP grid, not as headline content.
- Use first person ("we", "our") in this section — it is one of the few sections where first person is appropriate.
- Adapt section H2 heading:
  - Manufacturing: "Why Choose [Company] for [Product]"
  - SaaS: "Why [Product Name]", "The [Product] Advantage"
  - E-commerce: "Why Shop With Us", "The [Brand] Difference"

---

## Section 10: Get in Touch

**Purpose:** Conversion point. Make it easy to take action.

**Layout:** Dark background, centred text and buttons. No embedded contact form.

**Required elements:**
- Headline: "Get in Touch" or "Ready to Get Started?"
- Company phone number (from `config.company.phone`)
- Company email (from `config.company.email`)
- Primary CTA button: "Request a Quote" / "Get Started" / "Book a Demo"
- Secondary CTA: "Call Now" (linked to tel:) or "WhatsApp" (if available)
- Address (primary location from `config.company.addresses[0]`)

**Mobile:** CTAs full width. Address below contact details.

**Content guidelines:**
- No embedded contact forms on product/service landing pages. CTA buttons link to the dedicated contact page.
- Use first person ("we", "our") in this section.
- If WhatsApp is available (`config.company.whatsapp`), include a WhatsApp button with link: `https://wa.me/[number]`
- This section comes BEFORE FAQ — the conversion point should not be buried after FAQ content.

---

## Section 11: FAQ

**Purpose:** Capture long-tail SEO queries, answer remaining objections, and generate FAQPage schema.

**Layout:** Accordion/collapsible. Always the LAST content section on the page.

**Required elements:**
- 5-10 questions based on keyword research (use actual search queries as questions)
- Each answer: 2-4 sentences, adds unique value NOT already in the body content
- FAQ must support FAQPage schema markup

**Mobile:** Full-width accordion. One question open at a time.

**Content guidelines:**
- After writing FAQs, cross-check every answer against the body content. If the answer repeats information already visible on the page, replace the question with one that adds new value.
- Use actual search queries from keyword research as FAQ questions (rephrase as natural questions).
- Include price-intent FAQ if pricing keywords exist but a full pricing table is not in the body.
- Order questions from most-searched to least-searched.
- Do not start every answer with "Yes" or "No" — vary the opening.

---

## Schema Markup Block

After the FAQ section, include a schema markup code block with JSON-LD for:
- **Product** or **Service** schema (depending on the offering)
- **FAQPage** schema (all FAQ Q&As)
- **BreadcrumbList** schema (Home > [Category] > [This Page])
- **Organization** or **LocalBusiness** schema

See `references/seo-and-qa.md` for complete schema templates with `{{config.field}}` placeholders.

---

## Internal Linking Map

After schema markup, include a table mapping all internal links used in the page:

```
| Anchor Text | Destination URL | Section Used In |
|-------------|----------------|-----------------|
| [anchor] | [url] | [section number and name] |
```

Rules:
- Minimum 3 internal links per page (to related blog, related LP, contact page)
- No self-referencing links (page linking to itself)
- Use descriptive anchor text that includes keywords naturally
- Pull destinations from `config.technical.internal_links[]` and from other landing pages in the project

---

## Developer Notes

Final section of the landing page file. Include:

1. **Responsive behaviour**: Summarise mobile/tablet changes per section
2. **Image formats**: WebP with JPEG/PNG fallback, lazy-load below the fold
3. **Core Web Vitals targets**: LCP < 2.5s, INP < 200ms, CLS < 0.1
4. **Heading hierarchy**: H1 (hero only) > H2 (all section headings) — no H3 tags
5. **CTA styling**: Primary buttons should be visually prominent (not text links)
6. **Accessibility**: Alt text on all images, semantic HTML, ARIA labels on interactive elements
