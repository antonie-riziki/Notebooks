#Using f string function to separate a large number
from random import randint
num1 = 1000000000000
num2 = 19878634981863

cents = randint(1, 9)
total = num1 + num2
print (total) #Outputs large number
print (f'${total:,}.{cents}')
