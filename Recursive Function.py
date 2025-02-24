"""
Return the factorial of any given value

Logic : n! = n * (n - 1) * (n - 2) * (n - 3) * (n - 4) * ....... n
Similarly: n! = n(n - 1!)

"""

def recursionFactorial(n):
    if n <= 1:
        return 1
    return n * recursionFactorial(n - 1)
print(recursionFactorial(5))
