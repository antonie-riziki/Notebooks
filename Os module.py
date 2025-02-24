import os
from datetime import datetime
from math import *

print(dir(os))
print(os.getcwd())
#os.mkdir("os module11")""" make directory
#print(os.listdir())
""" Print the list of all directories in cwd """
#print(os.removedirs("os module11"))
#print(os.removedirs("os module2"))
#print(os.removedirs("os module3"))
print(os.listdir())
print()
print()

""" Check the stats of a doc
access its mode time or any other field
convert the time into human readable format"""

print(os.stat("hubble_data.csv"))
print("Time: " , os.stat("hubble_data.csv").st_mtime)
modeTime = os.stat("hubble_data.csv").st_mtime
print("Date and Time :", datetime.fromtimestamp(modeTime))

print()
print()

"""
use os.walk() module to access the tree structure of the current path
and its contents including directories and files 
"""

for dirpath, dirname, dirfile in os.walk("D:/Python"):
    print("Directory Path : ", dirpath)
    print("Directory Name : ", dirname)
    print("Directory Files : ", dirfile)
    print()
    print()
