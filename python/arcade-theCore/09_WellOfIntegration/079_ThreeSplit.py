'''
You have a long strip of paper with integers written on it in a single line from left to right. You wish to cut the paper into exactly three pieces such that each piece contains at least one integer and the sum of the integers in each piece is the same. You cannot cut through a number, i.e. each initial number will unambiguously belong to one of the pieces after cutting. How many ways can you do it?

It is guaranteed that the sum of all elements in the array is divisible by 3.

Example

For a = [0, -1, 0, -1, 0, -1], the output should be
threeSplit(a) = 4.

Here are all possible ways:

[0, -1] [0, -1] [0, -1]
[0, -1] [0, -1, 0] [-1]
[0, -1, 0] [-1, 0] [-1]
[0, -1, 0] [-1] [0, -1]
'''

def threeSplit(a):
    r = 0
    sumPart = sum(a) / 3
    for p1 in getPositionsToCut(a, 0, sumPart):
        for p2 in getPositionsToCut(a, p1 + 1, sumPart):
            if isLastPartCorrectlyCutted(a, p2, sumPart):
                r += 1
    return r
        
        
def getPositionsToCut(a, start, sumPart):
    r = []
    total = 0
    for pos in range(start, len(a)):
        total += a[pos]
        if total == sumPart:
            r.append(pos)
    return r


def isLastPartCorrectlyCutted(a, start, sumPart):
    if start + 1 >= len(a):
        return False    
    return sum(a[start+1:]) == sumPart

