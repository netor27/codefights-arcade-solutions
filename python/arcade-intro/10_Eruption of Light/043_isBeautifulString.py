def isBeautifulString(inputString):
    '''
    A string is said to be beautiful if b occurs in it no more times than a; c occurs in it no more times than b; etc.

    Given a string, check whether it is beautiful.


    '''
    codes = [0 for _ in range(26)]
    # sum the codes in the string
    for i in range(len(inputString)):
        ch = getIntFromChar(inputString[i])
        codes[ch] += 1
    
    # the array should be in decreasing order (the values can be equal, it's not
    # strictly decreasing)
    
    for i in range(1, 26):
        if codes[i-1] < codes[i]:
            return False
    return True  
    
    
def getIntFromChar(ch):
    # substract 97, so the value 'a' is 0, 'b' is 1, and so on
    return ord(ch)-97