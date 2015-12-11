# https://docs.python.org/2/library/csv.html#writer-objects
# python doc


import csv

# We check if Python can understand every CSV entry!


def notastring(s):
    if not isinstance(s, str):
        return 1
    return 0


with open('data.csv', 'rU') as f:
    reader = csv.reader(f)
    non1 = 0
    for row in reader:
        for i in range(0, len(row)):
            non1 += notastring(row[i])
    print non1

# result 0 - everything is a string - python should be able to read it!
