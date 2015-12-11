"""
Question 8:
Which area within the UK contains the largest number of published messages?
Hint, the geographic latitude and longitude coordinates can be aggregated.

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



"""

We find the minimum and maximum geospatial variables by doing separate queries in the database.
To save time we hardcode them to our code.

49.4 59.4

-7.9 2.1

"""

mapper = Code("""
		function() {
			var ukLatMin = 49.4;
			var ukLngMin = -7.9;
			var gridLength = 1.0;

			var thisLng = parseFloat(this.geo_lng);
			var thisLat = parseFloat(this.geo_lat);
			var gridLoc;

			var interm = Math.floor((thisLat-ukLatMin)/gridLength);
			gridLoc = interm * 10;
			interm = Math.floor((thisLng-ukLngMin)/gridLength);
			gridLoc += interm;
			emit(gridLoc, 1);
		}
""")

reducer = Code("""
		function(key, value) {
			return Array.sum(value);
		}
""")

maxGrid = dbc.map_reduce(mapper, reducer, 'geoLocDistr')
topGrid = client.mongo1.geoLocDistr.find().sort('value', -1).limit(1)

for i in topGrid:
    print i


client.close()
print "Disconnected."


"""
Results:
27 with 323894 tweets!


Lat 51.4 -> 52.4 (51.9) // (LatMin = 2*1+ukLatMin)
Lng -0.9 -> -0.1 (-0.4) // (LngMin = 7*1+ukLngMin)
"""








