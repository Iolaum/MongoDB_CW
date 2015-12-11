"""
    PreProcessing step 2:

    Entering all tweets that have complete syntax.
"""


import csv

inputFile = 'data.csv'
resultFile = open("output1.csv", 'wb+')
badFile = open("output2.csv", 'wb+')
wr1 = csv.writer(resultFile, dialect='excel')
wr2 = csv.writer(badFile, dialect='excel')
notId = 0


def cleanMemberId(s):
    # checks if we have less than 0 member id's and assigns them a new id
    try:
        a1 = int(s)
        if a1 > 0:
            return {'str': str(a1), 'num': 0}
        else:
            a1 = 1 / notId
            return {'str': str(a1), 'num': 1}

    except ValueError:
        return {'str': s, 'num': 0}


with open(inputFile, 'rU') as f:
    reader = csv.reader(f)
    badLine = []
    newLine = []
    for row in reader:

        if len(row) == 6:
            cleanId = cleanMemberId(row[2])
            notId += cleanId['num']
            row[2] = cleanId['str']

            for i in range(0, len(row)):
                # Collect elements
                newLine.append(row[i])
            wr1.writerow(newLine)
            # Prepare for new tweets.
            newLine = []

            if len(badLine) > 0:
                # If we have a bad tweet now that we found a proper tweet store the bad one that spread across lines.
                wr2.writerow(badLine)
                # Prepare for new tweets.
                badLine = []
        else:
            for i in range(0, len(row)):
                # Collect elements
                badLine.append(row[i])


resultFile.close()
badFile.close()

