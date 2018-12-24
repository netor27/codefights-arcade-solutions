from datetime import datetime, date

weekDays = { "Monday":0, "Tuesday":1, "Wednesday":2, "Thursday":3, "Friday":4, "Saturday":5, "Sunday":6}

def holiday(x, weekDay, month, yearNumber):
    dateStr = "01-{}-{}".format(month, yearNumber)
    base = datetime.strptime(dateStr, "%d-%B-%Y").date()
    weekDayIndex = weekDays[weekDay]
    aux = ((weekDayIndex - base.weekday()) % 7) + (7*(x-1))

    try:
        res = date(base.year, base.month, base.day + aux)
    except ValueError:
        return -1
    return res.day




