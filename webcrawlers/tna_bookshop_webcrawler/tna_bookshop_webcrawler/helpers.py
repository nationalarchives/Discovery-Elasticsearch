from tna_bookshop_webcrawler.items import TnaBookshopWebcrawlerItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join
from w3lib.html import replace_escape_chars


def remove_string(text):
    text = text.strip('- The National Archives Shop')
    return text


def parse_title(response):
    il = ItemLoader(item=TnaBookshopWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars, remove_string)
    il.default_output_processor = Join()
    il.add_xpath('TITLE', '//title/text()')
    return il.load_item()


def parse_description(response):
    il = ItemLoader(item=TnaBookshopWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('DESCRIPTION', '//p[contains(@class, "text-product-desc")]//text()')
    return il.load_item()


def parse_keywords(response):
    il = ItemLoader(item=TnaBookshopWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('KEYWORDS', '//meta[@name="keywords"]/@content')
    return il.load_item()


''' not currently using categories or file type
def parse_type(response):
    il = ItemLoader(item=TnaBookshopWebcrawlerItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    il.add_xpath('type', '//meta[@http-equiv="content-type"]/@content')
    return il.load_item()

def parse_category(response):
    il = ItemLoader(item=BookshopItem(), response=response)
    il.default_input_processor = MapCompose(lambda v: v.split(), replace_escape_chars)
    il.default_output_processor = Join()
    if len(il.get_xpath('//meta[@property="article:section"]/@content')) > 0:
        il.add_xpath('category', '//meta[@property="article:section"]/@content')
    elif len(il.get_xpath('//meta[@name="TNAcategory"]/@content')) > 0:
        il.add_xpath('category', '//meta[@name="TNAcategory"]/@content')
    else:
        il.add_value('category',  'Unspecified')
    return il.load_item()'''


'''solr date parsers
def parse_modified(response):
    il = ItemLoader(item=BookshopItem(), response=response)
    if il.add_xpath('modified', '//meta[@property="article:modified_time"]/@content') is not None:
        il.add_xpath('modified', '//meta[@property="article:modified_time"]/@content')
    else:
        il.add_value('modified', '1900-01-01T00:00:00+00:00')
        il.replace_value('modified', datetime.datetime.strptime(il.get_collected_values('modified')[0],
                                                               "%Y-%m-%dT%H:%M:%S+00:00").strftime("%Y-%m-%dT%H:%M:%SZ"))
    return il.load_item()


def parse_sortdate(response):
    il = ItemLoader(item=BookshopItem(), response=response)
    if il.add_xpath('sortdate', '//meta[@property="article:modified_time"]/@content') is not None:
        il.add_xpath('sortdate', '//meta[@property="article:modified_timed"]/@content')
    else:
        il.add_value('sortdate', '1900-01-01T00:00:00+00:00')
        il.replace_value('sortdate', datetime.datetime.strptime(il.get_collected_values('sortdate')[0],
                                                               "%Y-%m-%dT%H:%M:%S+00:00").strftime("%Y%m%d"))
    return il.load_item()'''
