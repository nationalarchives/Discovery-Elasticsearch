# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field


class TnaWebsiteItem(Field):
    ID = Field()
    TITLE = Field()
    DESCRIPTION = Field()
    SOURCE = Field()
    SUBJECTS = Field()
    KEYWORDS = Field()
    DATE_CREATED = Field()
    DATE_MODIFIED = Field()
    SCHEMA = Field()
    pass


starturls = ['https://www.nationalarchives.gov.uk/education/']

denyurls = ['/atoz/',
            '/webarchive.nationalarchives.gov.uk/',
            '/discovery.nationalarchives.gov.uk/',
            '/media.nationalarchives.gov.uk/',
            '/blog.nationalarchives.gov.uk/',
            '/bookshop.nationalarchives.gov.uk/',
            '/images.nationalarchives.gov.uk/',
            '/academic',
            '/accessions/accprograms/',
            '/activity*',
            '/assetbank-nationalarchives/',
            '/advanceorders',
            '/advanceorders/includes/',
            '/advanceorders/js/',
            '/archives/',
            '/archon/',
            '/bookshop/',
            '/bookshop/account.aspx',
            '/bookshop/App_Code/',
            '/bookshop/basket.aspx',
            '/bookshop/Bin/',
            '/bookshop/Controls/',
            '/bookshop/coupn.aspx',
            '/bookshop/digital_receipt.aspx',
            '/bookshop/ordercomplete.aspx',
            '/bookshop/process_order.aspx',
            '/bookshop/receiptfailure.aspx',
            '/bookshop/searchresult.aspx',
            '/bookshop/titleshow.asp',
            '/bookshop/xml/',
            '/browse-guidance-standards/',
            '/Bridging',
            '/business',
            '/cab/',
            '/cabinetpapers',
            '/cabinetpaperssearch',
            '/catalogue',
            '/celebratingcensus',
            '/census',
            '/chat',
            '/clickandbuy',
            '/conferences/ ',
            '/conferencesclosed',
            '/contact/form/',
            '/cover-it-live/',
            '/credits',
            '/css',
            '/currency',
            '/customerrors/',
            '/dc-framework/',
            '/dc-guidance/',
            '/dc-riskassessment/',
            '/dc-service/',
            '/dc-training/',
            '/digexpress',
            '/digitalcontinuity',
            '/digitalexpress/',
            '/discovery',
            '/document_handling',
            '/documentsonline',
            '/documentphotos/',
            '/documents/mog.pdf',
            '/documents/old/',
            '/documents/',
            '/dol',
            '/Download.aspx',
            '/droid/',
            '/e179/includes/',
            '/e179/scripts/',
            '/ecards',
            '/educationservice',
            '/edwardii-conference',
            '/emergency.htm',
            '/enewsletter',
            '/enewsletter/global/',
            '/enewsletter/includes/',
            '/equity',
            '/equity/includes/',
            '/equity/scripts/',
            '/ERO/*',
            '/eventsbooking',
            '/eventsbooking/email_templates/',
            '/eventsbooking/includes/',
            '/eventsbooking/scripts/',
            '/failover',
            '/Filestore/',
            '/filmindex.htm',
            '/foi/pubscheme/',
            '/galleries/',
            '/gazettestender',
            '/gettingstarted',
            '/gwdb',
            '/help/',
            '/help-with-your-research/',
            '/hospitalrecords/includes/',
            '/househistory',
            '/ia/',
            '/ichora5',
            '/images/',
            '/imagelibrary',
            '/information-principles',
            '/includes/',
            '/irlist/includes/',
            '/labs-maintenance.htm',
            '/legion',
            '/livingin1901',
            '/livingthepoorlife',
            '/localhistory',
            '/media',
            '/militaryhistory',
            '/museum',
            '/museum/includes/',
            '/mypage',
            '/news/999-snow.htm',
            '/online/includes',
            '/PageNotFound/',
            '/pas-198',
            '/place-of-deposit.php?',
            '/podcasts',
            '/poor_law',
            '/popup/',
            '/portal',
            '/preservation',
            '/presspreview/',
            '/pronom',
            '/pronom/product/',
            '/pronom/vendor/',
            '/recordpreviews/',
            '/recordsmanagement',
            '/records/',
            '/registration',
            '/registration/includes/',
            '/registration/js/',
            '/religiousarchives',
            '/research-guides/',
            '/results.php?',
            '/rss',
            '.rtf',
            '/script/',
            '/search/',
            '/Search/',
            '/search/name_search.aspx',
            '/searchthearchives',
            '/sepia/images',
            '/SFACS',
            '/source-1a/',
            '/source-1b/',
            '/source-1c/',
            '/source-1d/',
            '/spanish-civil-war',
            '/streamline',
            '/swf',
            '/TNACRL',
            '/towton',
            '/transfer',
            '/video',
            '/wdytya',
            'wrong*',
            '/xml',
            '/yourarchives',
            '/zoomify',
            'zoomifyImagePath',
            '/zzz/']

allowurls = ['/education/']
