i = 1
while i <= 10: 
    print(i)
    i += 1

import numpy as np
guess = str(np.random.randint(100))
user_guess = []
user_guess_count = 0
guess_limit = 3
total_guess = False

print(guess)
while user_guess != guess and total_guess != True:
    if user_guess_count < guess_limit:
        user_guess = input("Enter your guess ")
        user_guess_count += 1
    else:
        total_guess = True
        
if total_guess: 
    print("Out of guesses!!! Try again later, dummy")
    print("Lucky Number: ", guess)
else:
    print ("You won the game")
    
a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        break
    print(a.pop())
print('Done.')

a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
        continue
    print(a.pop())
    break
print('Done.')
    

#a = ['foo', 'bar', 'baz', 'qux', 'corge']
#while a:
 #   print(a.pop())
#else:
 #   print('Done.')

s = ""

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break
print(s)
