from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from tna_website_cabinet_papers.helpers import *


class TnaCabinetPapersWebcrawler(CrawlSpider):
    name = 'tna_website_cabinet_papers'
#    handle_httpstatus_list = [404]
    allowed_domains = ['nationalarchives.gov.uk']
    start_urls = ['https://www.nationalarchives.gov.uk/cabinetpapers/alevelstudies/the-general-strike.htm']
    rules = [Rule(LinkExtractor(allow=['/cabinetpapers/', '/alevelstudies/', '/themes/', '/cabinet-gov/'],
                                deny=['/cabinetpaperssearch/', 'WT.ac=', '/general-strike-interactive', '/details/',
                                      '/webarchive.nationalarchives.gov.uk/', '/sitemap.htm', '/documentsonline',
                                      '/help/', '/default.htm', '/use-the-wiring-frame.htm', '/maps-interactive',
                                      '/glossary.htm', '/writing-frame-help.htm', '/welfare-state-interactive/']),
                  'parse_item', follow=True)]

    def parse_item(self, response):
        il = ItemLoader(item=TnaWebsiteItem(), response=response)

        il.add_value('ID', response.url)
        il.add_xpath('TITLE', '//title/text()')
        il.add_xpath('DESCRIPTION', '//meta[@name="description"]/@content')
        il.add_value('SOURCE', '700')
        il.add_value('SCHEMA', 'CABINET PAPERS')
        il.add_xpath('START_DATE', '//meta[@name="DC.coverage.temporal.startdate"]/@content')
        il.add_xpath('END_DATE', '//meta[@name="DC.coverage.temporal.enddate"]/@content')
        il.add_xpath('DATE_CREATED', '//meta[@name="DC.date.created"]/@content')
        il.add_xpath('DATE_MODIFIED', '//meta[@name="DC.date.modified"]/@content')
        il.add_xpath('COVERING_DATES', '//meta[@name="DC.coverage.temporal"]/@content')
        il.add_xpath('PLACE_NAME', '//meta[@name="DC.coverage.spacial"]/@content')
        il.add_xpath('PERSON_FULL_NAME', '//meta[@name="DC.coverage.person"]/@content')
        il.add_value('', parse_content(response))
        il.add_value('', parse_keywords(response))

        return il.load_item()