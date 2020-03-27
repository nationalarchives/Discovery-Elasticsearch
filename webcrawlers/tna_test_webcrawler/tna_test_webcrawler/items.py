# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field


# define the fields for your webcrawler item:
class TnaTestWebcrawlerItem(Field):
    ID = Field()
    TITLE = Field()
    CONTENT = Field()
    DESCRIPTION = Field()
    DATE_MODIFIED = Field()
    DATE_CREATED = Field()
    COVERING_DATES = Field()
    SOURCE = Field()
    SUBJECTS = Field()
    KEYWORDS = Field()
    SCHEMA = Field()
    pass


# where the spider starts its crawl
starturls = ['https://www.nationalarchives.gov.uk/films/']
# allowed urls to be crawled
allowurls = ['/films/']
# urls that cannot be crawled
denyurls = ['/atoz/',
            '/webarchive.nationalarchives.gov.uk/',
            '/discovery.nationalarchives.gov.uk/',
            '/media.nationalarchives.gov.uk/',
            '/blog.nationalarchives.gov.uk/',
            '/bookshop.nationalarchives.gov.uk/',
            '/images.nationalarchives.gov.uk/',
            '/academic',
            '/accessions/accprograms/',
            '/assetbank-nationalarchives/',
            '/advanceorders',
            '/advanceorders/includes/',
            '/advanceorders/js/',
            '/archives/']