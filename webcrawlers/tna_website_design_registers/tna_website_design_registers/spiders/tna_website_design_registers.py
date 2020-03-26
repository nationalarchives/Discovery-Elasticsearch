# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_website_design_registers.items import TnaWebsiteItem, starturls, allowurls, denyurls
from tna_website_design_registers.helpers import parse_description, parse_keywords, parse_title
from scrapy.loader import ItemLoader


class TnaWebsiteWebCrawler(CrawlSpider):
    name = 'tna_website_design_registers'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = starturls
    rules = [Rule(LinkExtractor(allow=allowurls, deny=denyurls), 'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaWebsiteItem(), response=response)

        il.add_value('ID', response.url)
#        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'DESIGN REGISTERS')
        il.add_xpath('DATE_CREATED', '//meta[@name="DC.date.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DC.date.modified"]/@content')
        il.add_xpath('COVERING_DATES', '//meta[@name="DC.coverage.temporal"]/@content')
        il.add_value('', parse_description(response))
        il.add_value('', parse_keywords(response))
        il.add_value('', parse_title(response))

        return il.load_item()