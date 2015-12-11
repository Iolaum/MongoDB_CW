"""
Question 5:
What is the mean length of a message?
Question 7:
What is the average number of hashtags (#) used within a message?

"""
from pymongo import MongoClient
# import pymongo


client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")


dbc = client.mongo1.microblogging  # ...
cursor = dbc.find()#.limit(150000)


textLength = 0
hashtags = 0
notAString = 0
dummyVar = 0
badLength = 0
badhashtags = 0

for i in cursor:
    # print len(i["text"]), i["text"].count('#')
    if isinstance(i["text"], basestring):
        textLength += len(i["text"])
        hashtags += i["text"].count('#')
    else:
        # print i
        notAString += 1
        dummyVar = str(i["text"])
        badLength += len(dummyVar)
        badhashtags += dummyVar.count('#')

print textLength
print hashtags
print notAString
print badLength
print badhashtags
client.close()
print "Disconnected."

"""
Results (PreCleaning):
104222324
454972
45
162
0

"""









