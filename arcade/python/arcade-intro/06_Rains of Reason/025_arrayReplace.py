def arrayReplace(inputArray, elemToReplace, substitutionElem):
    '''
    Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.
    '''
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray


print(arrayReplace([1, 2, 1], 1, 3))