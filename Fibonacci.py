"""
Fibonacci Sequence
Print out a num
where each num printed is the sumation of the previous 2 nums

"""

a,b = 0, 1
for i in range(1, 11):
    print(a)
    a,b = b, a + b


print()
print()

c,d = 0,1
for i in range(1, 11):
    print(c, ":", d)
    c,d = d, c+d
    
    

