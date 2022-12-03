import csv
import pandas as pd  
def getOutputHeader():
    filename="sample-mademarket-contacts.csv"
    with open(filename, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header=next(csv_reader)
    return header
def readMm():
    mmFilename="sample-mademarket-contacts.csv"
    companiesSet=set()
    with open(mmFilename, newline='') as datareader:
        datareader = csv.reader(datareader)
        for row in datareader:
            companiesSet.add(row[4]) if row[4] not in companiesSet else print(f'{row[4]} already in set')
    return companiesSet
def readV8():
    vFilename="sample-mademarket-contacts.csv"
    rowsList={}
    with open(vFilename, newline='') as datareader:
        datareader=csv.reader(datareader)
        for row in datareader:
            rowsList[row[4]]=row
    return rowsList
def genNewfile(header:list[str], mmCompanies:set, v8Companies:dict):
    with open('outputBatch.csv', 'w') as filewriter:
        filewriter = csv.writer(filewriter)
        filewriter.writerows(v8Companies.values())

print(readV8())
genNewfile(getOutputHeader(), readMm(), readV8())