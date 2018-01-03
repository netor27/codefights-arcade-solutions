'''
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

'''
def allLongestStrings(inputArray):
    longestStrings = []
    longestValue = len(inputArray[0])
    
    for string in inputArray:
        if len(string) == longestValue:
            longestStrings.append(string)
        elif len(string) > longestValue:
            longestValue = len(string)
            longestStrings = [string]
    
    return longestStrings