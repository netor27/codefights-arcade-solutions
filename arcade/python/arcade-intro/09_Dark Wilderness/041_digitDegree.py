def digitDegree(n):
    '''
    Let's define digit degree of some positive integer as the number of times 
    we need to replace this number with the sum of its digits until we get 
    to a one digit number.
    Given an integer, find its digit degree.
    '''
    count = 0
    while n // 10 > 0:
        n = sumDigits(n)
        count += 1
    return count

def sumDigits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum
