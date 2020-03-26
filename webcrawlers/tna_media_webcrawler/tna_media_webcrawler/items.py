# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field


class TnaMediaWebcrawlerItem(Field):
    ID = Field()
    TITLE = Field()
    CONTENT = Field()
    DESCRIPTION = Field()
    START_DATE = Field()
    END_DATE = Field()
    SUBJECTS = Field()
    SOURCE = Field()
    SCHEMA = Field()
    pass
