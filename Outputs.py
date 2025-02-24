x = 1
def f():
    x = 2
    y = x
    return x ** x * x + y
print (x)
print (f())
print (x + f())
