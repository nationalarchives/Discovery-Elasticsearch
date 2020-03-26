from tna_website_research_guides.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_description(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "breather")]/p/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "breather")]//ul/li/text()')
    il.add_xpath('DESCRIPTION', '//table[contains(@class, "table table-striped")]//tbody/tr/td/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "accordion-content")]//p/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "two-thirds pad-horizontal-large margin-none margin-bottom-large")]//p/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "video-box")]//p/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "entry-content")]//h3/text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "entry-content clearfix")]//p/text()')
    return il.load_item()


def parse_keywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    return il.load_item()