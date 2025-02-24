import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
from math import *

sb.set()
print("Grade List")
grade = [[64, 75, 90, 82],
         [50, 55, 45, 68],
         [72, 86, 90, 90]]
print(grade)
print("")

gradeNumpy = np.array(grade)
print("Grade Array")
print(gradeNumpy)
print("")

print("Accessing row 1 of column 3 : ", gradeNumpy[1, 3])
print("")

gradePandas = pd.DataFrame(gradeNumpy, index = ["Jane", "Myles", "Eric"], columns = ["Year", "Year_2", "Year_3", "Year_4"])
print(gradePandas)
print("")

print("Display a given column")
print(gradePandas['Year_3'])
print("")

print("Display a given column")
print(gradePandas.Year_4 != 90)
print("")

print("Accessing Rows of a given table ")
print(gradePandas.loc["Jane"])
print("")

print("Accessing Rows of a given table using row variable/field")
print(gradePandas.loc["Eric"].Year)
print("")

print("Accessing Rows of a given table using row index")
print(gradePandas.iloc[1])
print("")

#mask module allows to access column data that meets a particular condition
#Also note that ~ operator is used to access the else structure of the condition
print("Mask to access columns under a given condition")
mask = gradePandas["Year_3"] >= 90 
print(gradePandas[mask])
print("Mask to access columns that doesnt satisfy the condition using ~ operator")
print(gradePandas[~mask])
print("")

#Add new data to the original data frame
print("Adding new data to the prevoius data frame (gradePandas)")
newGradePandas = pd.DataFrame([[45, 38, 30, 40],
                              [25, 32, 13, 0],
                              [50, 43, 36, 52],
                              [50, 55, 45, 68],
                              [17, 29, 45, 60],
                              [53, 77, 92, 83]], index = ["Brian", "Mercyline", "Joshua", "Miles", "Aswa", "Janet"], columns = gradePandas.columns)
print(newGradePandas)
print("")

#use append function to add the update to the prevoius data frame
gradePandas = gradePandas.append(newGradePandas)
#print(gradePandas.sort_values(by = "Year"))
print(gradePandas.sort_index())
"""
print(help(gradePandas.sort_values))
"""
print("")

#drop_duplicates function removes every duplicate data
newGradePandasWithoutDuplicate = gradePandas.drop_duplicates()
print(newGradePandasWithoutDuplicate)
print("")

#adding a new column to an existing data frame
newGradePandasWithoutDuplicate['Sex'] = ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F']
print("Add Sex column to the existing DataSet")
print(newGradePandasWithoutDuplicate)
print("")

#Using iterrows to loop through the dataframe
for index, columns in newGradePandasWithoutDuplicate.iterrows():
    print(index, "'s DataBase Report" )
    print(columns)
    print("-" * 50)
    print("")

print("")
#more functions
print(len(newGradePandasWithoutDuplicate))
print("")
print(newGradePandasWithoutDuplicate.median())
print("")

#Load CSV (Comma Seperated File
print("Load CSV File")
hubble = pd.read_csv("hubble_data.csv", sep = ",")
print(hubble)

titanic = sb.load_dataset('titanic')
print(titanic)
print(titanic.head())#head() func retrieves the first 5 rows of the dataset, you can also pass a value for a range i.e unique(10)
print(titanic.age.unique())#unique() func retrieves the dataset for the specific record/column
print(titanic.describe())#.head())
#titanic = titanic.dropna()#dropna() func removes the NaN values from the dataset
#print(titanic)
print(titanic.describe())
print(titanic.pivot_table("survived", index = "sex", aggfunc = "sum"))
print(titanic.tail(10))#tail() func retrieves the dataset for the last 5 set of data
print(titanic.describe(include = "all"))#include = "all", collects all the non-numeric columns in the analysis
print(titanic.head(10))
titanic = titanic.fillna({"age": 10})#fillna() func allows to fill the NaN to a specified input
print(titanic.head(10))
titanic1 = titanic.fillna(method = "pad").head(10)#method = "pad" func allows autofill for the NaN fields with the previous values
print(titanic1.describe(include = "all"))
print(titanic.dropna(axis = "columns").describe())
titanic = titanic.rename(columns = {"sex":"gender"})#Renaming rows and columns
print(titanic.head())
#print(titanic.drop(0))#deletes records of the given index
#print(titanic.drop(columns = {"gender"}))#deletes rows and columns
print(titanic)
