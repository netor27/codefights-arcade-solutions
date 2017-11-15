def avoidObstacles(inputArray):
    '''
    You are given an array of integers representing coordinates of obstacles 
    situated on a straight line.
    
    Assume that you are jumping from the point with coordinate 0 to the right.
    You are allowed only to make jumps of the same length represented by some integer.
    
    Find the minimal length of the jump enough to avoid all the obstacles.
    '''
    maxValue = max(inputArray)
    mySet = set(inputArray)
    
    i = 2    
    while i <= maxValue:
        current = 0
        collision = False
        while not collision:
            if current in mySet:
                collision = True
            if current > maxValue:
                return i
            current += i
        i += 1
    
    return maxValue + 1

print(avoidObstacles([5, 3, 6, 7, 9]))