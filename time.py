import datetime
import calendar
import math
import os
import sys

"""
Calc the no. of days until payment is done
"""
bal = 5000
interestRate = 0.13
payAmount = 1000

sysDate = datetime.datetime.today()
print(sysDate)

endMonth = calendar.monthrange(sysDate.year, sysDate.month)[1]
print(endMonth)

daysTillEndMonth = endMonth - sysDate.day
print(daysTillEndMonth)

nextMonthStartDate = sysDate + datetime.timedelta(daysTillEndMonth + 1)
print(nextMonthStartDate)

endDate = nextMonthStartDate
#rate = (interestRate / 12) * bal
#print(round(rate, 2))

count = 0
while bal > 0:
    rate = (interestRate / 12) * bal
    bal += rate
    bal -= payAmount

    if bal < 0:
        bal = 0
    print(endDate.date(), round(bal, 2))

    endMonth = calendar.monthrange(endDate.year, endDate.month)[1]
    endDate = endDate + datetime.timedelta(days = endMonth)
    count += 1
print("Payment is due in the next", count, "months")

"""
Calc weight loss in weeks
"""
currentWeight = 360
targetWeight = 120
avgWeekLoss = 2.9

currentDate = datetime.datetime.today()
gymEndDate = currentDate

while currentWeight > targetWeight:
    currentWeight -= avgWeekLoss
    gymEndDate += datetime.timedelta(days = 7)

print("Target End Date:", gymEndDate.date())
print(f"Cogratulations on your work out. You've lost {currentWeight} lbs in {(gymEndDate - currentDate).days //7} weeks")

"""
Calc days to targeted subscribers
"""
    
targetSub = 150000
currentSub = 10000
avgSubPerDay = 50

remainingSub = targetSub - currentSub
print(remainingSub)

daysRemaining = math.ceil(remainingSub / avgSubPerDay)
print(daysRemaining)

currentSubDate = datetime.datetime.today()
print("Subscription Target End Date: ",(currentSubDate + datetime.timedelta(days = daysRemaining)).date())

"""
Book Club
"""

bookPages = 750
targetPage = 700
avgPagePerDay = 5 

remainingPages = bookPages - targetPage
print(remainingPages)

avgBook = math.ceil(remainingPages / avgPagePerDay)
print("Average Book: ", avgBook)

currentBookTime = datetime.datetime.today()
print(currentBookTime)
newDate = datetime.datetime(2020, 11, 7)
print(newDate - currentBookTime)
#bookEndDate = currentBookTime
count = 0
while bookPages > targetPage:
    currentBookTime += datetime.timedelta(days = 10)
    bookPages -= avgPagePerDay
    count += 1
    print(currentBookTime.date(), bookPages)
print("Total Weeks: ", count)

    



