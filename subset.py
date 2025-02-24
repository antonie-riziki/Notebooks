issubset = False
for i in range(int(input("Enter the range: "))):  
    a = int(input("a: "))
    A = set(input("A: ").split())
    b = int(input("b: ")) 
    B = set(input("B: ").split())
    print (A.issubset(B))
    #issubset = True
