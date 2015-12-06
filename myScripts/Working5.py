# Learning from pymongo tutorials.
# http://api.mongodb.org/python/current/tutorial.html
# 5.12.2015

#

from pymongo import MongoClient
import pymongo
client = MongoClient('localhost', 27017)

print ("Connected.")  # make check for failure

dbc = client.mongo1.microblogging  # ...

cursor = dbc.find().limit(15)

for i in cursor:
    # print len(i["text"]), i["text"].count('#')
    if isinstance(i["text"], basestring):
        wordsList = i["text"].split()
    else:
        wordsList2 = str(i["text"]).split()


client.close()
print "Disconnected."










