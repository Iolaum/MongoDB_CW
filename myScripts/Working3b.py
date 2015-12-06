# Learning from pymongo tutorials.
# Question 4: timedelta
#
# http://stackoverflow.com/questions/22219210/convert-the-unicode-to-datetime-format
# 5.12.2015

from pymongo import MongoClient
import pymongo
import datetime
import time


client = MongoClient('localhost', 27017)
print ("Connected.")  # make check for failure
dbc = client.mongo1.microblogging  # ...

# dbc.ensure_index([("reviewDate", pymongo.ASCENDING)])

# cursor = dbc.find().limit(2)
cursor = dbc.find().sort("timestamp", pymongo.ASCENDING).limit(12000)

date1 = 0
date2 = 0
dateDiff = 0
for i in cursor:
    # print type(i["timestamp"]) > is unicode
    # print i["timestamp"]
    timeStr = i["timestamp"]#.replace(' ', 'T')
    date2 = datetime.datetime.strptime(timeStr, '%Y-%m-%d %H:%M:%S')
    if date1 == 0:
        date1 = date2
    else:
        dateDiff = time.mktime(date2.timetuple()) - time.mktime(date1.timetuple())  # check units
        date1 = date2
print str(dateDiff)


client.close()
print "Disconnected."

# >>> import datetime
# >>> today = datetime.datetime.today()
# >>> yourdate = datetime.datetime.strptime(u'2014-03-06T04:38:51Z', '%Y-%m-%dT%H:%M:%SZ')
# >>> difference = today - yourdate
# print str(difference)






