# Python code to demonstrate working of 
# Extracting key-value of dictionary in variables 
# Using items() 
  
# Initialize dictionary 
#test_dict = {'gfg' : 1} 
  
# printing original dictionary 
#print("The original dictionary : " +  str(test_dict)) 
  
# Using items() 
# Extracting key-value of dictionary in variables 
#key, val = test_dict.items()[0] 
  
# printing result  
#print("The 1st key of dictionary is : " + str(key)) 
#print("The 1st value of dictionary is : " + str(val))



# Using iter() + next() 
  
# Initialize dictionary 
test_dict = {'gfg' : 1} 
  
# printing original dictionary 
print("The original dictionary : " +  str(test_dict)) 
  
# Using iter() + next() 
# Extracting key-value of dictionary in variables 
key, val = next(iter(test_dict.items())) 
  
# printing result  
print("The 1st key of dictionary is : " + str(key)) 
print("The 1st value of dictionary is : " + str(val)) 

dict1 = {
    'antonie' : 7,
    'geoffrey' : 15,
    'habil' : 12,
    'shiko' : 9
    }
key, val = next(iter(dict1.items()))
print(key, val)

