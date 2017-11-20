def allLongestStrings(inputArray):
    '''
    Given an array of strings, return another array containing all of its longest strings.
    '''
    resultArray = []
    currentMax = len(inputArray[0])
    
    for i in range(len(inputArray) ):
        
        currentLen = len(inputArray[i])        
        if currentLen > currentMax :
            resultArray = [inputArray[i]]
            currentMax = currentLen
        elif currentLen == currentMax :
            resultArray.append(inputArray[i])
            
    return resultArray

print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))