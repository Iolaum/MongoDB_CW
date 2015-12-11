# https://docs.python.org/2/library/csv.html#writer-objects
# python doc


import csv


def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for rowucr in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in rowucr]


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

# RESULT = ['apple','cherry','orange','pineapple','strawberry']
resultFile = open("output1.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')


with open('dataTest.csv', 'rbU') as f:
    # numlines = len(f.readlines())
    # print numlines # 19
    reader = csv.reader(f)
    # print type(reader)
    for row in reader:
        newLine = []
        for i in range(0, len(row)):
            # print (row[1])
            newLine.append(unicode_csv_reader(row[i]))
            # reader2 = unicode_csv_reader('dataTest.csv', csv.excel)
            wr.writerow(newLine)





# with open('some.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print row