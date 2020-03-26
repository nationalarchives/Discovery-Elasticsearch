from tna_website_design_registers.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def parse_keywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    return il.load_item()


def parse_description(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//span[contains(@class, "btprojtxt")]/text()')
    il.add_xpath('DESCRIPTION', '//p[contains(@class, "btprojtxt")]/text()')
#    il.add_xpath('DESCRIPTION', '//a[contains(@class, "btprojlinks")]/text()')
#    il.add_xpath('DESCRIPTION', '//span[contains(@class, "btprojtoptitle")]/text()')
    return il.load_item()


def parse_title(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_value('TITLE', 'Design Registers ')
    il.add_xpath('TITLE', '//span[contains(@class, "btprojtoptitle")]/text()')
#    il.add_xpath('TITLE', '//span[contains(@class, "btprojtitle")]/text()')
    return il.load_item()


