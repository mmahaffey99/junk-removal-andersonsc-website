# Design Notes — Inspiration & Application

## Inspiration Site Analysis

**Reference:** https://www.autoglassnola.com/

### Key Design Principles Observed

**Layout & Structure**
- Clean, uncluttered layout with generous white space
- Sticky header stays visible on scroll with logo left, CTA right
- Hero section is full-width with a strong overlaid headline on a dark background image
- Content is organized into clearly separated horizontal sections with alternating background colors
- No visual clutter — each section has one clear purpose

**Typography**
- Bold, heavy headlines that are instantly scannable
- Body text is readable at comfortable size (16–17px range)
- Clear visual hierarchy: headline → subheadline → body → CTA
- No decorative or script fonts — clean and professional

**Color Use**
- Neutral palette (dark, white, light gray)
- High contrast between text and background at all times
- CTA buttons use the darkest/most contrasting color available
- Accent colors used sparingly — the phone number and primary CTA get the most visual weight

**Calls to Action**
- Phone number is always prominent and visible — appears in header, hero, and footer
- Primary CTA buttons are large, high-contrast, and use action-oriented copy
- The form is positioned where it can capture users who aren't ready to call

**Trust Signals**
- Trust indicators (licensed, insured, reviews) appear early — above or near the fold
- Social proof (star ratings, review counts) displayed prominently
- Simple, confident language — no overdesigned badges needed

**Mobile Behavior**
- Header collapses cleanly on mobile
- Phone number is always tappable with adequate touch target
- Form fields are full-width and easy to use with thumbs
- CTA button text is short enough to read at a glance

---

## How These Principles Are Applied to Anderson Junk Removal Pros

### Header
- Business name left, "Call Now — Free Quote" button right
- Button uses `#1C1C1C` background / `#FFFFFF` text for maximum contrast
- Sticky on scroll — phone number always accessible

### Hero Section
- Dark overlay on background image (replace placeholder with real Anderson, SC job photo)
- H1 in white, large, bold — optimized for SEO ("Junk Removal Near Me | Anderson, SC")
- Subheadline reinforces trust and location
- CTA button matches header button style
- Form positioned to the right on desktop, stacked below on mobile

### Section Separation
- White sections and `#F5F5F5` sections alternate for visual rhythm
- Each section has a clear H2 headline and a single purpose

### Color Application
- `#FFFFFF` — main content backgrounds
- `#F5F5F5` — Trust Bar, Why Choose Us, FAQ sections
- `#1C1C1C` — all CTA buttons, final CTA section background, sticky header button
- `#1A1A1A` — all body text, headlines
- `#E0E0E0` — borders, card outlines, form field borders

### Font Strategy
- System font stack only (no Google Fonts) for faster load time
- Bold weight for all headlines
- 17px body text, 1.65 line-height for readability

---

## WordPress/Kadence Implementation Notes

1. **Kadence Header Builder:** Use Header Row → Left column (logo/name), Right column (button)
   - Set button to "sticky" so it persists on scroll
2. **Hero Section:** Use Kadence full-width section block with background image option
   - Set overlay opacity to ~55% for readability
3. **Service Cards:** Use Kadence Info Box blocks in a 3-column Kadence Row block
4. **FAQ:** Use Kadence Accordion block — no custom coding required
5. **Trust Bar:** Use Kadence Row block with 4 equal columns, centered text
6. **Final CTA Section:** Use Kadence Section block with `#1C1C1C` background color set in block settings

---

## Photo Placeholder Note

The hero section references a background image. Before launch:
- Take or source a high-quality photo of a completed junk removal job in Anderson, SC
- Compress the image at squoosh.app to under 200KB before uploading
- Recommended dimensions: 1920px × 900px, JPG format
- Replace the placeholder background image in Kadence → Row → Background → Image
