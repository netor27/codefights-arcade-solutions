def checkPalindrome(inputString):
    '''Given the string, check if it is a palindrome.'''
    return inputString == inputString[::-1]


print(checkPalindrome("aabaa"))
