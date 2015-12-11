"""
Script to answer question 1:
How many unique users are there?
"""

from pymongo import MongoClient


client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")



# print client.database_names()  # python 2 print usage !
# it works and prints available databases :)

# print client.collection_names()

dbc = client.mongo1.microblogging  # ...

distinctUsersList = dbc.distinct("id_member")
print "Number of unique users is:"
print (len(distinctUsersList))
# results: #119218


client.close()
print "Disconnected."





