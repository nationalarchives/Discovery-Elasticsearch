# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_website_research_guides.helpers import *


class TnaWebsiteWebCrawler(CrawlSpider):
    handle_httpstatus_list = [301, 404]
    name = 'tna_website_research_guides'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = ['https://www.nationalarchives.gov.uk/help-with-your-research/']
    rules = [Rule(LinkExtractor(allow='/help-with-your-research/',
                                deny=['/atoz/', 'testlb', 'webarchive', 'letter=', '/research-guides-keywords/',
                                      '/cabinetpapers/', '/SearchUri/', 'research-category=', 'utm_campaign=']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaWebsiteItem(), response=response)
        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'RESEARCH GUIDES')
        il.add_xpath('DATE_CREATED', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DCTERMS.modified"]/@content')
        il.add_value('', parse_description(response))
        il.add_value('', parse_keywords(response))

        return il.load_item()
