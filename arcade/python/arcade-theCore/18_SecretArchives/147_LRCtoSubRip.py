def lrc2subRip(lrcLyrics, songLength):
    res = []
    sp = []
    for l in lrcLyrics:
        splitted = l.split(" ", 1)
        text = splitted[1] if len(splitted) > 1 else ""
        time = getsubRipTime(splitted[0])
        sp.append((time, text))
    print(sp)

    counter = 1
    for i in range(len(sp)-1):
        res.append(str(counter))
        res.append("{} --> {}".format(sp[i][0], sp[i+1][0]))
        res.append(sp[i][1])
        res.append("")
        counter += 1

    h,m,s = map(int, songLength.split(":"))
    endTimeStr = "{:02}:{:02}:{:02},{:03}".format(h, m, s, 0)
    res.append(str(counter))
    res.append("{} --> {}".format(sp[i+1][0], endTimeStr))
    res.append(sp[i+1][1])
    return res


def getsubRipTime(lrcTime):
    minute = int(lrcTime[1:3])
    hour = minute // 60
    minute = minute % 60
    second = int(lrcTime[4:6])
    milli = int(lrcTime[7:9]) * 10
    return "{:02}:{:02}:{:02},{:03}".format(hour, minute, second, milli)

