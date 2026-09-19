AUTHOR = "L'Équipe"
SITENAME = "Outils Business & Créateurs"
SITESUBTITLE = "Les meilleurs logiciels SaaS B2B pour les pros"
SITELOGO = "https://cdn-icons-png.flaticon.com/512/2953/2953423.png" # Icône business libre de droits
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Theme settings
THEME = 'themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll (Liens de la barre latérale)
LINKS = (('Outils IA', 'https://M0ebius0ne.github.io/outils-ia/'),)

# Social widget
SOCIAL = ()

# SEO Clean URLs
ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
