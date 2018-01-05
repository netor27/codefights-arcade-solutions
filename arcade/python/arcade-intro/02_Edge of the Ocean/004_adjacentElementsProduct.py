def adjacentElementsProduct(inputArray):
    '''Given an array of integers, find the pair of adjacent elements 
    that has the largest product and return that product.
    '''
    n = len(inputArray)
    if n < 2:
        raise "inputArray must have at least 2 elements"

    maxValue = inputArray[0] * inputArray[1]
    for i in range(n - 1):
        aux = inputArray[i] * inputArray[i + 1]
        if aux > maxValue:
            maxValue = aux
    return maxValue

print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))
