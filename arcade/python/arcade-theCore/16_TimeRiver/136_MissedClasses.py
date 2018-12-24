from datetime import date

def missedClasses(year, daysOfTheWeek, holidays):
    count = 0
    daysSet = set([x-1 for x in daysOfTheWeek])

    for h in holidays:
        temp = getDateFromStr(h, year)
        if temp.weekday() in daysSet:
            count += 1
    return count

def getDateFromStr(s, year):
    m, d = map(int, s.split('-'))
    if m < 9:
        year += 1
    return date(year, m, d)