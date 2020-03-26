# coding=utf-8
from tna_blog_webcrawler.items import TnaBlogWebcrawlerItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_description(response):
    il = ItemLoader(item=TnaBlogWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "entry-content clearfix")]/p//text()')
    return il.load_item()


def parse_subjects(response):
    il = ItemLoader(item=TnaBlogWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('SUBJECTS', '//meta[@name="keywords"]/@content')
    return il.load_item()
