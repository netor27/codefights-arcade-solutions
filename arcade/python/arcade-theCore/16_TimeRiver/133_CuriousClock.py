from datetime import datetime

def curiousClock(someTime, leavingTime):
    timeFormat = "%Y-%m-%d %H:%M"
    s = datetime.strptime(someTime, timeFormat )
    l = datetime.strptime(leavingTime, timeFormat)
    diff = l - s
    res = s - diff
    print("fail at", s)
    print("leaving at", l)
    print("diff", diff)
    print("res", res)
    return res.strftime(timeFormat)
