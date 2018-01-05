def longestDigitsPrefix(s):
    '''
    Given a string, output its longest prefix which contains only digits.
    '''
    i = 0
    n = len(s)
    while i < n and s[i].isdigit():        
        i+=1
        
    return str(s[:i])