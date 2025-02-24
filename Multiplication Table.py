import sys

try:
    arraySize = eval(input("Enter the Size of the Table : "))
except:
    raise TypeError ("Invalid Data Format ", arraySize)

for row in range(1, arraySize + 1):
    for column in range(1, arraySize + 1):
        product = row * column
        print('{0:4}'.format(product), end = "  " )
    print()

