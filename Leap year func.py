"""DRY - Dont Repeat Yourself"""
import datetime

print(datetime.date.today())
def age(name, birthDate, month, year):
		
    todaysDate = str(datetime.date.today())
    currentYear = todaysDate.split('-')

    activeYear = int(currentYear[0])
    currentMonth = int(currentYear[1])
    currentDay = int(currentYear[2])

    print(f"{datetime.date.today()}")	
    currentAge = activeYear - year
    if birthDate == currentDay and month == currentMonth:
       print(f"Hello {name}! Its {activeYear} and you're now {currentAge} years old")
       print(f"Happy Birthday to you!!!")
    else:
       print(f"Its not yet your birthday dummy... but you're {currentAge} years old.")

monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#print(len(monthDays))


"""
#def isLeap1(year):
 #   if year%4 == 0:
  #      if year%100 != 0 and year%400 == 0:
   #         return False
    #    elif year%100 == 0 and year%400 == 0:
     #       return True
    #else:
     #   return False
     """

def isLeap(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def daysInMonth(year, month):
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and isLeap(year):
        return 29

    return monthDays[month]

age(name = input("Enter your name : "),  
    birthDate = int(input("Date [dd]: ")),
    month = int(input("Month [mm]: ")),
    year = int(input("Year [yyyy] :")))

"""print("Is leap year : ", isLeap1(2020))"""
print("Is leap year : ", isLeap(year))
print(daysInMonth(year, month))

