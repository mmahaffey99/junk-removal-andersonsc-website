# Launch Checklist — Anderson Junk Removal Pros
**Complete every item below before and after going live.**
**This checklist is designed to be worked top-to-bottom, in order.**

---

## PRE-LAUNCH CHECKLIST

### ① Placeholder Replacement
- [ ] All `CALLRAIL_PLACEHOLDER` replaced with real CallRail tracking number (display format)
- [ ] All `tel:CALLRAIL_PLACEHOLDER` replaced with real tel link format (e.g. `tel:+18645550192`)
- [ ] `YOUR_NOTIFICATION_EMAIL@placeholder.com` replaced with real business email in WPForms
- [ ] `https://www.YOUR-DOMAIN-PLACEHOLDER.com` replaced with real domain in schema JSON
- [ ] `YOUR-DOMAIN-PLACEHOLDER.com` replaced in all other files where it appears

### ② CallRail Configuration
- [ ] CallRail account created and local 864 area code number purchased
- [ ] CallRail JavaScript tracking snippet added via Insert Headers and Footers → Scripts in Header
- [ ] CallRail email notification active for every new call
- [ ] CallRail SMS notification active (recommended)
- [ ] Test call made and confirmed visible in CallRail dashboard

### ③ WPForms Setup
- [ ] Quote request form built with all required fields (Name, Phone, Email, Project description)
- [ ] Notification email updated to real business address
- [ ] Confirmation message set: "Thanks! We'll be in touch within 1 business day."
- [ ] Test form submission completed — confirmation message displays correctly
- [ ] Form notification email received in your inbox (check spam folder too)

### ④ SEO Configuration (Yoast)
- [ ] Yoast SEO setup wizard completed
- [ ] Site connected to Google Search Console
- [ ] Meta title and description entered for Homepage (from `seo/meta-tags.md`)
- [ ] Meta title and description entered for all 5 service pages
- [ ] Meta title and description entered for Contact page
- [ ] Meta title and description entered for all 3 blog posts
- [ ] Focus keyphrase set for each page (from `seo/keyword-targets.md`)
- [ ] XML sitemap enabled (Yoast → Settings → General → Features)
- [ ] Sitemap URL confirmed working: `https://yourdomain.com/sitemap_index.xml`

### ⑤ Schema Markup
- [ ] Local Business JSON-LD schema added to site header via Insert Headers and Footers
- [ ] FAQ Page JSON-LD schema added to site header via Insert Headers and Footers
- [ ] Both schemas validated at search.google.com/test/rich-results (no errors)
- [ ] Phone number in schema matches CallRail number

### ⑥ Pages & Content
- [ ] Homepage published with all 10 sections complete
- [ ] All 5 service pages published at correct slugs:
  - [ ] `/furniture-removal-anderson/`
  - [ ] `/appliance-removal-anderson/`
  - [ ] `/yard-waste-removal-anderson/`
  - [ ] `/estate-cleanouts-anderson/`
  - [ ] `/construction-debris-removal-anderson/`
- [ ] Contact page published at `/contact/`
- [ ] Privacy Policy page published at `/privacy-policy/`
- [ ] All 3 blog posts published at correct URLs
- [ ] No placeholder text remaining on any published page (`[CITY]`, `[BUSINESS_NAME]`, etc.)

### ⑦ Design & Mobile
- [ ] Custom CSS from `theme-customizations/kadence-child/style.css` applied
- [ ] Sticky header shows business name left, CTA button right on desktop
- [ ] Hero section shows H1, subheadline, and CTA button above fold on desktop
- [ ] Quote form visible above or near fold on desktop
- [ ] Tested on iPhone SE width (375px) — hero content readable without horizontal scroll
- [ ] All phone numbers use `<a href="tel:...">` links (tappable on mobile)
- [ ] CTA buttons minimum 44px tap target height on mobile
- [ ] Form fields full-width on mobile (no horizontal scroll on form)
- [ ] Footer links are tappable on mobile
- [ ] No horizontal scroll on any screen size (375px minimum)

### ⑧ Technical
- [ ] SSL certificate active — site loads on `https://` (not http://)
- [ ] WordPress address and Site address both set to `https://` in Settings → General
- [ ] Permalink structure set to Post name (`/%postname%/`)
- [ ] Homepage set as static front page in Settings → Reading
- [ ] WP Super Cache enabled and caching active
- [ ] All images compressed before upload (target: hero <200KB, all others <100KB)
- [ ] Alt text added to all images
- [ ] WordPress admin username changed from default "admin" to something unique
- [ ] WordPress admin password is strong and saved securely

### ⑨ Performance Testing
- [ ] PageSpeed score tested at pagespeed.web.dev
  - [ ] Mobile score: **85 or above** ✓
  - [ ] Desktop score: **90 or above** ✓
- [ ] If scores are below target, address top recommendations in PageSpeed report

### ⑩ Final Review
- [ ] Call the phone number from a personal cell — confirm it rings the correct destination
- [ ] Submit the quote form — confirm email notification is received
- [ ] Visit every page on mobile and confirm it looks and functions correctly
- [ ] Visit every page on desktop and confirm layout is correct
- [ ] All internal links work (no 404 errors)
- [ ] Hero background image replaced with real Anderson, SC job photo (not placeholder)

---

## POST-LAUNCH CHECKLIST

Complete these tasks within the first 48 hours after going live:

### Google Business Profile
- [ ] Go to business.google.com and create or claim your Google Business Profile
- [ ] Enter business name: **Anderson Junk Removal Pros**
- [ ] Category: **Junk Removal Service** (primary), **Hauling Service** (secondary)
- [ ] Add your website URL
- [ ] Add phone number (your CallRail tracking number)
- [ ] Add service areas: Anderson, Clemson, Seneca, Easley, Belton, Honea Path, Williamston, Pendleton, Iva, Walhalla — all in SC
- [ ] Add business hours: Monday–Saturday 7AM–7PM
- [ ] Add service descriptions from your service pages
- [ ] Verify your Google Business Profile (by postcard, phone, or email as available)

### Search Console
- [ ] Google Search Console verified and active (connected via Yoast wizard)
- [ ] XML sitemap submitted: Settings → Sitemaps → add `sitemap_index.xml`
- [ ] Request indexing for Homepage: URL Inspection → your homepage URL → Request Indexing

### Online Directories (Citations)
Submit your business information to these free directories within the first week. Consistent NAP (Name, Address, Phone) across all listings helps local SEO:
- [ ] **Yelp** — biz.yelp.com
- [ ] **Angi** — pro.angi.com
- [ ] **Thumbtack** — thumbtack.com/pro
- [ ] **HomeAdvisor** — homeadvisor.com/contractor
- [ ] **Nextdoor** — nextdoor.com/business
- [ ] **Facebook Business Page** — business.facebook.com
- [ ] **Better Business Bureau** — bbb.org (free listing)

### Reviews
- [ ] Ask your first 5 satisfied customers for Google reviews (direct link from Google Business Profile)
- [ ] Set up a review request process for all future customers

### Ongoing (monthly)
- [ ] Check Google Search Console weekly for crawl errors and keyword impressions
- [ ] Publish 1 new blog post per month targeting a new local keyword
- [ ] Monitor CallRail for call volume and missed calls
- [ ] Check WPForms for form submissions daily during business hours
- [ ] Respond to all Google reviews (positive and negative)

---

## QUICK REFERENCE — KEY URLs

| Purpose | URL |
|---|---|
| WordPress Admin | `https://yourdomain.com/wp-admin` |
| Google Search Console | search.google.com/search-console |
| Google Business Profile | business.google.com |
| PageSpeed Test | pagespeed.web.dev |
| Rich Results Test | search.google.com/test/rich-results |
| CallRail Dashboard | app.callrail.com |
| XML Sitemap | `https://yourdomain.com/sitemap_index.xml` |

---

*Anderson Junk Removal Pros | Anderson, SC | Last updated 2026*
