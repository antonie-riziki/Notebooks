import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import pandas as pd
import sys
import csv

s = []
for i in range(26):
    i += 1
    s.append(i)
    #print (i)

sb.set()
plt.style.use("bmh")
distance = [0.032,0.034,0.214,0.263,0.275,0.275,0.45,0.5,0.5,0.63,0.8,0.9,0.9,0.9,0.9,1,1.1,1.1,1.4,1.7,2,2,2,2]
recessionVelocity = [170,290,-130,-70,-185,-220,200,290,270,200,300,-30,650,150,500,920,450,500,500,960,500,850,800,1090]
x = np.linspace(0, 24, 24)
plt.rcParams.update({"font.size": 14})
plt.scatter(x, recessionVelocity, color = "black", label = "Velocity")
d = np.linspace(0, 26, 26)
plt.plot(d, s, color = "black", label = "Line")
#plt.plot(x, recessionVelocity, color = "black", label = "Velocity")
y = plt.axes()
y.set(xlabel = "Recession Velocity", ylabel = "Distance")
plt.legend(loc = "best")
plt.title("Linear Regression of Distance against Velocity")
plt.show()

with open("hubble_data.csv", "r") as f:
    reader = csv.reader(f)
    print(reader)
    print("File Name : ", f.name)
    print()
    print("Mode : ", f.mode)
    print()
    print("File Closed : ", f.closed)
    print()
    stry = f.read(20) 
    print("File read : \n", stry)
    print()
    #srtyPandas = pd.DataFrame(f, index = [f.read(2)], columns = ["distance", "velocity"])
    #print(stry)
    print()
    fid = f.fileno()
    print("File No. : ", fid)
