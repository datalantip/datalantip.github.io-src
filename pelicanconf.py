#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

AUTHOR = 'faris priadi'
SITENAME = 'aladeve'
SITESUBTITLE = "narasi dan data visualization"
SITEURL = "" #"https://datalantip.github.io" # leave it blank when in localhost

PATH = "content"

# Regional Settings
TIMEZONE = "Asia/Jakarta"
DATE_FORMATS = {"en": "%b %d, %Y"}

# Plugins and extensions
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.admonition": {},
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {"permalink": " "},
    }
}




PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "extract_toc",
    "liquid_tags.img",
    "liquid_tags.include_code",
    "neighbors",
    "related_posts",
    "render_math",
    "series",
    "share_post",
    "tipue_search",
]
SITEMAP = {
    "format": "xml",
    "priorities": {"articles": 0.5, "indexes": 0.5, "pages": 0.5},
    "changefreqs": {"articles": "monthly", "indexes": "daily", "pages": "monthly"},
}

# Appearance
THEME = "themes/elegant"
TYPOGRIFY = True
DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = False

# Defaults
DEFAULT_CATEGORY = "Miscellaneous"
USE_FOLDER_AS_CATEGORY = False
ARTICLE_URL = "{slug}"
PAGE_URL = "{slug}"
PAGE_SAVE_AS = "{slug}.html"
TAGS_URL = "tags"
CATEGORIES_URL = "categories"
ARCHIVES_URL = "archives"
SEARCH_URL = "search"


# Feeds
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None


# Social
SOCIAL = (
    ("Twitter", "https://twitter.com/farispriadi", "Cuitan Faris"),
    ("Github", "https://github.com/farispriadi/", "Repo Faris"),
    ("linkedin", "https://www.linkedin.com/in/faris-priadi-9ba17245/", "Portfolio"),
    ("RSS", SITEURL + "/feeds/all.atom.xml"),
    
)



# Elegant theme
# STATIC_PATHS = ["theme/images", "images", "extra/_redirects", "code"]
# EXTRA_PATH_METADATA = {"extra/_redirects": {"path": "_redirects"}}

# if os.environ.get("CONTEXT") == "production":
#     STATIC_PATHS.append("extra/robots.txt")
#     EXTRA_PATH_METADATA["extra/robots.txt"] = {"path": "robots.txt"}
# else:
#     STATIC_PATHS.append("extra/robots_deny.txt")
#     EXTRA_PATH_METADATA["extra/robots_deny.txt"] = {"path": "robots.txt"}

DIRECT_TEMPLATES = ["index", "tags", "categories", "archives", "search", "404"]
TAG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
USE_SHORTCUT_ICONS = True

# Elegant Labels
SOCIAL_PROFILE_LABEL = "Stay in Touch"
RELATED_POSTS_LABEL = "Keep Reading"
SHARE_POST_INTRO = "Share :"
# COMMENTS_INTRO = "So what do you think? Did I miss something? Is any part unclear? Leave your comments below."

# Email Subscriptions
EMAIL_SUBSCRIPTION_LABEL = "Get New Release Alert"
EMAIL_FIELD_PLACEHOLDER = "Enter your email..."
SUBSCRIBE_BUTTON_TITLE = "Notify me"

FREELISTS_NAME = "oracle-l"
FREELISTS_FILTER = True

# SMO
TWITTER_USERNAME = "farispriadi"
# FEATURED_IMAGE = SITEURL + "/theme/images/apple-touch-icon-152x152.png"

# Legal
# SITE_LICENSE = """Content licensed under <a rel="license nofollow noopener noreferrer"
#     href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
#     Creative Commons Attribution 4.0 International License</a>."""
# HOSTED_ON = {"name": "Netlify", "url": "https://www.netlify.com/"}

LANDING_PAGE_TITLE = "Melihat Data Dengan Cerita"
SITE_DESCRIPTION = "tell your research story"
SITE_LOGO = "/theme/images/logo_text_h_white.png"
FEATURED_IMAGE = "/theme/images/banner.png"


DELETE_OUTPUT_DIRECTORY = True

# Share links at bottom of articles
# Supported: twitter, facebook, hacker-news, reddit, linkedin, email
SHARE_LINKS = [("twitter", "Twitter"), ("linkedin", "LinkedIn")]
# Landing Page
PROJECTS_TITLE = "Free & Open Source Apps"
PROJECTS = [{
    'name': 'WALeadApp',
    'url': 'https://github.com/farispriadi/WALeadApp',
    'description': 'Tool kirim pesan WhatsApp massal otomatis'},
    ]

AUTHORS = {
    "Faris Priadi": {
        "url": "https://www.linkedin.com/in/faris-priadi-9ba17245/",
        "blurb": "Python Programmer",
        "avatar": "/theme/images/avatars/avatar.png",
    },
}
DISQUS_FILTER = True
UTTERANCES_FILTER = True
COMMENTBOX_FILTER = True


#SEO

# settings.py
SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = False  # To disable this feature
SEO_ENHANCER_OPEN_GRAPH = False # The default value for this feature
SEO_ENHANCER_TWITTER_CARDS = False # The default value for this feature