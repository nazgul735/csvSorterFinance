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


def getData():
    filename="data.csv"
    rowsList21={}
    with open(filename, newline='') as datareader:
        datareader=csv.reader(datareader)
        stat=False
        for row in datareader:
            temp=[]
            if row[0]=="#":
                stat=True
                continue
            elif stat is False:
                continue
            if stat is True:
                index=len(row)-3
                key=row[1].lower()
                if rowsList21 is None:
                    
                    temp.append(row[1].lower())
                    temp.append(row[27].lower())
                    temp.append(row[28].lower())
                    
                    for i in temp:
                        if i.lower() in rowsList21:
                            rowsList21[i]=float(rowsList21.get(key))+float(row[index])
                            continue
                
                rowsList21[key]=float(row[index])
        print(rowsList21)
getData()
