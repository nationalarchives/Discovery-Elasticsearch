# -*- coding: utf-8 -*-

# Scrapy settings for tna_blog_webcrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tna_blog_webcrawler'

SPIDER_MODULES = ['tna_blog_webcrawler.spiders']
NEWSPIDER_MODULE = 'tna_blog_webcrawler.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'tna_blog_webcrawler (+http://www.nationalarchives.gov.uk)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEPTH_LIMIT = 100
DOWNLOAD_DELAY = .2

# LOG_LEVEL = 'INFO'
# LOG_FILE = 'tna_blog_webcrawler.log'

COOKIES_ENABLED = False
RETRY_ENABLED = False
REDIRECT_ENABLED = False

# ITEM_PIPELINES = {'tna_blog_webcrawler.pipelines.MongoDBPipeline': 100}

ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100}

# ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100,
#                  'tna_blog_webcrawler.pipelines.MongoDBPipeline': 200}

"MONGODB PIPELINE SETTINGS"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = 'tna_webcrawlers'
MONGODB_COLLECTION = 'tna_blog'
MONGODB_UNIQ_KEY = 'ID'
MONGODB_ITEM_ID_FIELD = '_id'

"ELASTIC PIPELINE SETTINGS"
ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'discovery_website_dev'
ELASTICSEARCH_TYPE = 'tnawebpageassetview'
ELASTICSEARCH_UNIQ_KEY = 'ID'
