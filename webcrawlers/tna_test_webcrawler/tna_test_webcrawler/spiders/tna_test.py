# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_test_webcrawler.items import TnaTestWebcrawlerItem, starturls, allowurls, denyurls
from tna_test_webcrawler.helpers import parse_description, parse_keywords
from scrapy.loader import ItemLoader


# spider class for crawling
class TnaWebsiteWebCrawler(CrawlSpider):
    name = 'tna_website_films'
    allowed_domains = ['www.nationalarchives.gov.uk']
    start_urls = starturls
    # scraping rules: allowed urls, deny urls, follow links
    rules = [Rule(LinkExtractor(allow=allowurls, deny=denyurls), 'parse_item', follow=True)]

    # main function to parse craped data to defined items
    def parse_item(self, response):
        # define item loader to load scraped data to items
        il = ItemLoader(item=TnaTestWebcrawlerItem(), response=response)

        # values to add to scraped items
        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'FILMS')
        il.add_xpath('DATE_CREATED', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DCTERMS.modified"]/@content')
        il.add_xpath('COVERING_DATES', '//meta[@name="DC.coverage.temporal"]/@content')
        # call parsing helpers to add scraped items
        il.add_value('', parse_description(response))
        il.add_value('', parse_keywords(response))
        # load the item
        return il.load_item()