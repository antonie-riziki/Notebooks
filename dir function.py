#The dir function returns a list of all members of a given module, class, instance, or other type
def dump(value):
    print (value, " => ", dir(value))
import sys
dump("os")
print()
##dump(1.0)
##print()
##dump(0.0j) # complex number
##print()
##dump([]) # list
##print()
##dump({}) # dictionary
##print()
##dump("string")
##print()
##dump(len) # function
##print()
##dump(sys) # module
##print()
##dump("")

sys.exit()
import json 
  
# python object(dictionary) to be dumped 
dict1 ={ 
    "emp1": { 
        "name": "Lisa", 
        "designation": "programmer", 
        "age": "34", 
        "salary": "54000"
    }, 
    "emp2": { 
        "name": "Elis", 
        "designation": "Trainee", 
        "age": "24", 
        "salary": "40000"
    }, 
} 
  
# the json file where the output must be stored 
#out_file = open("myfile.json", "w") 
with open("Employees.json", "w") as out_file:
    json.dump(dict1, out_file, indent = 6)
    out_file.close() 
