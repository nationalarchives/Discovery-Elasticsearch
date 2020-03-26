# -*- coding: utf-8 -*-

# Scrapy settings for tna_website_cabinet_papers project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tna_website_cabinet_papers'

SPIDER_MODULES = ['tna_website_cabinet_papers.spiders']
NEWSPIDER_MODULE = 'tna_website_cabinet_papers.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'tna_website_cabinet_papers (+http://www.nationalarchives.gov.uk)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DEPTH_LIMIT = 100
DOWNLOAD_DELAY = .2

# LOG_LEVEL = 'INFO'
# LOG_FILE = 'tna_cabinetpapers_webcrawler.log'

COOKIES_ENABLED = False
RETRY_ENABLED = False

SPIDER_MIDDLEWARES = {'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 100}

# ITEM_PIPELINES = {'tna_website_cabinet_papers.pipelines.MongoDBPipeline': 100}

ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100}

# ITEM_PIPELINES = {'scrapyelasticsearch.scrapyelasticsearch.ElasticSearchPipeline': 100,
#                   'tna_website_cabinet_papers.pipelines.MongoDBPipeline': 200}

"MONGODB PIPELINE SETTINGS"
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = 'tna_webcrawlers'
MONGODB_COLLECTION = 'tna_website_cabinet_papers'
MONGODB_UNIQ_KEY = 'ID'
MONGODB_ITEM_ID_FIELD = '_id'

"ELASTIC PIPELINE SETTINGS"
ELASTICSEARCH_SERVERS = ['localhost']
ELASTICSEARCH_INDEX = 'discovery_website'
ELASTICSEARCH_TYPE = 'tnawebpageassetview'
ELASTICSEARCH_UNIQ_KEY = 'ID'
