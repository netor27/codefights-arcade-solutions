def arrayMaximalAdjacentDifference(inputArray):
    '''
    Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
    '''
    
    if len(inputArray) < 2:
        raise "The inputArray must contain at least 2 elements"
        
    maxDiff = abs(inputArray[0] - inputArray[1])
    
    for i in range(len(inputArray)-1):
        diff = abs(inputArray[i] - inputArray[i+1])
        if diff > maxDiff:
            maxDiff = diff
    return maxDiff

print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))
