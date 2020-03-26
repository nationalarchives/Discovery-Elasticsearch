from tna_website_accessions.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_title(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('TITLE', '//h1[contains(@class, "parchment")]//text()')
    return il.load_item()


def parse_keywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//td[contains(@class, "tabbody")]//ul/li/a/text()')
    return il.load_item()


def parse_corporate_bodies(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('CORPORATE_BODIES', '//a[contains(@class, "bigblack")]//text()')
    il.add_xpath('CORPORATE_BODIES', '//p[contains(@class, "bodytext")]//a/text()')
    return il.load_item()


def parse_description(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//h1[contains(@class, "parchment")]//text()')
    il.add_xpath('DESCRIPTION', '//td[contains(@class, "tabbody")]//ul/li/text()')
    return il.load_item()
