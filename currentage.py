import datetime as datetime

def age(name, birthDate, birthMonth, birthYear):
	todaysDate = datetime.date.today()
	todaysDate = todaysDate.split('')
	currentYear = todaysDate
	currentDay = currentYear[0]
	currentMonth = currentYear[1]
	currentYear = currentYear[2]
	