# Learning from pymongo tutorials.
# http://api.mongodb.org/python/current/tutorial.html
# 5.12.2015

#

from pymongo import MongoClient
import pymongo
client = MongoClient('localhost', 27017)

print ("Connected.")  # make check for failure

dbc = client.mongo1.microblogging  # ...


# earDate = dbc.find().sort([    ("borough", pymongo.ASCENDING),    ("address.zipcode", pymongo.DESCENDING)])

cursor = dbc.find().sort("timestamp", pymongo.ASCENDING).limit(1)
for latDate in cursor:
    print(latDate)

cursor2 = dbc.find().sort("timestamp", pymongo.DESCENDING).limit(1)
for earDate in cursor2:
    print(earDate)

client.close()
print "Disconnected."










