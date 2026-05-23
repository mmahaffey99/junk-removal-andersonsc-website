# CallRail Setup & Placeholder Replacement Guide
**Anderson Junk Removal Pros**

Complete this guide before your website goes live. Every step is required.

---

## STEP 1 — Get Your CallRail Tracking Number

1. Log into your CallRail account at **callrail.com**
2. Go to **Numbers → Buy a Number**
3. Select a local area code for Anderson, SC (area code **864**)
4. Purchase the number — note both:
   - **Display format:** e.g., `(864) 555-0192` ← shown on the website
   - **Tel link format:** e.g., `tel:+18645550192` ← used in href links

---

## STEP 2 — Get Your CallRail JavaScript Snippet

1. In CallRail, go to **Settings → Website → Tracking Code**
2. Copy the JavaScript snippet — it looks like this:
   ```html
   <script type="text/javascript">
     (function() {
       var ca = document.createElement('script');
       ca.type = 'text/javascript';
       ca.async = true;
       ca.src = ("https:" == document.location.protocol ? "https://cdn" : "http://cdn")
                + ".callrail.com/companies/XXXXXXXX/[account].js";
       var sc = document.getElementsByTagName('script')[0];
       sc.parentNode.insertBefore(ca, sc);
     })();
   </script>
   ```
3. In WordPress Admin, go to **Settings → Insert Headers and Footers**
4. Paste this snippet into the **"Scripts in Header"** field
5. Click **"Save"**

---

## STEP 3 — Replace All CALLRAIL_PLACEHOLDER Instances

Do a find-and-replace across all WordPress pages, widgets, forms, and the schema:

### Find: `CALLRAIL_PLACEHOLDER`
### Replace with: your display number, e.g. `(864) 555-0192`

### Find: `tel:CALLRAIL_PLACEHOLDER`
### Replace with: your tel link, e.g. `tel:+18645550192`

---

## COMPLETE LIST OF LOCATIONS TO REPLACE

Go through every item below and confirm the replacement is in place:

### WordPress Pages
- [ ] **Homepage — Sticky Header** button text and href
- [ ] **Homepage — Hero Section** CTA button text and href
- [ ] **Homepage — FAQ Section** (2 instances within FAQ answers)
- [ ] **Homepage — Service Areas section** (callout below the list)
- [ ] **Homepage — Final CTA Section** display number and href
- [ ] **Homepage — Footer** display number and href

### Service Pages (5 pages — check each one)
- [ ] **Furniture Removal page** — CTA section at bottom
- [ ] **Appliance Removal page** — CTA section at bottom
- [ ] **Yard Waste Removal page** — CTA section at bottom
- [ ] **Estate Cleanouts page** — CTA section at bottom
- [ ] **Construction Debris Removal page** — CTA section at bottom

### Contact Page
- [ ] **Contact page** — right column phone display and href

### Blog Posts
- [ ] **Blog Post 1** (cost guide) — soft CTA at end
- [ ] **Blog Post 2** (how often) — soft CTA at end
- [ ] **Blog Post 3** (DIY vs pro) — soft CTA at end

### Schema Markup (Insert Headers and Footers)
- [ ] **LocalBusiness schema** — `"telephone"` field
- [ ] **FAQ schema** — answers that reference the phone number (2 instances)

### WPForms
- [ ] **Notification email** — update to your real business email (not CallRail related, but do it now)
- [ ] **Confirmation message** — verify it reads correctly and has no placeholder text

---

## STEP 4 — Test CallRail Dynamic Number Insertion (DNI)

CallRail's JavaScript snippet automatically swaps the displayed phone number for tracking purposes. After adding the snippet:

1. Visit your website in a browser (not logged in to WordPress)
2. The phone number should display — CallRail's DNI will activate and track the session
3. Click the phone number — it should open your dialer (on mobile) or show the number clearly
4. Make a test call from a real phone
5. In CallRail, go to **Activity** — confirm the test call appears in your dashboard within 60 seconds

---

## STEP 5 — Set Up CallRail Notifications

1. In CallRail, go to **Settings → Notifications**
2. Enable **email notification** for every new call — enter your business email
3. Enable **SMS notification** if you want real-time text alerts for new calls (recommended)
4. Set business hours for after-hours call handling as desired

---

## STEP 6 — Verify Everything Is Working

Final verification checklist:
- [ ] CallRail JavaScript snippet added to site header via Insert Headers and Footers
- [ ] All `CALLRAIL_PLACEHOLDER` replaced with display number
- [ ] All `tel:CALLRAIL_PLACEHOLDER` replaced with tel link
- [ ] Test call made and confirmed in CallRail dashboard
- [ ] CallRail email/SMS notifications active
- [ ] WPForms notification email updated to real business email
- [ ] Test form submitted and email notification received

---

## TROUBLESHOOTING

**Problem:** CallRail number not showing / CALLRAIL_PLACEHOLDER still visible
- **Fix:** Search your WordPress pages for the exact text "CALLRAIL_PLACEHOLDER" — in the WordPress block editor, use Ctrl+F or the Find tool. Some instances may be inside custom HTML blocks or widget areas.

**Problem:** Calls not showing in CallRail dashboard
- **Fix:** Confirm the JavaScript snippet is in the site header (use browser DevTools → Sources and search for "callrail"). Make sure you didn't paste it in the footer by mistake.

**Problem:** Tel link not working on desktop
- **Fix:** Desktop behavior varies — tel: links open Skype, FaceTime, or similar depending on the user's computer setup. This is expected. On mobile, it always opens the dialer correctly.
