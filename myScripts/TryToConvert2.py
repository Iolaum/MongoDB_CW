# http://stackoverflow.com/questions/19697846/python-csv-to-json


import csv
import json

# https://docs.python.org/2/howto/unicode.html
import codecs

# http://stackoverflow.com/questions/6726953/open-the-file-in-universal-newline-mode-using-csv-module-django
csvfile = open('data.csv', 'rU')
jsonfile = open('data.json', 'w')

# id,id_member,timestamp,text,geo_lat,geo_lng
fieldnames = ("id","id_member","timestamp","text", "geo_lat", "geo_lng")
reader = csv.reader( csvfile, fieldnames)
counter = 0
for row in reader:
    # implement for loop for items in list !
    json.JSONDecoder(row).dump(row, jsonfile)
    jsonfile.write('\n')
jsonfile.write(out)


