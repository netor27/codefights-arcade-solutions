def newYearCelebrations(takeOffTime, minutes):
    currentTime = getTotalMinutes(takeOffTime)
    newYearsTime = 24 * 60

    acum = 0
    for i in range(len(minutes)):
        minutes[i] -= acum
        acum += minutes[i]
    print(minutes)

    count = 0
    for m in minutes:
        print("Current Time ", getHourFromMin(currentTime),"({})".format(currentTime), "TimeToNextTimeZone", m, "TimeWhenCrossingTimeZone", getHourFromMin(currentTime+m))
        if currentTime + m >= newYearsTime and currentTime <= newYearsTime:
            count += 1
        currentTime = currentTime + m - 60

    if currentTime <= newYearsTime:
        count += 1
    return count



def getTotalMinutes(time):
    split = [int(x) for x in time.split(':')]
    if split[0] == 0:
        res = 24 * 60
    else:
        res = split[0] * 60

    res += split[1]
    return res

def getHourFromMin(m):
    h = m // 60
    m = m % 60
    return "{}:{}".format(h,m)