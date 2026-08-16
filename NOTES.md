# Business Owner Notes — Anderson Junk Removal Pros

## NAP Consistency (Critical for Local SEO)

**NAP = Name, Address, Phone.** These three pieces of information must be identical everywhere they appear online. Inconsistencies confuse Google and suppress local rankings.

**Your official NAP:**
- **Name:** Anderson Junk Removal Pros *(use this exact name everywhere)*
- **Phone:** (843) 642-8417 *(use this exact format everywhere — with parentheses and hyphen)*
- **Address:** Anderson, SC *(If you add a street address later, use that exact format everywhere)*

### Where NAP Must Match Exactly
Every directory listing, citation, and online profile should use the identical name, phone, and address format above. Common places that need to match:

- [ ] Your website footer (update via Kadence Footer Builder in WordPress)
- [ ] Google Business Profile (when created)
- [ ] Yelp listing (when created)
- [ ] Facebook Business Page (when created)
- [ ] BBB profile (if applicable)
- [ ] Angi / HomeAdvisor / Thumbtack / Bark (if listed)
- [ ] Any local Chamber of Commerce directory
- [ ] YellowPages.com
- [ ] Bing Places for Business
- [ ] Apple Maps Connect
- [ ] NextDoor Business Profile

### Common NAP Mistakes to Avoid
- Don't use "Anderson Junk Removal" (without "Pros") anywhere — keep the full name consistent
- Don't alternate between "(843) 642-8417" and "843-642-8417" — pick one format and stick with it (parentheses format is preferred)
- If you get a CallRail tracking number, use it consistently in one category of listings — don't mix the tracking number and the real number in the same directories

---

## CallRail Setup

The phone number (843) 642-8417 currently appears throughout the website content and schema. If you use CallRail for call tracking:

1. Your **CallRail DNI (Dynamic Number Insertion)** script swaps the number on the website automatically — you don't need to update every page
2. For **static listings** (directories, GBP, Yelp) — use your real/forwarding number consistently, not the tracking number
3. File `deployment/callrail-setup.md` in this repo has the full setup guide

---

## Lead-Gen Disclosure (FTC Requirement)

The about.md page contains a placeholder:
`[TODO: insert lead-sharing disclosure once fulfillment partner is confirmed]`

**This is not optional.** The FTC's truth-in-advertising rules require lead-gen sites that share leads with third-party fulfillment partners to disclose that relationship clearly. Before launch (or as soon as a fulfillment partner is confirmed), replace this placeholder with accurate disclosure language — for example:

> "When you submit a request through this site, your information may be shared with licensed service providers in the Anderson, SC area who may contact you with a quote."

The exact wording should reflect your actual business model. Consult the fulfillment partner agreement for what disclosure language they require or recommend.

---

## Logo Files

**Both logo files are in `assets/` in this repo.**

| File | Use |
|---|---|
| `assets/logo-primary.svg` | Full logo (badge + wordmark) — website header, email signature |
| `assets/logo-icon.svg` | Badge mark only (144×144, transparent background) — favicon, small spaces |

**Brand color palette:**
- Primary green: `#1F3D2B`
- Accent orange: `#E8792E`
- Background/cream: `#F5F1E8`
- Dark text: `#2B2620`

**How to install in WordPress:**

1. **Upload both files:** WordPress Admin → Media Library → Add New → upload `logo-primary.svg` and `logo-icon.svg`
2. **Set the header logo:** Kadence → Header Builder → Logo element → select `logo-primary.svg`
3. **Set the favicon:** WordPress Admin → Appearance → Customize → Site Identity → Site Icon → select `logo-icon.svg`
4. **Update schema.json:** The `logo` field in `seo/schema.json` section `1_LocalBusiness_sitewide` already references `https://andersonjunkremovalpros.com/wp-content/uploads/logo-primary.svg` — confirm the Media Library URL matches after upload (it may append a size suffix)

**SVG note:** Some WordPress installs block SVG uploads by default. If you see an error, install the free plugin **"Safe SVG"** — it sanitizes and enables SVG uploads safely.

---

## Post-Launch Priority Checklist

### Week 1
- [ ] Verify wordpress-import.xml imported successfully — check all pages exist at their expected URLs
- [ ] Confirm Yoast SEO meta is set on all pages (check each page's Yoast panel)
- [ ] Add WPCode snippets for all schema blocks (see seo/schema.json)
- [ ] Set up Google Search Console and submit sitemap
- [ ] Enable LiteSpeed Cache and test PageSpeed Insights score (target 85+ mobile)
- [ ] Replace all `[TODO: ...]` placeholders in content

### Month 1
- [ ] Create Google Business Profile (if pursuing GBP strategy)
- [ ] Build 10–15 directory citations with consistent NAP
- [ ] Add the three Tier 1 city pages (Clemson, Easley, Seneca) to navigation
- [ ] Monitor Google Search Console for crawl errors or indexing issues

### Month 2–3
- [ ] Check rankings for primary keywords in Google
- [ ] Begin building backlinks (local business features, Upstate SC press)
- [ ] If real reviews are collected, revisit AggregateRating schema (see schema.json instructions)

---

## Files in This Repository

| File/Folder | Purpose |
|---|---|
| `content/homepage.md` | Homepage copy and section content |
| `content/services/` | All 5 service page content files |
| `content/locations/` | Tier 1 city pages (Clemson, Easley, Seneca) |
| `content/blog/` | All 10 blog posts |
| `content/contact.md` | Contact page copy |
| `content/about.md` | About page copy + FTC disclosure placeholder |
| `seo/schema.json` | All JSON-LD schema blocks with WPCode instructions |
| `seo/meta-tags.md` | Meta titles and descriptions for all pages |
| `seo/keyword-targets.md` | Primary and secondary keywords per page |
| `seo/technical-seo.md` | Sitemap, robots.txt, alt text, canonicals, Core Web Vitals |
| `theme-customizations/kadence-child/style.css` | Custom CSS for Kadence theme |
| `theme-customizations/kadence-child/design-notes.md` | Design decisions and Kadence implementation notes |
| `deployment/hostinger-setup.md` | WordPress setup guide for Hostinger |
| `deployment/callrail-setup.md` | CallRail integration guide |
| `deployment/launch-checklist.md` | Full pre-launch and post-launch checklist |
| `plugins/plugin-list.txt` | Required plugins and setup notes |
| `wordpress-import.xml` | WordPress WXR import file (core pages + initial 3 blog posts) |
| `generate_wxr.py` | Script that generated wordpress-import.xml |
| `wp_builder.py` | WordPress REST API page builder (alternative to WXR import) |
| `NOTES.md` | This file — business owner notes and NAP guidance |
