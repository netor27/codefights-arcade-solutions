def arrayMaxConsecutiveSum(inputArray, k):
    '''
    Given array of integers, find the maximal possible sum of some of its k consecutive elements.
    '''
    maxValue = 0
    for i in range(k):
        maxValue += inputArray[i]
    
    aux = maxValue
    for i in range(k, len(inputArray)):
        aux -= inputArray[i-k]
        aux += inputArray[i]
        if aux > maxValue:
            maxValue = aux
    return maxValue    

