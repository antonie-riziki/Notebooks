n = 8
suma = 1

for i in range(n):
    i *= n
    n -= 1
##    i = n*n
##    suma *= i
    print(n)
    for num in n:
        n *= n
        print(n)
    
    
##suma *= i
##print(suma)
##    

