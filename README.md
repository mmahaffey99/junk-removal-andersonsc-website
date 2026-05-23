# Anderson Junk Removal Pros — Website Repository

**Business:** Anderson Junk Removal Pros
**Location:** Anderson, South Carolina (SC)
**Purpose:** Conversion-focused local SEO website to generate phone calls and form leads

---

## What This Repository Contains

This repository holds all content, SEO assets, deployment instructions, and theme customizations needed to launch a high-converting WordPress website for a local junk removal business in Anderson, SC.

Every file is organized to make WordPress setup, content entry, and pre-launch configuration as straightforward as possible — even for non-developers.

---

## Free Tech Stack

| Layer | Tool | Cost |
|---|---|---|
| Hosting | Hostinger (hPanel) | Paid hosting, free setup |
| CMS | WordPress | Free |
| Theme | Kadence | Free |
| Page Builder Blocks | Kadence Blocks | Free |
| Forms | WPForms Lite | Free |
| SEO Plugin | Yoast SEO | Free |
| Caching | WP Super Cache | Free |
| Header/Footer Scripts | Insert Headers and Footers (WPBeginner) | Free |
| Phone Tracking | CallRail | Paid (separate account) |
| Image Compression | Squoosh.app | Free |
| Speed Testing | PageSpeed Insights (pagespeed.web.dev) | Free |
| Search Console | Google Search Console | Free |

**No paid plugins. No premium themes. No page builder subscriptions required.**

---

## Repository Structure

```
/
├── README.md                          ← You are here
├── theme-customizations/
│   └── kadence-child/
│       ├── style.css                  ← Custom CSS overrides for Kadence
│       └── design-notes.md           ← Design inspiration notes
├── plugins/
│   └── plugin-list.txt               ← All required plugins with install steps
├── content/
│   ├── homepage.md                   ← Full homepage copy (all sections)
│   ├── services/
│   │   ├── service-page-template.md  ← Reusable template
│   │   ├── furniture-removal-anderson.md
│   │   ├── appliance-removal-anderson.md
│   │   ├── yard-waste-removal-anderson.md
│   │   ├── estate-cleanouts-anderson.md
│   │   └── construction-debris-removal-anderson.md
│   ├── contact.md                    ← Contact page copy
│   └── blog/
│       ├── junk-removal-cost-anderson-sc.md
│       ├── how-often-junk-removal-anderson.md
│       └── junk-removal-diy-vs-professional-anderson.md
├── seo/
│   ├── schema.json                   ← Local business + FAQ JSON-LD schema
│   ├── meta-tags.md                  ← Meta titles & descriptions for every page
│   └── keyword-targets.md           ← Target keywords per page
└── deployment/
    ├── hostinger-setup.md            ← Full step-by-step deployment guide
    ├── callrail-setup.md             ← CallRail placeholder replacement guide
    └── launch-checklist.md          ← Pre and post-launch checklist
```

---

## How to Deploy (Quick Summary)

Full instructions are in `deployment/hostinger-setup.md`. At a high level:

1. **Buy hosting** on Hostinger (Business or Cloud plan recommended)
2. **Install WordPress** via hPanel one-click installer
3. **Install plugins** listed in `plugins/plugin-list.txt`
4. **Install Kadence theme** and upload the CSS from `theme-customizations/kadence-child/style.css`
5. **Enter page content** from the `content/` folder into WordPress
6. **Configure Yoast SEO** using meta data from `seo/meta-tags.md`
7. **Add schema markup** from `seo/schema.json` via Insert Headers and Footers plugin
8. **Replace all CALLRAIL_PLACEHOLDER** instances per `deployment/callrail-setup.md`
9. **Run through** `deployment/launch-checklist.md` before going live

---

## Critical Pre-Launch: CALLRAIL_PLACEHOLDER

Every phone number on this site uses the token `CALLRAIL_PLACEHOLDER`. Before launch, do a find-and-replace across all WordPress pages, widgets, and the schema JSON:

- Replace `CALLRAIL_PLACEHOLDER` → your display number (e.g. `(864) 555-0192`)
- Replace `tel:CALLRAIL_PLACEHOLDER` → your tel link (e.g. `tel:+18645550192`)

See `deployment/callrail-setup.md` for the full checklist of every location.

---

## Goals

1. **Rank on page 1 of Google** for "junk removal Anderson SC" and related local keywords
2. **Convert visitors into leads** via phone call or form submission

Every design decision, content choice, and SEO configuration in this repository serves those two goals.

---

*Last updated: 2026 | Anderson Junk Removal Pros | Anderson, SC*
