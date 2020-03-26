from tna_website_information_management.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def getKeywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@property="article:tag"]/@content')
    return il.load_item()


def getDescription(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "breather")]/p//text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "breather")]/ul/li//text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@id, "col starts-at-full ends-at-two-thirds clr")]/p//text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@id, "col starts-at-full ends-at-half clr")]/p//text()')
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "col starts-at-full ends-at-half clr")]/p//text()')
    return il.load_item()