n = int(input())
if int(n)%2 == 0:
    if n>=2 and n<=5:
        print("Not Weird")
    elif n>=6 and n<=20:
        print("Weird")
    elif n%2!=0 or n%2==0 or n>20:
        print("Not Weird")
elif n%2!=0 or n<20:
    print("Weird")
