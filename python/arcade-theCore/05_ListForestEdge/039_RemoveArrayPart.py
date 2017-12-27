def removeArrayPart(inputArray, l, r):
    '''
    Remove a part of a given array between given 0-based indexes l and r (inclusive).
    '''
    return inputArray[0:l] + inputArray[r+1:]