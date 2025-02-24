import sys
print(sys.argv)
print(sys.getallocatedblocks())
#print(sys.exit())

for i in range(10):
    print (i, i*i, i*i*i)
    
a = range(10)
for x in a:
    if x % 2 == 0:
        print(x*x*x)

a, b = 17, 5
print(a.__mul__(b))

for c in "Python":
    print (c)
colors =['Red', 'Brown', 'Blue', 'Black', 'Yellow', 'Green', 'White']
print(colors)
colors.reverse()
print(colors)
colors.append('Maroon')
print(colors)

