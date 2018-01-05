def alphabeticShift(inputString):    
    '''
    Given a string, replace each its character by the next one in the English 
    alphabet (z would be replaced by a).
    '''
    return ''.join(['a' if i == 'z' else chr(ord(i)+1) for i in inputString])


print(alphabeticShift("abcde"))
print(alphabeticShift("abcdezzz"))
