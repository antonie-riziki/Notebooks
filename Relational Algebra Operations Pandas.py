import pandas as pd
import numpy as np

#Create a series of data 
ser = pd.Series([1,2,3,4,5,6,7], index = ["a","b","c","d","e","f","g"])
print(ser)

#Create an increament dictionary 
data = [{"a": i, "b": 2*i} for i in range(0, 4)]
print(data)
##for i in range (0, 4):
##    data = {"a": i, "b": 2*i}
##    print(data)
        
#Create a dataframe from the above dictionary
df = pd.DataFrame(data, index = ["^0", "^1", "^2", "^3"])
print("Creatign DataFrame: ", df)

#Projection - selcting certain columns
print("Selcting a column:", ser)
print("Column with index ['c']: ", ser.loc['c'])
print("Column with index[6]: ", ser.iloc[6])

#Restriction - Selecting certain rows
print(ser)

area = pd.Series({"California": 423967,
                  "Texas": 695662,
                  "New York": 141297,
                  "Florida": 170312,
                  "Illinois": 149995})

pop = pd.Series({"California": 38332521,
                 "Texas": 26448193,
                 "New York": 19651127,
                 "Florida": 19552860,
                 "Illinois": 12882135})

cities = pd.DataFrame({"area":area, "pop": pop})
print(cities)

print()
print()

#Projection and Restriction
print("DataFrame based on California: \n", cities.loc['California'])
print("DataFrame based on area:\n", cities.loc[:,'area'])
