"""
Script to answer question 2:
How many tweets (%) did the top 10 users (measured by the number of messages) publish?

>> Done through aggregation pipeline !

https://docs.mongodb.org/manual/core/aggregation-pipeline/
and
https://docs.mongodb.org/manual/reference/operator/aggregation-pipeline/

########### Notes from documentation on how it works !! ###########

The aggregation pipeline is a framework for data aggregation modeled on the concept of data processing pipelines.
The aggregation pipeline provides an alternative to map-reduce and may be the preferred solution for aggregation tasks
where the complexity of map-reduce may be unwarranted. Aggregation pipeline have some limitations on value types and
result size.


pipeline stages :

$group:

Groups input documents by a specified identifier expression and applies the accumulator expression(s),
if specified, to each group. Consumes all input documents and outputs one document per each distinct group.
The output documents only contain the identifier field and, if specified, accumulated fields.

Groups documents by some specified expression and outputs to the next stage a document for each distinct grouping.
The output documents contain an _id field which contains the distinct group by key.
The output documents can also contain computed fields that hold the values of some accumulator expression grouped by
the $group's _id field. $group does not order its output documents. The $group stage has the following prototype form:

{ $group: { _id: <expression>, <field1>: { <accumulator1> : <expression1> }, ... } }

The _id field is mandatory; however, you can specify an _id value of null to calculate accumulated values for
all the input documents as a whole. The remaining computed fields are optional and computed using the <accumulator>
operators. The _id and the <accumulator> expressions can accept any valid expression.
For more information on expressions, see Expressions.

$count

Counts the number of documents in a collection. Returns a document that contains this count and as well as the command
status. count has the following form:

{ count: <collection>, query: <query>, limit: <limit>, skip: <skip>, hint: <hint> }

$sum

Calculates and returns the sum of numeric values. $sum ignores non-numeric values.

Changed in version 3.2: $sum is available in the $group and $project stages.
In previous versions of MongoDB, $sum is available in the $group stage only.

## I have version 3.0.7 of Mongodb at the time of this project.

$sort

Sorts all input documents and returns them to the pipeline in sorted order.
The $sort stage has the following prototype form:

{ $sort: { <field1>: <sort order>, <field2>: <sort order> ... } }

$limit
Limits the number of documents passed to the next stage in the pipeline.


"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
if client is None:
    print "Couldn't connect!"
else:
    print ("Connected.")



dbc = client.mongo1.microblogging  # ...
# Let's implement aggregate
query1 = dbc.aggregate([
    {"$group": {"_id": "$id_member", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])

tweetNumber = 0
for i in query1:
    tweetNumber += i['count']

print tweetNumber

#  tweetNumber = 32344
# total good = 1459434


client.close()
print "Disconnected."

