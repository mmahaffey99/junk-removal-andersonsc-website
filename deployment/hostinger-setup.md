# Hostinger Setup Guide — Anderson Junk Removal Pros
**Full step-by-step deployment guide for WordPress on Hostinger**

---

## PART 1 — INSTALLING WORDPRESS ON HOSTINGER

### Step 1: Purchase Hostinger Hosting
1. Go to hostinger.com
2. Select **Business Web Hosting** or **Cloud Startup** plan (both support the performance you need)
3. Complete purchase and verify your email address

### Step 2: Access hPanel (Hostinger Control Panel)
1. Log into your Hostinger account at hpanel.hostinger.com
2. Click **"Websites"** in the top navigation
3. Click **"Create or migrate a website"** → **"Create a new website"**

### Step 3: One-Click WordPress Install
1. Select **"WordPress"** as your website type
2. Enter your WordPress admin details:
   - **Username:** Choose something other than "admin" (security best practice)
   - **Password:** Use a strong, unique password — save it in a password manager
   - **Email:** Your business email address
3. Select your domain name
4. Click **"Finish setup"**
5. Hostinger will install WordPress automatically — takes 1–3 minutes

### Step 4: Enable SSL (HTTPS)
1. In hPanel, go to **Security → SSL**
2. Click **"Install"** next to your domain for the free SSL certificate
3. Wait for SSL to activate (may take up to 30 minutes)
4. In WordPress Admin → Settings → General:
   - Set WordPress Address (URL) to `https://yourdomain.com`
   - Set Site Address (URL) to `https://yourdomain.com`
5. Click "Save Changes"

---

## PART 2 — INITIAL WORDPRESS CONFIGURATION

### Step 5: Log Into WordPress Admin
1. Go to `https://yourdomain.com/wp-admin`
2. Log in with the username and password from Step 3

### Step 6: Set Permalink Structure
1. In WordPress Admin, go to **Settings → Permalinks**
2. Select **"Post name"** — this creates URLs like `/furniture-removal-anderson/`
3. Click **"Save Changes"**
4. This is critical for SEO — do not skip this step

### Step 7: Delete Default Content
1. Go to **Posts** → delete "Hello World" post
2. Go to **Pages** → delete "Sample Page"
3. Go to **Comments** → delete any default comments

### Step 8: Set a Static Homepage
1. Create your homepage page first (see Part 4)
2. Go to **Settings → Reading**
3. Select **"A static page"**
4. Set **"Homepage"** to your Homepage page
5. Set **"Posts page"** to a Blog page you create
6. Click "Save Changes"

---

## PART 3 — THEME INSTALLATION

### Step 9: Install Kadence Theme
1. Go to **Appearance → Themes → Add New**
2. Search for **"Kadence"**
3. Find the theme by **Kadence WP** — click **"Install"** then **"Activate"**

### Step 10: Apply Custom CSS (from this repository)
The custom CSS is in `theme-customizations/kadence-child/style.css`.

**Method: Additional CSS (Recommended for quick setup)**
1. Go to **Appearance → Customize → Additional CSS**
2. Copy the entire contents of `style.css` from this repository
3. Paste it into the Additional CSS field
4. Click **"Publish"**

**Alternative: Kadence Child Theme**
For more permanent control, create a child theme:
1. Create a folder on your computer called `kadence-child`
2. Add a `style.css` file with the Theme header plus the CSS from this repo
3. Add a blank `functions.php` file
4. Zip the folder
5. In WordPress: **Appearance → Themes → Add New → Upload Theme**
6. Upload the zip → Install → Activate

### Step 11: Kadence Theme Settings
1. Go to **Appearance → Customize**
2. **Header:** Enable sticky header, add business name left, add phone button right
3. **Colors:** Set primary color to `#1C1C1C`
4. **Typography:** Set body font size to 17px, line-height to 1.65
5. **Buttons:** Set background to `#1C1C1C`, text to `#FFFFFF`
6. Click **"Publish"** when done

---

## PART 4 — PLUGIN INSTALLATION

Install all plugins from `plugins/plugin-list.txt`. For each plugin:
1. Go to **Plugins → Add New**
2. Search for the plugin name
3. Click **"Install Now"** → **"Activate"**

### Order of Installation:
1. **Kadence Blocks** — install first, needed for page layouts
2. **WPForms Lite** — install and set up the quote form before building pages
3. **Yoast SEO** — install and run setup wizard (see below)
4. **WP Super Cache** — install and enable caching (see below)
5. **Insert Headers and Footers** — install and add schemas (see below)

### WPForms Lite Setup
1. After activation, go to **WPForms → Add New**
2. Select **"Simple Contact Form"** template
3. Rename it: **"Free Quote Request"**
4. **Edit fields:**
   - Keep Name field — rename label to "Full Name"
   - Keep Email field
   - Add Phone field: click "+" → "Phone" — mark as Required
   - Add Paragraph Text field — label: "Tell us about your project" — mark Required
5. **Settings → Notifications:**
   - Update "Send To Email Address" to your actual business email (not the placeholder)
   - Update email subject: "New Quote Request from [business name field]"
6. **Settings → Confirmations:**
   - Set confirmation message to: "Thanks! We'll be in touch within 1 business day."
7. Click **"Save"**
8. Note the Form ID number — you'll need it to embed the form on pages

### Yoast SEO Setup
1. After activation, click **"Start first-time configuration"**
2. **Site type:** Select "Junk removal / Local service business"
3. **Organization details:** Enter Anderson Junk Removal Pros, your phone, and logo
4. **Social profiles:** Add any social profiles (skip if none yet)
5. **Search console:** Connect Google Search Console (requires a Google account)
   - If you haven't set up Search Console yet, do it at search.google.com/search-console
   - Add your property (domain) and verify via the HTML tag method Yoast provides
6. Complete the wizard

**After wizard — configure per-page SEO:**
- On each page/post, scroll to the Yoast panel → "Edit snippet" → enter meta title and description from `seo/meta-tags.md`

**Enable XML Sitemap:**
1. In Yoast SEO → Settings → General → Features tab
2. Ensure "XML sitemaps" toggle is ON
3. Your sitemap will be at: `https://yourdomain.com/sitemap_index.xml`
4. Submit this URL in Google Search Console → Sitemaps

### WP Super Cache Setup
1. After activation, go to **Settings → WP Super Cache**
2. On the **Easy** tab:
   - Click **"Enable Caching"**
   - Click **"Update Status"**
3. On the **Advanced** tab (optional but helpful):
   - Enable "Compress pages so they're served more quickly to visitors"
   - Enable "Don't cache pages for known users"
4. Click "Update Status"

### Insert Headers and Footers Setup
1. After activation, go to **Settings → Insert Headers and Footers**
2. **"Scripts in Header"** box — paste the following (each as a separate `<script>` block):
   - CallRail tracking script (get this from your CallRail account after setup)
   - Local Business JSON-LD schema from `seo/schema.json`
   - FAQ Page JSON-LD schema from `seo/schema.json`
3. Click **"Save"**

---

## PART 5 — CREATING PAGES IN WORDPRESS

### Create Pages in this Order:

**Homepage**
- Title: `Junk Removal Near Me | Anderson, SC`
- Slug: leave blank (will be homepage)
- Content from: `content/homepage.md`
- Use Kadence Blocks for layout (columns, buttons, accordion)

**Service Pages** (create one per service):
- Furniture Removal → slug: `furniture-removal-anderson`
- Appliance Removal → slug: `appliance-removal-anderson`
- Yard Waste Removal → slug: `yard-waste-removal-anderson`
- Estate Cleanouts → slug: `estate-cleanouts-anderson`
- Construction Debris Removal → slug: `construction-debris-removal-anderson`
- Content from: corresponding files in `content/services/`

**Contact Page**
- Title: `Contact Us`
- Slug: `contact`
- Content from: `content/contact.md`

**Privacy Policy**
- Title: `Privacy Policy`
- Slug: `privacy-policy`
- WordPress has a default Privacy Policy page template — use Settings → Privacy to set it up

**Blog Posts** (create in Posts, not Pages):
- Create 3 posts from `content/blog/`
- Set categories to "Blog" or "Tips"
- Set slugs to match the filenames (without .md)

### Using Kadence Blocks for Layout

**For the hero section with form:**
1. Add a Kadence Row block
2. Set to 2 columns (70/30 split on desktop)
3. Left column: hero headline, subheadline, CTA button
4. Right column: WPForms shortcode `[wpforms id="FORM_ID"]`
5. Set row background to your hero image

**For the FAQ section:**
1. Add a Kadence Accordion block
2. Add one accordion item per FAQ
3. Set the question as the panel title
4. Add the answer as the panel content

**For service cards:**
1. Add a Kadence Row block set to 3 columns
2. In each column, add a Kadence Info Box block
3. Set icon, title (H3), description, and link button

---

## PART 6 — SPEED OPTIMIZATION

### WordPress-Level
1. **WP Super Cache:** Confirm caching is enabled (see above)
2. **Yoast XML Sitemap:** Confirm it's enabled (see above)
3. **Kadence theme:** Go to Appearance → Customize → Performance → disable any unused scripts

### Hostinger-Level
1. In hPanel, look for **"LiteSpeed Cache"** or **"Speed"** settings
2. If LiteSpeed Cache is available (Hostinger Business and above), enable it
3. Enable **Gzip/Brotli compression** if available in hPanel → Advanced → PHP Configuration

### Image Optimization
1. Before uploading any photo, compress it at **squoosh.app** (free)
2. Target file sizes:
   - Hero background image: under 200KB
   - Service card icons/images: under 50KB each
   - Blog post images: under 100KB
3. Use WebP format where possible (modern browsers support it, Hostinger does too)
4. In WordPress, add alt text to every image for accessibility and SEO

### Performance Testing
- Test your site at: **pagespeed.web.dev**
- Target scores: **85+ mobile, 90+ desktop**
- If scores are low, the most common fixes are:
  1. Image sizes too large — re-compress and re-upload
  2. Too many plugins — deactivate any you're not using
  3. Render-blocking scripts — use WP Super Cache's "CDN" or defer JS settings

---

## PART 7 — ADDING SCHEMA MARKUP

### Local Business Schema
1. Open `seo/schema.json` in this repository
2. Copy the LocalBusiness JSON object
3. Paste into this template and add to Insert Headers and Footers:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Anderson Junk Removal Pros",
  "description": "Professional junk removal serving Anderson, SC and surrounding areas.",
  "telephone": "CALLRAIL_PLACEHOLDER",
  "url": "https://www.YOUR-DOMAIN-PLACEHOLDER.com",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Anderson",
    "addressRegion": "SC",
    "addressCountry": "US"
  },
  "areaServed": ["Anderson", "Clemson", "Seneca", "Easley", "Belton", "Honea Path", "Williamston", "Pendleton", "Iva", "Walhalla"],
  "serviceType": "Junk Removal",
  "priceRange": "$$",
  "openingHours": "Mo-Sa 07:00-19:00"
}
</script>
```

### FAQ Schema
Add a second `<script type="application/ld+json">` block with the FAQPage schema from `seo/schema.json`. Both schemas can live in the same "Scripts in Header" field in Insert Headers and Footers.

### Validate Your Schema
After adding, validate at: **search.google.com/test/rich-results**
- Paste your homepage URL and click "Test URL"
- Confirm no errors appear in the LocalBusiness or FAQPage rich results

---

## PART 8 — FINAL CONFIGURATION CHECKLIST

Before considering the WordPress setup complete:

- [ ] SSL enabled and site loads on HTTPS
- [ ] Permalink structure set to Post name
- [ ] Homepage set as static front page in Settings → Reading
- [ ] All 5 service pages created with correct slugs
- [ ] Contact page created at `/contact/`
- [ ] 3 blog posts published at correct URLs
- [ ] WPForms quote form embedded on homepage and contact page
- [ ] WPForms notification email updated to real business email
- [ ] Yoast meta title and description entered for every page and post
- [ ] Yoast focus keyphrase set per `seo/keyword-targets.md`
- [ ] XML sitemap enabled in Yoast
- [ ] Sitemap submitted to Google Search Console
- [ ] Local Business schema added via Insert Headers and Footers
- [ ] FAQ schema added via Insert Headers and Footers
- [ ] Schema validated at search.google.com/test/rich-results
- [ ] WP Super Cache enabled
- [ ] All images compressed before upload
- [ ] Custom CSS from `theme-customizations/kadence-child/style.css` added
- [ ] CALLRAIL_PLACEHOLDER replaced everywhere (see `callrail-setup.md`)
- [ ] Site tested on mobile device
- [ ] PageSpeed score 85+ mobile
