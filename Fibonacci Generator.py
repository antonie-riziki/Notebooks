"""
Fibonacci Generators
"""

def fib(num):
    a, b = 0,1
    for i in range(0, num):
        yield "{}:{} = {}".format(i+1, a, b)
        
        """
        Yield returns the given statement and execution continues
        Return returns the given statement and stops execution of the code
        """
        
        a,b = b, a+b
        #print("A : B ==>", a ,":", b)
print("  A  B")
for item in fib(10):
    print (item)
