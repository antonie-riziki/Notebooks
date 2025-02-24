# import module sys to get the type of exception
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
print()
print()

age = int(input("Enter your age : "))
limit = 18
for i in str(age):
    try:
        int(i) >= limit
        nationalId = int(input("Enter National ID : "))
        print("You're now an adult")
        break
    except:
        print("You're too young for this site")
        print(sys.exc_info()[0], "Error occured since age is below limit")
        print()

print("Thanks for visiting our Website")
