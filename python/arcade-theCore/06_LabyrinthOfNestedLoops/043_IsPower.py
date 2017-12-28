def isPower(n):
    '''
    Determine if the given number is a power of some non-negative integer.
    '''
    if n == 1:
        return True
    sqrt = math.sqrt(n)
    
    for a in range(int(sqrt)+1):
        for b in range(2, int(sqrt)+1):
            if a ** b == n:
                return True
    return False