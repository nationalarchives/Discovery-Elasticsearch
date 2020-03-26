# -*- coding: utf-8 -*-
import pymongo
import logging
from scrapy.exceptions import DropItem
from scrapy.conf import settings


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db['tna_website_design_registers']

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem('missing data!')
            self.collection.update({'ID': item['ID']}, dict(item), upsert=True)
            logging.log(logging.INFO, 'Web Page inserted into db: %s' % item['ID'])
            return item['ID']