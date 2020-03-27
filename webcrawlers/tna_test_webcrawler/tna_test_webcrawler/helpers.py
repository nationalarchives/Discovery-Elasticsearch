from tna_test_webcrawler.items import TnaTestWebcrawlerItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_keywords(response):
    il = ItemLoader(item=TnaTestWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="Keywords"]/@content')
    return il.load_item()


def parse_description(response):
    il = ItemLoader(item=TnaTestWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//p[contains(@class, "bodytext")]//text()')
    il.add_xpath('DESCRIPTION', '//span[contains(@class, "bodytext")]//a/text()')
    return il.load_item()