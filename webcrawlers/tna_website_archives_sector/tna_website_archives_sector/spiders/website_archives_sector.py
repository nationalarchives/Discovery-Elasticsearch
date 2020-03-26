# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_website_archives_sector.items import TnaWebsiteItem, starturls, allowurls, denyurls
from tna_website_archives_sector.helpers import parse_content
from scrapy.loader import ItemLoader


class TnaWebsiteWebCrawler(CrawlSpider):
    name = 'tna_website_archives_sector'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = starturls
    rules = [Rule(LinkExtractor(allow=allowurls, deny=denyurls), 'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaWebsiteItem(), response=response)

        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_xpath('DSECRIPTION', '//meta[@property="og:description"]/@content')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'ARCHIVES SECTOR')
        il.add_xpath('DATE_CREATED', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DCTERMS.modified"]/@content')
        il.add_value('', parse_content(response))

        return il.load_item()