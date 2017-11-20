def arrayChange(inputArray):
    '''
    You are given an array of integers. On each move you are allowed to increase 
    exactly one of its element by one. Find the minimal number of moves required 
    to obtain a strictly increasing sequence from the input.
    '''
    if len(inputArray) < 2:
        return 0
    
    totalMoves = 0
    for i in range(len(inputArray)-1):
        if inputArray[i+1] <= inputArray[i]:
            diff = inputArray[i] - inputArray[i+1] + 1
            totalMoves += diff
            inputArray[i+1] += diff
    return totalMoves

print(arrayChange([1, 1, 1]))