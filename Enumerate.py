#Enumerate
daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursady", "Friday", "Saturday", "Sunday"]

for days in enumerate(daysOfTheWeek):
    print(days)

print("=" * 30)

for days in enumerate(daysOfTheWeek, 1):
    print(days)

print("=" * 30)

for count, days in enumerate(daysOfTheWeek, 1):
    print(count, days)

print("=" * 30)
    
monthsOfTheYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

for count, months in enumerate(monthsOfTheYear, 1):
    print(count, months)

