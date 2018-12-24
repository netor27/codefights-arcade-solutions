from datetime import datetime
def regularMonths(currMonth):
    splitted = currMonth.split('-')
    month = int(splitted[0])
    year = int(splitted[1])

    found = False
    while not found:
        month += 1
        if month > 12:
            month = 1
            year += 1
        aux = datetime(year, month, 1)
        if aux.weekday() == 0:
            found = True
    return "{:02d}-{}".format(month, year)

