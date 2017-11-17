def stringsRearrangement(inputArray):
    '''
    Given an array of equal-length strings, check if it is possible to rearrange the strings in 
    such a way that after the rearrangement the strings at consecutive positions would differ 
    by exactly one character.
    '''
    totalLen = len(inputArray)
    for i in range(totalLen):
        print("================================================")
        if analizeElement(inputArray[i], inputArray[:i] + inputArray[i + 1:], 1, totalLen):
            return True
        print("================================================")
    return False


def analizeElement(item, array, step, totalLen):
    print("Now analizing '{}' with array {} in step {}".format(item, array, step))
    if step == totalLen:
        return True
    for i in range(len(array)):
        if sum(1 for a, c in zip(item, array[i]) if a != c) == 1:
            if analizeElement(array[i], array[:i] + array[i + 1:], step + 1, totalLen):
                return True
    return False


print(stringsRearrangement(["abc",  "bef",  "bcc", "bec",  "bbc",  "bdc"]))
print(stringsRearrangement(["aba", "bbb", "bab"]))
