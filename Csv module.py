import csv
from math import *

with open("hubble_data.csv", "r") as file:
    reader = csv.DictReader(file)   #, delimiter = "\n")
    #for i in reader:
       #print(i)
    
    """ next(reader) """ ##Doesnt print the first row of the file
    for row in reader:
       print(row)
       #print(row["recessionVelocity"])

#hubble_data.csv = reader("hubble_data.csv", dialect = ' ')

""" Creating a new .csv file """

with open("hubble_data.csv","r") as file:
    readfile = csv.reader(file)

    with open("newHubbleData.csv", "w") as newFile:
        writer = csv.writer(newFile, delimiter = "\t")

        for row in readfile:
            print(writer.writerow(row), end = "\n")
            
with open ("D:\Open Classroom\Web Development\Section 16 - MySQL Database Integration\Lecture 304 - SQL Select\select.php","r") as file:
    contents = file.read()
    print(contents)

with open ("D:\Open Classroom\Web Development\Section 16 - MySQL Database Integration\Lecture 304 - SQL Select\select.php","r") as rrf:
    with open("newSQLSelect.txt","w") as rf:
        for i in rrf:
            rf.write(i)
            with open("SQLSelectCopy.txt","w") as wf:
                for line in rrf:
                    wf.write(line)
                    print(wf)
         

class myFile:
    def __init__(self, fileName, mode):
        self.fileName = fileName
        self.mode = mode

    def __enter__(self):
        self.file = open(self.fileName, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback):
        self.file.close()

with myFile("D:\Python\hubble_data.csv","r") as f:
    readMyFile = csv.reader(f)
    print(readMyFile)
 
