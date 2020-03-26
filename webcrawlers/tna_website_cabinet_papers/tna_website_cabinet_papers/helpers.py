from tna_website_cabinet_papers.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_content(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('CONTENT', '//div[contains(@class, "block-main")]//p/text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "block-main")]//h4//b/a/text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "accordion")]//p/text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "block-main")]//h2/text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "block-main")]//ul/li/a/text()')
    il.add_xpath('CONTENT', '//div[contains(@class, "block-main")]//ul/li/text()')
    il.add_xpath('CONTENT', '//h2[contains(@class, "subtheme")]/text()')
    return il.load_item()


def parse_keywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    il.add_xpath('KEYWORDS', '//meta[@name="DC.coverage.person"]/@content')
    return il.load_item()
