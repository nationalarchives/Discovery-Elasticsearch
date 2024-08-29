import xlrd
import simplejson as json
import requests
from pymongo import MongoClient
import html.parser
import os.path
import sys
import re
import datetime

h = html.parser.HTMLParser()

# pymongo no longer supports multiple standalones, so each client has to be listed separately
client1 = MongoClient('mongodb://username:password@servername/?authSource=admin')
db1 = client1['iadata']
col1 = db1['Records']

# set url for search index api
url1 = 'http://wb-t-lobapp1.web.local/SearchIndexSvcWebApi/IndexDev/'


# set file path
xlsfile = '/home/pdavis/Documents/DiscoveryUpdates.xls'

# check if filepath exists and document is readable
if os.path.isfile(xlsfile) and os.access(xlsfile, os.R_OK):
    print("INFO: File exists and is being processed")
else:
    print("ERROR: File does not exist or is not readable")
    sys.exit(1)

# location of workbook
wb = xlrd.open_workbook(xlsfile)

# set worksheet from workbook
sh = wb.sheet_by_index(0)

# create empty lists for updates
ul1 = []

for rws in range(1, sh.nrows):
    # create empty dict to store all update values
    doc = {}
    # set spreadsheet data values
    row_values = sh.row_values(rws)
    # populate dict with spreadsheet data
    doc['IAID'] = row_values[0]
    if doc['IAID'] == "":
        del doc['IAID']

    doc['Ttl'] = html.unescape(row_values[1])
    if doc['Ttl'] == "":
        del doc['Ttl']

    doc['SC.Desc'] = html.unescape(row_values[2])
    if doc['SC.Desc'] == "":
        del doc['SC.Desc']

    doc['Note'] = html.unescape(row_values[3])
    if doc['Note'] == "":
        del doc['Note']

    doc['CovDts'] = row_values[4]
    if doc['CovDts'] == "":
        del doc['CovDts']

    doc['CFrmDt'] = row_values[5]
    if isinstance(doc['CFrmDt'], float):
        doc['CFrmDt'] = str(int(doc['CFrmDt']))
    if doc['CFrmDt'] == "":
        del doc['CFrmDt']

    doc['CToDt'] = row_values[6]
    if isinstance(doc['CToDt'], float):
        doc['CToDt'] = str(int(doc['CToDt']))
    if doc['CToDt'] == "":
        del doc['CToDt']

    doc['Clsr.CC'] = row_values[7]
    if isinstance(doc['Clsr.CC'], float):
        doc['Clsr.CC'] = str(int(doc['Clsr.CC']))
    if doc['Clsr.CC'] == "":
        del doc['Clsr.CC']

    doc['Clsr.RecOpenD'] = row_values[8]
    if isinstance(doc['Clsr.RecOpenD'], float):
        doc['Clsr.RecOpenD'] = xlrd.xldate_as_datetime(int(doc['Clsr.RecOpenD']), wb.datemode).strftime('%d/%m/%Y')
    if doc['Clsr.RecOpenD'] == "":
        del doc['Clsr.RecOpenD']

    print(doc)

    # append dict data to the update lists
    ul1.append(doc)
    # write data to json
    jd = json.dumps(doc)
#    print(doc)
# create empty lists for iaids
idl1 = []

# update mongodb collections
for doc in ul1:
    docRef = doc['IAID']
    rows = col1.find({'IAID': docRef})
    s1 = str(re.findall(r".*\(.*\(.*\((.*)", str(col1)))
    s2 = re.split(", ", s1)
    if rows.count() == 0:
        print('ERROR: ' + docRef + ' Does not exists in: ' + s2[0] + s2[4] + s2[5])
    else:
        col1.update_one({'IAID': doc['IAID']}, {'$set': doc})
        print('INFO: ' + docRef + ' has been updated in: ' + s2[0] + s2[4] + s2[5])

#        idl1.append(docRef)
# payload = ";".join(idl1)

# post iaids to search index api
# req1 = requests.post(url1, data=json.dumps(payload))
# print(req1)
# req2 = requests.post(url2, data=iaids2)%
# print 'IAIDS have been sent for indexing, please check index logs'
