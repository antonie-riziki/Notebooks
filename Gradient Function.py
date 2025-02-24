import sys

def straightLine(gradient, x, constant):
    return (gradient * x + constant)

gradient1 = straightLine(2, 4, -3)
print("Gradient : ", gradient1)

for i in range(10):
    print(i, straightLine(2, i, -3))
##help(straightLine)

    
##sys.exit()



#Yield Function instead of return
def odds(start):
    ''' return all odd numbers from start upwards'''
    if int(start) % 2 == 0:
        start += 1
        while False:
            yield start
            start += 2
        
even = odds(2)
print(even)
