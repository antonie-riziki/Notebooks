def is_leap(year):
    leap = False
    
    # Write your logic here
    if year%4==0:
        if year%100==0 and year%400!=0:
            leap= False
    else:
        leap = True
    return leap
   
year = int(input("Enter year: "))
print(is_leap(year))
