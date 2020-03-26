# coding=utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_blog_webcrawler.helpers import *


class TnaBlogCrawl(CrawlSpider):
    name = 'tna_blog'
    allowed_domains = ['blog.nationalarchives.gov.uk']
    start_urls = ['https://blog.nationalarchives.gov.uk/']
    rules = [Rule(LinkExtractor(allow='/blog/', deny=['/tag/', '/author/', '/?replytocom=', '/photos/']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaBlogWebcrawlerItem(), response=response)

        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'BLOG')
        il.add_xpath('START_DATE', '//meta[@name="DCTERMS.created"]/@content')
        il.add_xpath('END_DATE', '/meta[@name="DCTERMS.modified"]/@content')
        il.add_value('', parse_subjects(response))
        il.add_value('', parse_description(response))
        return il.load_item()
