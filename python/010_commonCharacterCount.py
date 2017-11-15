def commonCharacterCount(s1, s2):
    '''
    Given two strings, find the number of common characters between them.
    '''
    # use an array of 25 elements that represent a to z. a = 0, z = 24
    code = [0 for i in range(26)]
    base = 97
    for s in s1:
        code[ord(s)-base] += 1
    
    count = 0
    for s in s2:
        if code[ord(s)-base] > 0:
            code[ord(s)-base] -= 1
            count += 1
    return count

print(commonCharacterCount("aabcc", "adcaa"))