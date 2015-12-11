"""
Question 4:
What is the mean time delta between all messages?

"""
import datetime
import time

date1 = "2014-06-22 23:00:00"
date2 = "2014-06-30 21:59:59"
dateDiff = 0
tweetDiff = 0

date1 = datetime.datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
date2 = datetime.datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')
date1 = time.mktime(date1.timetuple())
date2 = time.mktime(date2.timetuple())

dateDiff = date2 - date1
print dateDiff
tweetDiff = dateDiff/1459433
print tweetDiff


# DateDiff = 687599
# tweetDiff = 0.471141189763






