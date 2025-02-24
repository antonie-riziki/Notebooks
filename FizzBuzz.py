""" FizzBuzz Interview Quiz """

"""
Expected to print out 'FizzBuzz' if num% 5 == 0 and num% 3 == 0
print 'Fizz' if num % 3 == 0
print 'Buzz' if num % 5 == 0
otherwise print num
"""

for i in range(1, 101):
    if i%5 == 0 and i%3 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
