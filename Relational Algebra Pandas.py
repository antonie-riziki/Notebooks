import numpy as np
import pandas as pd
# We can create a series from a lit
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print("data looks like a numpy array: ", data)

# We can manually specify indexes
data = pd.Series([0.25, 0.5, 0.75, 1.0],        
                index=['a', 'b', 'c', 'd'])
print("data looks like a Python dict: ", data)

print(data['b'])
# We can create a Series directly from a dict:
population_dict = {'California': 38332521,
                    'Texas': 26448193,
                    'New York': 19651127,               
                    'Florida': 19552860,                  
                    'Illinois': 12882135}
area_dict = {'California': 423967,
            'Texas': 695662,
            'New York': 141297,
            'Florida': 170312,
            'Illinois': 149995}

population = pd.Series(population_dict)
area = pd.Series(area_dict)
print(population)
# What do you think of this line?
print(population['California':'Florida'])
# From a Series
df = pd.DataFrame(population, columns=['population'])
print(df)

# From a list of dict
data = [{'a': i, 'b': 2 * i} for i in range(3)]
df = pd.DataFrame(data)
print(df)

# From several Series
df = pd.DataFrame({'population': population,
                    'area': area})
print(df)

# From a 2-dimensional Numpy array
df = pd.DataFrame(np.random.rand(3, 2),
                columns=['foo', 'bar'],
                index=['a', 'b', 'c'])
print(df)

# A function to easily generate DataFrames. It will be very 
# useful in the rest of this chapter.
def make_df(cols, ind):    
    """Quickly create DataFrames"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)
    
# example
print(make_df('ABC', range(3)))

#Projection and selection
data = pd.Series([0.25, 0.5, 0.75, 1.0],
                index=['a', 'b', 'c', 'd'])
print(data)

print(data.loc['b'])
print(data.iloc[1])
data = pd.DataFrame({'area':area, 'pop':population})
print(data)
data.loc[:'Illinois', :'pop']
