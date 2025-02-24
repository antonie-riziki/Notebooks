target = 78

while True :
    """ value = input("Enter an integer between 1 and 100 \n") """
    try:
        """ value = int(value) """
        value = int(input("Enter an integer between 1 and 100 \n"))
        break
    except ValueError:
        print("An integer value is needed to process execution")

if int(value) > target:
    print("Number too high")
elif int(value) < target:
    print("Number too low")
else:
    print("Perfect guess")
    
#for n in range(7):
 #   print("You the flower that I gotta protect and keep alive in the winter, dontchya die yet")
    
val = "antonie"
while val in val:
    if val == "o":
        print(val)


