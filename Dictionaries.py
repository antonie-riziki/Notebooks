daysOfWeek = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
    }

print(daysOfWeek.get(9, "Not a valid day of the week"))
print(daysOfWeek.get(4))
key, value = next(iter(daysOfWeek.items()))
for i in range(7):
    i += 1
    #key, value = next(iter(daysOfWeek.items()))
    #print("The key of days of week is: ", daysOfWeek(str(key)) + " which is ", daysOfWeek(str(value)))
    
    
for i in range(1):
    print(list(daysOfWeek.keys()),"",list(daysOfWeek.values()))
    i =+ 1
#print(list(daysOfWeek.valueas(3)))

todays = str(daysOfWeek.keys())
print(todays.split("\t"))
print(daysOfWeek.values())
print()
print()
numbers = dict(x=5, y=0)
maths = "bssid" 
print('numbers =', numbers)
print(type(numbers))

empty = dict(numbers)
print('empty =', empty)
math = dict(empty)
print("Math =", math)
print(type(empty))



marks = {}.fromkeys(['Math','English','Science'], 0)

# Output: {'English': 0, 'Math': 0, 'Science': 0}
print(marks)
name = input("Name : ")
score = int(input("Score : "))
newMark = marks.setdefault(name, score)
newMark = marks.items()
#print(newMark)

newResults = {}.fromkeys(newMark)
print(newResults)

#for item in marks.items():
 #   print(item)

# Output: ['English', 'Math', 'Science']
list(sorted(marks.keys()))
