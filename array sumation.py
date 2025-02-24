number = [67]
def minMaxSum():
    for i in number:
        i = 5
        arr = int(input("Enter a number "))
        while int(arr) == number:
            print(int(arr + i))
    return int(arr + i)
print(minMaxSum())
