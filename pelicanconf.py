#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Isaac Skibinski'
SITENAME = 'Isaac Skibinski'
SITEURL = ''

THEME = 'themes/ppe'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ARTICLE_URL = '{slug}'
ARTICLE_SAVE_AS = '{slug}/index.html'

PLUGIN_PATHS = ['../../otherSrc/pelican-plugins', 'plugins']
PLUGINS = ['representative_image', 'advthumbnailer'] # 'clean_summary'

DISPLAY_CATEGORIES_ON_MENU = False

# It's a hack but I don't need a whole plugin for this:
from datetime import date
BUILD_DATE = date.today()