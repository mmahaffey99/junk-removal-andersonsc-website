# Technical SEO Implementation Guide — Anderson Junk Removal Pros

## Sitemap Structure

The XML sitemap tells Google which pages exist and their relative priority. Yoast SEO generates your sitemap automatically at `https://andersonjunkremovalpros.com/sitemap_index.xml`.

### After importing the WXR file, verify these URLs appear in Yoast's sitemap:

**Core pages (Priority: 1.0)**
- `https://andersonjunkremovalpros.com/` — Homepage

**Service pages (Priority: 0.9)**
- `https://andersonjunkremovalpros.com/furniture-removal-anderson/`
- `https://andersonjunkremovalpros.com/appliance-removal-anderson/`
- `https://andersonjunkremovalpros.com/yard-waste-removal-anderson/`
- `https://andersonjunkremovalpros.com/estate-cleanouts-anderson/`
- `https://andersonjunkremovalpros.com/construction-debris-removal-anderson/`

**City/Location pages (Priority: 0.8)**
- `https://andersonjunkremovalpros.com/junk-removal-clemson-sc/`
- `https://andersonjunkremovalpros.com/junk-removal-easley-sc/`
- `https://andersonjunkremovalpros.com/junk-removal-seneca-sc/`

**Support pages (Priority: 0.5)**
- `https://andersonjunkremovalpros.com/about/`
- `https://andersonjunkremovalpros.com/contact/`
- `https://andersonjunkremovalpros.com/blog/`

**Blog posts (Priority: 0.6)**
- `https://andersonjunkremovalpros.com/junk-removal-cost-anderson-sc/`
- `https://andersonjunkremovalpros.com/how-often-junk-removal-anderson/`
- `https://andersonjunkremovalpros.com/junk-removal-diy-vs-professional-anderson/`
- `https://andersonjunkremovalpros.com/where-to-take-junk-anderson-county/`
- `https://andersonjunkremovalpros.com/how-often-clean-garage-anderson/`
- `https://andersonjunkremovalpros.com/anderson-county-bulk-trash-vs-junk-removal/`
- `https://andersonjunkremovalpros.com/how-to-dispose-old-refrigerator-anderson-sc/`
- `https://andersonjunkremovalpros.com/yard-debris-after-storm-upstate-sc/`
- `https://andersonjunkremovalpros.com/estate-cleanout-checklist-anderson-sc/`
- `https://andersonjunkremovalpros.com/junk-removal-vs-dumpster-rental-anderson/`

### How to configure Yoast sitemap priorities:
1. WordPress Admin → SEO (Yoast) → Settings → Site features → XML sitemaps → enable
2. The sitemap auto-generates. Yoast does not expose per-page priority controls in the free version.
3. Confirm the sitemap exists by visiting `/sitemap_index.xml` in a browser.
4. Submit the sitemap URL to Google Search Console once the domain is verified.

### Pages to EXCLUDE from sitemap (Yoast will handle by default):
- `/privacy-policy/` — not needed in sitemap but won't hurt if included
- Tag/category archive pages (set these to noindex in Yoast)

---

## robots.txt

**Location:** `https://andersonjunkremovalpros.com/robots.txt`
WordPress generates this automatically. You can customize it via Yoast SEO (free version) or a plugin.

**Recommended robots.txt content:**

```
User-agent: *
Allow: /

Sitemap: https://andersonjunkremovalpros.com/sitemap_index.xml

# Block wp-admin and common junk paths
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

# Block search result URLs (thin content)
Disallow: /?s=
Disallow: /search/

# Block calendar archive pages (thin content)
Disallow: /date/

# Block author pages if no author content (single-author site)
Disallow: /author/
```

**How to customize in WordPress:**
1. WordPress Admin → SEO (Yoast) → Tools → File editor → robots.txt tab
2. Paste the content above (Yoast will preserve the default directives and add yours)
3. Save
4. Test at: https://search.google.com/search-console/robots-testing-tool

---

## Image Alt Text Standards

Every image on the site needs descriptive alt text for accessibility and Google Image indexing.

### Naming convention for image files:
Use descriptive, keyword-containing filenames before upload:
- `junk-removal-anderson-sc-truck.jpg` (not `IMG_4521.jpg`)
- `furniture-removal-anderson-sc-sofa.jpg`
- `estate-cleanout-anderson-sc-before.jpg`

### Alt text formula:
`[What the image shows] + [location if relevant]`

| Image | Bad Alt | Good Alt |
|---|---|---|
| Crew loading truck | "junk removal" | "Junk removal crew loading furniture into truck in Anderson, SC" |
| Hero background | "" (empty) | "Junk removal service in Anderson, SC — truck loaded and ready" |
| Before/after | "before after" | "Estate cleanout in Anderson, SC — before and after" |
| Logo | "logo" | "Anderson Junk Removal Pros logo" |
| Service area map | "" | "Junk removal service area map covering Anderson and surrounding Upstate SC cities" |

### How to set alt text in WordPress:
- When uploading: Media Library → click image → "Alternative Text" field on the right
- In page editor: click image block → "Alt text" field in the right sidebar

---

## Canonical Tags

Canonical tags tell Google which URL is the "official" version when duplicate content could exist.

### Yoast handles canonicals automatically — but verify these cases:

**Homepage:** Must be `https://andersonjunkremovalpros.com/` (with trailing slash, HTTPS)
- Go to Yoast SEO → Settings → Site → verify canonical points to root domain

**Paginated blog:** If `/blog/page/2/` exists, Yoast automatically sets canonical to itself (correct).

**Check for accidental duplicates:**
1. Visit https://andersonjunkremovalpros.com/?p=1 (sample post by ID) — should redirect to the real slug, not be a separate page
2. Verify `http://` redirects to `https://` (SSL redirect — set in Hostinger control panel)
3. Verify `www.` redirects to non-www (or vice versa) — set this in Hostinger to be consistent

**Manual canonical for city pages (if Yoast doesn't set correctly):**
In Yoast on each city page → Advanced tab → Canonical URL → enter the correct URL (e.g. `https://andersonjunkremovalpros.com/junk-removal-clemson-sc/`)

---

## Core Web Vitals — Optimization Checklist

Google uses Core Web Vitals (LCP, CLS, FID/INP) as ranking signals. Kadence + Hostinger + these settings should put you in a good position.

### LCP (Largest Contentful Paint) — target: under 2.5 seconds

- [ ] **Hero image optimized:** Compress to under 200KB using squoosh.app before uploading. Use JPG format at 1920×900px.
- [ ] **LiteSpeed Cache enabled:** WordPress Admin → LiteSpeed Cache → enable all basic settings (HTML, CSS, JS minification)
- [ ] **Preload LCP image:** In WordPress Admin → LiteSpeed Cache → Image Optimization → add hero image URL to preload list
- [ ] **No Google Fonts:** Style.css uses system font stack only — already implemented
- [ ] **Hostinger CDN:** Enable in Hostinger hPanel under Performance → CDN

### CLS (Cumulative Layout Shift) — target: under 0.1

- [ ] **Set image dimensions:** Always add width and height attributes to img tags (WordPress/Gutenberg does this automatically for uploaded images)
- [ ] **No late-loading ads or embeds** — no third-party embeds that resize after load
- [ ] **Form layout stable:** WPForms renders inline, no layout shift

### INP (Interaction to Next Paint) — target: under 200ms

- [ ] **Minimize unused JavaScript:** Deactivate any unused plugins (extra plugins add JS even when not visually present on page)
- [ ] **LiteSpeed Cache → JS optimization:** Combine and defer non-critical JS

### Testing Tools
- PageSpeed Insights: https://pagespeed.web.dev/ — test both mobile and desktop
- Google Search Console → Core Web Vitals report (requires 28+ days of traffic data)
- Chrome DevTools → Lighthouse (run locally before traffic arrives)

---

## Internal Linking Map

Internal links distribute PageRank and help Google understand site structure. Every page should link to relevant sibling pages.

### From Homepage → link to:
- All 5 service pages (service cards section)
- All 3 city pages (service areas section)
- Contact page (CTA sections)
- Blog (blog preview section or footer nav)

### From each Service page → link to:
- Homepage (in breadcrumb)
- 2–3 related service pages (e.g., Furniture Removal → link to Appliance Removal, Estate Cleanouts)
- Contact page (CTA section)
- Relevant blog posts (e.g., Furniture Removal → link to "DIY vs. Professional" blog post)

### From each City page → link to:
- Homepage (in breadcrumb)
- All 5 service pages (services offered in that city)
- Contact page (CTA)

### From Blog posts → link to:
- Relevant service pages (e.g., cost guide → link to all service pages)
- Contact page (end-of-post CTA)
- Related blog posts (2 internal links minimum per post)

### Priority internal links to add immediately post-launch:
1. Homepage → Clemson page, Easley page, Seneca page (update service areas section)
2. Blog post "Cost Guide" → all 5 service pages
3. Blog post "DIY vs. Professional" → Contact page (strong CTA)
4. Estate Cleanouts service page → "Estate Cleanout Checklist" blog post

---

## Google Search Console Setup

1. Go to https://search.google.com/search-console/
2. Add property → URL prefix → `https://andersonjunkremovalpros.com`
3. Verify via HTML tag method: copy the meta tag, add it to WordPress via Yoast SEO → Settings → Site connections → Google verification
4. After verification: Sitemaps → add `sitemap_index.xml`
5. Monitor: Index coverage, Core Web Vitals, Search performance (after 4–6 weeks of traffic)
