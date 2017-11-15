def centuryFromYear(year):
    '''Given a year, return the century it is in. 
    The first century spans from the year 1 up to and including the year 100,
    the second - from the year 101 up to and including the year 200, etc.
    '''
    x = year // 100
    if year % 100 == 0:
        return x
    return x + 1


print(centuryFromYear(1900))