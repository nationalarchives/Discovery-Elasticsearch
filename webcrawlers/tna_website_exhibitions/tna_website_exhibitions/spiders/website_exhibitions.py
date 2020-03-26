# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_website_exhibitions.items import TnaWebsiteItem, starturls, allowurls, denyurls
from tna_website_exhibitions.helpers import parse_description, parse_keywords
from scrapy.loader import ItemLoader


class TnaWebsiteWebCrawler(CrawlSpider):
    name = 'tna_website_exhibitions'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = starturls
    rules = [Rule(LinkExtractor(allow=allowurls, deny=denyurls), 'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaWebsiteItem(), response=response)

        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '700')
        il.add_xpath('DATE_CREATED', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DCTERMS.modified"]/@content')
        il.add_xpath('PLACE_NAME', '//div[contains(@class, "slider-city")]/text()')
        il.add_xpath('PLACE_COUNTRY', '//div[contains(@class, "slider-country")]/text()')
        il.add_xpath('CATALOGUE_REFERENCE', '//span[contains(@class, "catRef")]/text()')
        il.add_value('SCHEMA', 'EXHIBITIONS')
        il.add_value('', parse_description(response))
        il.add_value('', parse_keywords(response))
        return il.load_item()
