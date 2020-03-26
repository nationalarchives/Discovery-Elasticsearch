from tna_website_about.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_keywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="DC.subject.keyword"]/@content')
    return il.load_item()


def parse_content(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('CONTENT', '//div[contains(@class, "breather")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "breather")]/ul/li//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "breather")]/ol/li//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "entry-content")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "records-content")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@id, "news-content")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@id, "banner")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "col-md-8 col-md-pull-4")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "col-xs-12 col-sm-8 col-md-8")]/p//text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "margin-top-medium margin-bottom-medium")]/text()')
    return il.load_item()