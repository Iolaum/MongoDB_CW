"""
Question 8:
Which area within the UK contains the largest number of published messages?
Hint, the geographic latitude and longitude coordinates can be aggregated.

"""

from pymongo import MongoClient
# import pymongo


client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")

dbc = client.mongo1.microblogging  # ...

# cursor = dbc.find().sort("geo_lat", pymongo.ASCENDING).limit(1)
# for item in cursor:
#     print item
#
# cursor = dbc.find().sort("geo_lat", pymongo.DESCENDING).limit(1)
# for item in cursor:
#     print item

# # geo-lat min: 49.423927 max: 59.31852 // 9.894593


# cursor = dbc.find().sort("geo_lng", pymongo.ASCENDING).limit(1)
# for item in cursor:
#     print item
#
# cursor = dbc.find().sort("geo_lng", pymongo.DESCENDING).limit(1)
# for item in cursor:
#     print item


# # geo-lng min: -7.633333 max: 1.860704 // 9.494037


#
# for i in cursor:
#     # print len(i["text"]), i["text"].count('#')
#     if isinstance(i["text"], basestring):
#         wordsList = i["text"].split()
#     else:
#         wordsList2 = str(i["text"]).split()
#

"""

49.4 59.4

-7.9 2.1

"""

client.close()
print "Disconnected."










