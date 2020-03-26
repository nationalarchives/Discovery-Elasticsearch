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
        self.collection = db['tna_media']

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem('Missing data!')
        self.collection.update({'ID': item['ID']}, dict(item), upsert=True)
        logging.log(logging.INFO, 'URL added to database: %s' % item['ID'])
        return item['ID']