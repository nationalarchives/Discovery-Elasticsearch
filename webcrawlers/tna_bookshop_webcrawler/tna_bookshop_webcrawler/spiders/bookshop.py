from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_bookshop_webcrawler.items import deny_urls
from tna_bookshop_webcrawler.helpers import *


class TnaBookshopWebCrawler(CrawlSpider):
    handle_httpstatus_list = [301, 403]
    name = 'tna_bookshop'
    allowed_domains = ['bookshop.nationalarchives.gov.uk']
    start_urls = ['https://bookshop.nationalarchives.gov.uk/']
    rules = [Rule(LinkExtractor(allow='bookshop', deny=deny_urls), 'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaBookshopWebcrawlerItem(), response=response)

        il.add_value('ID', response.url)
        il.add_value('', parse_title(response))
        il.add_value('SCHEMA', 'BOOKSHOP'),
        il.add_value('SOURCE', '700')
        il.add_value('', parse_description(response))
        il.add_value('', parse_keywords(response))
        return il.load_item()
