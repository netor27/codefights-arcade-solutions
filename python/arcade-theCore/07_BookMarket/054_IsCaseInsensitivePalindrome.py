def isCaseInsensitivePalindrome(inputString):
    '''
    Given a string, check if it can become a palindrome through a case change of some (possibly, none) letters.
    '''
    lowerCase = inputString.lower()
    return lowerCase == lowerCase[::-1]


print(isCaseInsensitivePalindrome("AaBaa"))
print(isCaseInsensitivePalindrome("aabbc"))