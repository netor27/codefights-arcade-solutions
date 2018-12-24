def videoPart(part, total):
    partSec = getSeconds(part)
    totalSec = getSeconds(total)

    divisor = gcd(partSec, totalSec)
    print (divisor)
    return [partSec // divisor, totalSec // divisor]

def getSeconds(time):
    splitted = time.split(':')
    return int(splitted[0]) * 3600 + int(splitted[1]) * 60 + int(splitted[2])


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a