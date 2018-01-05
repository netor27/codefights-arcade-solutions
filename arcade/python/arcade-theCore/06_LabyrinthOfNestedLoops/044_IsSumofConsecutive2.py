def isSumOfConsecutive2(n):
    '''
    Find the number of ways to express n as sum of some (at least two) consecutive positive integers.
    '''
    total = 0
    for i in range(1, n):
        start = i
        temp = i
        j = i+1
        while temp < n:
            temp += j
            j += 1
        if temp == n:
            total += 1
    return total