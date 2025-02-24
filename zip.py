import sys
occupantName = ["Riziki Antonie", "Geoffrey Habil", "John Paul Pope", "Daniel Manyasi", "Naisula Naserian"]
profession = ["Software Engineering and Data Science", "Medicine & Health Records", "Architecture", "Social & Political Science", "Phsychology"]
institute = ["DreamVille", "KMTC", "University of Nairobi", "Kenya School of Governance", "University of Nairobi"]

for name, occupation, place in zip (occupantName, profession, institute):
    print (name +" has studied " + occupation + " in " + place)

print("")
print("Alternatively \nYou can use the 'f' format in zip to achieve \nthe same output")
print("")

for name, occupation, place in zip(occupantName, profession, institute):
    print(f"{name} has studied {occupation} in {place}", end = '')
    print("")
a = [2,4,6,7,1]
b = [3,5,9,2,15]

for x, y in zip(a, b):
    print(x + y)
    
a = ([3,4])
print(sys.stderr, "There's an error during execution process ", a)
#print(sys.exit(1))

#Unzipping the values using zip()
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)
