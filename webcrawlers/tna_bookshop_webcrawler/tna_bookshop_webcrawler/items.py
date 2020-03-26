# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field


class TnaBookshopWebcrawlerItem(Field):
    ID = Field()
    TITLE = Field()
    CONTENT = Field()
    SOURCE = Field()
    SUBJECTS = Field()
    KEYWORDS = Field()
    START_DATE = Field()
    END_DATE = Field()
    AUTHOR = Field()
    pass


deny_urls = ['/FAQ/',
             '/Postage-Rates/',
             '/Reserve-and-Collect/',
             '/Returns-Policy/',
             '/about-us/',
             '/contact-us/',
             '/store/',
             '/voucher/',
             '/product/',
             '/Wish-List/',
             '/1/',
             '/2/',
             '/3/',
             '/4/',
             '/5/',
             '/6/',
             '/7/',
             '/8/',
             '/9/',
             '/10/',
             '/11/',
             '/12/',
             '/13/',
             '/British-history/',
             '/Crime-and-policing/',
             '/Family-history/',
             '/Books-for-Children/',
             '/Gifts-and-stationery/',
             '/Local-history/',
             '/Military-history/',
             '/Transport/',
             '/Womens%27-history/',
             '/Women%27-history/',
             '/Women%27s-history/',
             '/archives-and-records/',
             '/Archives-and-records/',
             '/Historical-Fiction/',
             '/Bargains-and-special-offers/',
             '/Books-from-The-National-Archiv/',
             '/Christmas-Gift-Ideas/',
             '/Christmas-gift-ideas/',
             '/Christmas-Offers/',
             '/Gifts-and-humour/',
             '/Inspired-by-our-collection/',
             '/Summer-Spectacular-Savings/',
             '/theme/',
             '/WHITEQUEENSET/',
             '/SERVANTSSET/',
             '/WIPERSSET/',
             '/The-Family-Project/',
             '/WomeninWar-Bundle/',
             '/Gifts-and-Humour/',
             '/Bargains-and-offers/',
             '/The-Map-Room/',
             '/Gifts-%26-Stationery/',
             '/Replica-documents-%26-medals/',
             '/Landscape-%26-Identity/',
             '/London%27s-history/']
