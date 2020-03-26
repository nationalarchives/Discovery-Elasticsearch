from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_media_webcrawler.helpers import *


class TNAMediaCrawl(CrawlSpider):
    name = 'tna_media'
    allowed_domains = ['media.nationalarchives.gov.uk']
    start_urls = ['https://media.nationalarchives.gov.uk/']
    rules = [
        Rule(LinkExtractor(allow='media', deny=['comment', '/page/', '/tag/', '/author']), 'parse_item',
             follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaMediaWebcrawlerItem(), response=response)

        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//h1[contains(@class, "separator-heading")]//text()')
#        il.add_xpath('TITLE', parse_title(response))
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'MEDIA')
        il.add_value('', parse_content(response))
        il.add_value('', parse_keywords(response))
        il.add_value('', parse_description(response))

        return il.load_item()
