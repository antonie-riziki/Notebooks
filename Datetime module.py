import datetime
import pytz

"""
The datetime module
"""

#Create a date 
d = datetime.date(2016, 7, 24)
print("Date created: ", d)

#Output current sys day
tday = datetime.date.today()
print("Current system date: ", tday)

#Print the year
print("Year: ", tday.year)

#print weekday
print("Iso weekday: ", tday.isoweekday()) #""" Monday 1 Sunday 7 """
print("Normal Weekday: ", tday.weekday()) #""" Monday 0 Sunday 6 """

#Create time delta
#Time delta calculates the difference between 2 dates
tdelta = datetime.timedelta(days = 7)

bday = datetime.date(2021, 4, 9)

dateTillBday = (bday - tday)
print("Remaining Days: ", dateTillBday.days)
print("Total Remaining Seconds: ", dateTillBday.total_seconds())

weekLater = tday + tdelta
print("A week later date: ", weekLater)
print()
print()

"""
The Time module
"""

#Create a time
t = datetime.time(9, 12, 8, 1000)
print("Time Created: ", t)

#Current sys Time
currentTime = datetime.datetime.now()
print("Current system Time: ", currentTime.ctime())
dt = datetime.datetime(2021, 4, 9, 00, 00, 00, 100000)
print("Current sys Date & Time: ", dt)
bdayFullTime = datetime.datetime.today()
print("Birthday date: ", bdayFullTime)
timeDiff = dt - bdayFullTime
print("Difference :", timeDiff)

tdelta = datetime.timedelta(hours = 24)
print("Next 24hrs Date: ", currentTime + tdelta)
print()
print()


"""
Using the pytz module
"""
pytzDateTime = datetime.datetime(2016, 7, 27, 3, 45, 10, tzinfo = pytz.utc)
print("PYTZ created datetime: ", pytzDateTime)

dtUTCNow = datetime.datetime.utcnow().replace(tzinfo = pytz.utc)
print("Current Datetime UTC: ", dtUTCNow)

#Create a time in your local time zone
myTimeZone = dtUTCNow.astimezone(pytz.timezone("AFRICA/NAIROBI"))
print("My Local Time Zone: ", myTimeZone)

#Print all timezones in the pytz lib
##for tz in pytz.all_timezones:
##    print(tz)
                                
#Create timezone from a naive datetime
dt = datetime.datetime.now()
myLocalTime = pytz.timezone("AFRICA/NAIROBI")
dt = myLocalTime.localize(dt)
print("Localize Naive Datetime: ", dt)

#Output date in a certain isoformat
dt = datetime.datetime.now(tz = pytz.timezone("AFRICA/NAIROBI"))
print("Date in isoformat: ", dt.strftime("%B %dTH, %Y"))

dtStr = "May 20, 2020"
dt = datetime.datetime.strptime(dtStr, "%B %d, %Y")
print("Date in strptime format: ", dtStr)
