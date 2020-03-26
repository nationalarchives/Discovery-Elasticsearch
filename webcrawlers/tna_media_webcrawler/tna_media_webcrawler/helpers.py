from tna_media_webcrawler.items import TnaMediaWebcrawlerItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_description(response):
    il = ItemLoader(item=TnaMediaWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
#    il.add_xpath('DESCRIPTION', '//div[contains(@class, "entry-content clearfix")]/p//text()')
    il.add_xpath('DESCRIPTION', '//ul[contains(@id, "archive")]//p//text()')
    return il.load_item()


def parse_content(response):
    il = ItemLoader(item=TnaMediaWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('CONTENT', '//div[contains(@class, "transcription-content")]//p/text()')
    return il.load_item()


def parse_keywords(response):
    il = ItemLoader(item=TnaMediaWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    return il.load_item()


def parse_title(response):
    il = ItemLoader(item=TnaMediaWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('TITLE', '//title/text()')
    return il.load_item()
