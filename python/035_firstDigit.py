def firstDigit(inputString):
    '''
    Find the leftmost digit that occurs in a given string.
    '''
    for i in inputString:
        if i.isdigit():
            return i
    return None
        
print(firstDigit("var_1__Int"))
print(firstDigit("q2q-q"))
print(firstDigit("0ss"))