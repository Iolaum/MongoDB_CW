# Learning from pymongo tutorials.
# http://api.mongodb.org/python/current/tutorial.html
# 5.12.2015

#

from pymongo import MongoClient
client = MongoClient('localhost', 27017)

print ("It works!")
# :)

# print client.database_names()  # python 2 print usage !
# it works and prints available databases :)

# print client.collection_names()

dbc = client.mongo1.microblogging  # ...

distinctUsersList = dbc.distinct("id_member")
print (len(distinctUsersList))
#results: #119231








