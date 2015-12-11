"""
Question 6:
What are the 10 most common unigram and bigram strings within the messages?
"""

from pymongo import MongoClient
# import pymongo
from bson.code import Code


client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")

dbc = client.mongo1.microblogging  # ...

mapper = Code("""
		function() {
			var thisText = this.text;
			var splitStr = thisText.toString().split(" ");
			var gramList = [];

			for(i=0 ; i<splitStr.length ;i++){
				var clean1 = splitStr[i].replace(/[.,-\/#!$%\^&\*;:{}=\-_`~()]/g,"");
				var clean2 = clean1.replace(/\s{2,}/g," ");
				var cleanStr = clean2.trim();
				if (cleanStr.length >0)
				    gramList.push(cleanStr);
			}
			for (j=0 ; j < (gramList.length - 1) ;j++) {
			var bigram = gramList[j] + " " + gramList[j+1];
			// emit(bigram,1);
			}
		}
""")

reducer = Code("""
		function(key, value) {
			return Array.sum(value);
		}
""")

bigramCounter = dbc.map_reduce(mapper, reducer, 'bigrams')

cursor = client.mongo1.bigrams.find().sort('value', -1).limit(10)

for uni in cursor:
	print (uni)

client.close()
print "Disconnected."












