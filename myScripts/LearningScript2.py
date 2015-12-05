
# http://altons.github.io/python/2013/01/21/gentle-introduction-to-mongodb-using-pymongo/
# 5.12.2015

import pymongo

# Connection to Mongo DB
try:
    conn = pymongo.MongoClient('localhost', 27017)
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
    print "Could not connect to MongoDB: %s" % e
conn

# Does not give error if it does not connect ...




