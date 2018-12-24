from datetime import datetime

def dayOfWeek(birthdayDate):
    d = datetime.strptime(birthdayDate, "%m-%d-%Y").date()
    temp = d.replace(year=getNextYear(d))
    while temp.weekday() != d.weekday():
        temp = temp.replace(year=getNextYear(temp))
    print(temp)
    return temp.year - d.year


def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def getNextYear(date):
    baseYear = date.year + 1
    if date.day == 29 and date.month == 2:
        found = False
        while(not found):
            baseYear += 1
            if isLeapYear(baseYear):
                found = True

    return baseYear




