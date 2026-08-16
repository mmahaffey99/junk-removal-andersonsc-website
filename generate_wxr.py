#!/usr/bin/env python3
"""Generates a WordPress WXR import file for Anderson Junk Removal Pros."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from wp_builder import (homepage_content, contact_content, privacy_content,
                         about_content, service_page,
                         clemson_page_content, easley_page_content, seneca_page_content,
                         blog_post_1, blog_post_2, blog_post_3,
                         blog_post_4, blog_post_5, blog_post_6, blog_post_7,
                         blog_post_8, blog_post_9, blog_post_10,
                         SERVICES)

def cdata(text):
    return f"<![CDATA[{text}]]>"

def postmeta(key, value):
    return f"""
        <wp:postmeta>
            <wp:meta_key>{cdata(key)}</wp:meta_key>
            <wp:meta_value>{cdata(value)}</wp:meta_value>
        </wp:postmeta>"""

def item(title, slug, content, post_type, seo_title, seo_desc, seo_kw,
         post_id, status="publish", category=None):
    cat_xml = ""
    if category:
        cat_xml = f'\n        <category domain="category" nicename="{category.lower()}"><![CDATA[{category}]]></category>'
    return f"""
    <item>
        <title>{cdata(title)}</title>
        <link>https://andersonjunkremovalpros.com/{slug}/</link>
        <pubDate>Sat, 24 May 2026 12:00:00 +0000</pubDate>
        <dc:creator>{cdata("mmahaffey99")}</dc:creator>
        <content:encoded>{cdata(content)}</content:encoded>
        <excerpt:encoded>{cdata("")}</excerpt:encoded>
        <wp:post_id>{post_id}</wp:post_id>
        <wp:post_date>{cdata("2026-05-24 12:00:00")}</wp:post_date>
        <wp:post_date_gmt>{cdata("2026-05-24 12:00:00")}</wp:post_date_gmt>
        <wp:post_modified>{cdata("2026-05-24 12:00:00")}</wp:post_modified>
        <wp:post_modified_gmt>{cdata("2026-05-24 12:00:00")}</wp:post_modified_gmt>
        <wp:comment_status>{cdata("closed")}</wp:comment_status>
        <wp:ping_status>{cdata("closed")}</wp:ping_status>
        <wp:post_name>{cdata(slug)}</wp:post_name>
        <wp:status>{cdata(status)}</wp:status>
        <wp:post_parent>0</wp:post_parent>
        <wp:menu_order>0</wp:menu_order>
        <wp:post_type>{cdata(post_type)}</wp:post_type>
        <wp:post_password>{cdata("")}</wp:post_password>
        <wp:is_sticky>0</wp:is_sticky>{cat_xml}{postmeta("_yoast_wpseo_title", seo_title)}{postmeta("_yoast_wpseo_metadesc", seo_desc)}{postmeta("_yoast_wpseo_focuskw", seo_kw)}
    </item>"""

def build_wxr():
    items = []
    pid = 10

    # Blog archive page
    pid += 1
    items.append(item(
        "Blog", "blog",
        "<!-- wp:paragraph -->\n<p>Junk removal tips and guides for Anderson, SC homeowners.</p>\n<!-- /wp:paragraph -->",
        "page", "Junk Removal Blog | Anderson Junk Removal Pros",
        "Tips, guides, and local information about junk removal in Anderson, SC.",
        "junk removal blog Anderson SC", pid
    ))

    # Homepage
    pid += 1
    items.append(item(
        "Junk Removal Near Me | Anderson, SC", "home",
        homepage_content(), "page",
        "Junk Removal Anderson SC | Anderson Junk Removal Pros",
        "Top-rated junk removal in Anderson, SC. Free estimates. Fast, same-day service. Call CALLRAIL_PLACEHOLDER or request a free quote online today.",
        "junk removal Anderson SC", pid
    ))

    # Service pages
    for slug, d in SERVICES.items():
        pid += 1
        content = service_page(
            d["h1"], d["service"], d["intro1"], d["intro2"],
            d["included"], d["why1"], d["why2"], d["why3"],
            d["process"], d["faqs"], d["cta_note"], slug
        )
        items.append(item(d["h1"], slug, content, "page",
                          d["seo_title"], d["seo_desc"], d["seo_kw"], pid))

    # About page
    pid += 1
    items.append(item(
        "About Anderson Junk Removal Pros", "about", about_content(), "page",
        "About Anderson Junk Removal Pros | Anderson, SC",
        "Anderson Junk Removal Pros is a local junk removal service in Anderson, SC. Licensed, insured, honest pricing. Serving Anderson County and Upstate SC.",
        "junk removal Anderson SC", pid
    ))

    # City pages — Tier 1
    pid += 1
    items.append(item(
        "Junk Removal in Clemson, SC", "junk-removal-clemson-sc", clemson_page_content(), "page",
        "Junk Removal Clemson SC | Anderson Junk Removal Pros",
        "Professional junk removal in Clemson, SC. Furniture, appliances, yard waste, and more. Serving Clemson and Lake Hartwell area. Free estimates. Call (843) 642-8417.",
        "junk removal Clemson SC", pid
    ))

    pid += 1
    items.append(item(
        "Junk Removal in Easley, SC", "junk-removal-easley-sc", easley_page_content(), "page",
        "Junk Removal Easley SC | Anderson Junk Removal Pros",
        "Professional junk removal in Easley, SC. Furniture, appliances, yard waste, estate cleanouts, and more. Serving Easley and Pickens County. Free estimates. Call (843) 642-8417.",
        "junk removal Easley SC", pid
    ))

    pid += 1
    items.append(item(
        "Junk Removal in Seneca, SC", "junk-removal-seneca-sc", seneca_page_content(), "page",
        "Junk Removal Seneca SC | Anderson Junk Removal Pros",
        "Professional junk removal in Seneca, SC. Serving Seneca, Lake Keowee, and western Oconee County. Furniture, appliances, yard waste. Free estimates. Call (843) 642-8417.",
        "junk removal Seneca SC", pid
    ))

    # Contact
    pid += 1
    items.append(item(
        "Contact Us", "contact", contact_content(), "page",
        "Contact Anderson Junk Removal Pros | Anderson, SC",
        "Get a free estimate for junk removal in Anderson, SC. Call (843) 642-8417 or fill out our quick form. We respond within 1 business day.",
        "junk removal Anderson SC contact", pid
    ))

    # Privacy Policy
    pid += 1
    items.append(item(
        "Privacy Policy", "privacy-policy", privacy_content(), "page",
        "Privacy Policy | Anderson Junk Removal Pros",
        "Privacy policy for Anderson Junk Removal Pros — Anderson, SC.",
        "privacy policy", pid
    ))

    # Blog post 1
    pid += 1
    items.append(item(
        "How Much Does Junk Removal Cost in Anderson, SC? (2024 Pricing Guide)",
        "junk-removal-cost-anderson-sc", blog_post_1(), "post",
        "Junk Removal Cost in Anderson, SC — 2024 Pricing Guide",
        "What does junk removal cost in Anderson, SC? Pricing ranges, cost factors, and how to avoid cheap quotes that backfire. Read now.",
        "junk removal cost Anderson SC", pid, category="Blog"
    ))

    # Blog post 2
    pid += 1
    items.append(item(
        "How Often Should You Get Junk Removal in Anderson, SC? A Homeowner's Guide",
        "how-often-junk-removal-anderson", blog_post_2(), "post",
        "How Often Should You Get Junk Removal in Anderson, SC?",
        "Not sure how often to schedule junk removal in Anderson, SC? This homeowner's guide covers timing, warning signs, and how to stay ahead of clutter.",
        "how often junk removal Anderson SC", pid, category="Blog"
    ))

    # Blog post 3
    pid += 1
    items.append(item(
        "Junk Removal in Anderson, SC: DIY vs. Hiring a Professional — What You Need to Know",
        "junk-removal-diy-vs-professional-anderson", blog_post_3(), "post",
        "DIY vs. Professional Junk Removal in Anderson, SC — What to Know",
        "Thinking about hauling junk yourself in Anderson, SC? Read this honest breakdown of DIY vs. hiring a professional before you decide.",
        "junk removal DIY vs professional Anderson SC", pid, category="Blog"
    ))

    # Blog post 4
    pid += 1
    items.append(item(
        "Where to Take Junk in Anderson County, SC (Your Disposal Options Explained)",
        "where-to-take-junk-anderson-county", blog_post_4(), "post",
        "Where to Take Junk in Anderson County, SC — Disposal Options",
        "Where do you take junk in Anderson County, SC? This guide covers the landfill, recycling, donation options, and when hiring a junk removal service makes sense.",
        "where to take junk Anderson County SC", pid, category="Blog"
    ))

    # Blog post 5
    pid += 1
    items.append(item(
        "How Often Should You Clean Out Your Garage in Anderson, SC?",
        "how-often-clean-garage-anderson", blog_post_5(), "post",
        "How Often Should You Clean Your Garage in Anderson, SC?",
        "How often should Anderson, SC homeowners clean out their garage? This guide covers timing, warning signs, and what to do with junk that won't fit in the trash.",
        "how often clean garage Anderson SC", pid, category="Blog"
    ))

    # Blog post 6
    pid += 1
    items.append(item(
        "Anderson County Bulk Trash Pickup vs. Junk Removal: What's the Difference?",
        "anderson-county-bulk-trash-vs-junk-removal", blog_post_6(), "post",
        "Anderson County Bulk Trash vs. Junk Removal — What's the Difference?",
        "What's the difference between Anderson County bulk trash pickup and hiring a junk removal service? This guide explains both so you can choose the right option.",
        "Anderson County bulk trash junk removal", pid, category="Blog"
    ))

    # Blog post 7
    pid += 1
    items.append(item(
        "How to Dispose of an Old Refrigerator in Anderson, SC",
        "how-to-dispose-old-refrigerator-anderson-sc", blog_post_7(), "post",
        "How to Dispose of an Old Refrigerator in Anderson, SC",
        "How do you get rid of an old refrigerator in Anderson, SC? This guide covers legal disposal options — county programs, utility rebates, and appliance removal.",
        "dispose old refrigerator Anderson SC", pid, category="Blog"
    ))

    # Blog post 8
    pid += 1
    items.append(item(
        "What to Do With Yard Debris After a Storm in Upstate SC",
        "yard-debris-after-storm-upstate-sc", blog_post_8(), "post",
        "Yard Debris After a Storm in Upstate SC — What to Do",
        "After a storm in Anderson or Upstate SC, what do you do with fallen limbs and debris? This guide covers safety, cleanup options, and when to call for haul-away.",
        "yard debris storm cleanup Upstate SC", pid, category="Blog"
    ))

    # Blog post 9
    pid += 1
    items.append(item(
        "Estate Cleanout Checklist for Anderson, SC Homeowners",
        "estate-cleanout-checklist-anderson-sc", blog_post_9(), "post",
        "Estate Cleanout Checklist for Anderson, SC Homeowners",
        "Planning an estate cleanout in Anderson, SC? This checklist covers what to do first, what to keep, what to donate, and how to handle the haul-away efficiently.",
        "estate cleanout checklist Anderson SC", pid, category="Blog"
    ))

    # Blog post 10
    pid += 1
    items.append(item(
        "Junk Removal vs. Dumpster Rental in Anderson, SC: Which One Is Right for You?",
        "junk-removal-vs-dumpster-rental-anderson", blog_post_10(), "post",
        "Junk Removal vs. Dumpster Rental in Anderson, SC — Which to Choose?",
        "Deciding between junk removal and dumpster rental in Anderson, SC? This honest comparison covers cost, convenience, timing, and which option fits your project.",
        "junk removal vs dumpster rental Anderson SC", pid, category="Blog"
    ))

    wxr = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
    xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
    xmlns:content="http://purl.org/rss/1.1/modules/content/"
    xmlns:wfw="http://wellformedweb.org/CommentAPI/"
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:wp="http://wordpress.org/export/1.2/"
>
<channel>
    <title>Anderson Junk Removal Pros</title>
    <link>https://andersonjunkremovalpros.com</link>
    <description>Trusted Junk Removal Experts Serving Anderson, SC and Surrounding Areas</description>
    <pubDate>Sat, 24 May 2026 12:00:00 +0000</pubDate>
    <language>en-US</language>
    <wp:wxr_version>1.2</wp:wxr_version>
    <wp:base_site_url>https://andersonjunkremovalpros.com</wp:base_site_url>
    <wp:base_blog_url>https://andersonjunkremovalpros.com</wp:base_blog_url>
    <wp:author>
        <wp:author_id>1</wp:author_id>
        <wp:author_login><![CDATA[mmahaffey99]]></wp:author_login>
        <wp:author_email><![CDATA[mmahaffey99@gmail.com]]></wp:author_email>
        <wp:author_display_name><![CDATA[mmahaffey99]]></wp:author_display_name>
        <wp:author_first_name><![CDATA[]]></wp:author_first_name>
        <wp:author_last_name><![CDATA[]]></wp:author_last_name>
    </wp:author>
    <wp:category>
        <wp:term_id>1</wp:term_id>
        <wp:category_nicename><![CDATA[blog]]></wp:category_nicename>
        <wp:category_parent><![CDATA[]]></wp:category_parent>
        <wp:cat_name><![CDATA[Blog]]></wp:cat_name>
    </wp:category>
{"".join(items)}
</channel>
</rss>"""
    return wxr

if __name__ == "__main__":
    print("Generating wordpress-import.xml ...")
    wxr = build_wxr()
    with open("wordpress-import.xml", "w", encoding="utf-8") as f:
        f.write(wxr)
    size = len(wxr) / 1024
    print(f"Done! wordpress-import.xml ({size:.0f} KB)")
    print("Upload this file at: WordPress Admin → Tools → Import → WordPress")
