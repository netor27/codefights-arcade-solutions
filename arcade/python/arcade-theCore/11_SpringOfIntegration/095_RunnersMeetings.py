'''
Some people run along a straight line in the same direction. They start simultaneously at pairwise distinct positions and run with constant speed (which may differ from person to person).

If two or more people are at the same point at some moment we call that a meeting. The number of people gathered at the same point is called meeting cardinality.

For the given starting positions and speeds of runners find the maximum meeting cardinality assuming that people run infinitely long. If there will be no meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
runnersMeetings(startPosition, speed) = 3.

In 20 seconds after the runners start running, they end up at the same point.
'''

def runnersMeetings(startPosition, speed):
    currentMax = -1
    for i in range(len(startPosition)):
        t, d = -1, -1
        aux = -1
        for j in range(i+1, len(startPosition)):
            t, d = getTimeAndDistanceOfMeeting(speed[i], startPosition[i], speed[j], startPosition[j])
            if t >= 0:
                aux = 2
                for k in range(j+1, len(startPosition)):
                    if (speed[k] * t + startPosition[k]) == d:
                        aux += 1
            currentMax = max(currentMax, aux)
    return currentMax   

    
def getTimeAndDistanceOfMeeting(v1, b1, v2, b2):
    if v1 == v2:
        return -1, -1
    time = (b2-b1) / (v1-v2)
    distance = v1 * time + b1
    return time, distance