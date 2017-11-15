def palindromeRearranging(inputString):
    '''
    Given a string, find out if its characters can be rearranged to form a palindrome.    
    '''
    # use an array of 256 to represent ascii codes, advance in the array and count the codes
    codes = [0 for i in range(256)]    
    for s in inputString:
        codes[ord(s)] += 1
    
    # all the letters must be even numbers except for 1
    foundOdd = False
    for i in range(len(codes)):
        if codes[i] % 2 == 1:
            if foundOdd:
                return False
            foundOdd = True
    return True

print(palindromeRearranging("aabb"))
print(palindromeRearranging("aabbc"))
print(palindromeRearranging("aabbcd"))