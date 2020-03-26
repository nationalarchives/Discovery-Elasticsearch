# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field


class TnaWebsiteItem(Field):
    ID = Field()
    TITLE = Field()
    CONTENT = Field()
    SOURCE = Field()
    SUBJECTS = Field()
    START_DATE = Field()
    END_DATE = Field()
    DATE_CREATED = Field()
    DATE_MODIFIED = Field()
    KEYWORDS = Field()
    SCHEMA = Field()
    pass

