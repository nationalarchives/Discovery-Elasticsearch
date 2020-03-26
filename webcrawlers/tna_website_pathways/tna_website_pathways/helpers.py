from tna_website_pathways.items import TnaWebsiteItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def getKeywords(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    il.add_xpath('KEYWORDS', '//meta[@name="KEYWORDS"]/@content')
    il.add_xpath('KEYWORDS', '//meta[@name="subject"]/@content')
    il.add_xpath('KEYWORDS', '//meta[@name="subjects"]/@content')
    il.add_xpath('KEYWORDS', '//meta[@name="title"]/@content')
    il.add_xpath('KEYWORDS', '//td/h4/text()')
    return il.load_item()


def getDescription(response):
    il = ItemLoader(item=TnaWebsiteItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    '''All'''
    il.add_xpath('DESCRIPTION', '//p/text()')
    il.add_xpath('DESCRIPTION', '//td/text()')
    '''census'''
    il.add_xpath('DESCRIPTION', '//div[contains(@class, "caption")]/text()')
    '''blackhistory'''
    il.add_xpath('DESCRIPTION', '//td/a/text()')
    '''citizenship'''
    il.add_xpath('DESCRIPTION', '//p/font/text()')
    '''first-world-war'''
    il.add_xpath('DESCRIPTION', '//td/p/text()')
    il.add_xpath('DESCRIPTION', '//th/h4/text()')
    il.add_xpath('DESCRIPTION', '//span[contains(@class, "maintext")]/text()')

    return il.load_item()
