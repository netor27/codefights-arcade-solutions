def addTwoDigits(n):
    '''
    You are given a two-digit integer n. Return the sum of its digits.
    '''
    return n % 10 + n // 10

print(addTwoDigits(29))