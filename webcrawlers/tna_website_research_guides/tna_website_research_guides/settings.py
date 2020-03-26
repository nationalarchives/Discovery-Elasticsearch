
BOT_NAME = 'tna_website_research_guides'

SPIDER_MODULES = ['tna_website_research_guides.spiders']
NEWSPIDER_MODULE = 'tna_website_research_guides.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'tna_website_research_guides (+http://www.nationalarchives.gov.uk)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEPTH_LIMIT = 100
DOWNLOAD_DELAY = .2

# LOG_LEVEL = 'INFO'
# LOG_FILE = 'tna_website_research_guides.log'

COOKIES_ENABLED = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False

# ITEM_PIPELINES = {'tna_website_research_guides.pipelines.MongoDBPipeline': 100}

ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100}

# ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100,
#                  'tna_website_research_guides.pipelines.MongoDBPipeline': 200}

"MONGODB PIPELINE SETTINGS"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = 'tna_webcrawlers'
MONGODB_COLLECTION = 'tna_website_research_guides'
MONGODB_UNIQ_KEY = 'ID'
MONGODB_ITEM_ID_FIELD = '_id'

"ELASTIC PIPELINE SETTINGS"
ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'discovery_website'
ELASTICSEARCH_TYPE = 'tnawebpageassetview'
ELASTICSEARCH_UNIQ_KEY = 'ID'


# ITEM_PIPELINES = ['scrapysolr.SolrPipeline']
# SOLR_URL = 'http://urlofyoursolrserver/solr'
# SOLR_MAPPING = {
#   'id': 'url',
#   'text': ['title', 'breadcrumbs', 'description'],
#   'description': 'description',
#   'keywords': 'breadcrumbs',
#   'price': 'price',
#   'title': 'title'
# }
# SOLR_IGNORE_DUPLICATES = True
# SOLR_DUPLICATES_KEY_FIELDS = ['id']
