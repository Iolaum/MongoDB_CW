# http://stackoverflow.com/questions/19697846/python-csv-to-json


import csv
# import json
# import codecs

# http://stackoverflow.com/questions/6726953/open-the-file-in-universal-newline-mode-using-csv-module-django
# http://stackoverflow.com/questions/6916542/writing-list-of-strings-to-excel-csv-file-in-python

# https://docs.python.org/2/library/csv.html#writer-objects
# python doc

csvfile = open('data.csv', 'rU')
# jsonfile = open('data.json', 'w')

# Open File
resultFile = open("output.csv",'wb')

# id,id_member,timestamp,text,geo_lat,geo_lng
fieldnames = ("id","id_member","timestamp","text", "geo_lat", "geo_lng")
reader = csv.DictReader( csvfile, fieldnames, dialect=csv.excel_tab)
# counter = 0
for row in reader:
    # fill me


