"""
Question 3:
What was the earliest and latest date (YYYY-MM-DD HH:MM:SS) that a message was
published?

"""

from pymongo import MongoClient
import pymongo


client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")


dbc = client.mongo1.microblogging  # ...

cursor = dbc.find().sort("timestamp", pymongo.ASCENDING).limit(1)

for latDate in cursor:
    print(latDate)
    print (type(latDate["timestamp"]))

cursor2 = dbc.find().sort("timestamp", pymongo.DESCENDING).limit(1)
for earDate in cursor2:
    print(earDate)

client.close()
print "Disconnected."


# "2014-06-22 23:00:00"
# "2014-06-30 21:59:59"
# Lucky result because timestamp is unicode string object !!









