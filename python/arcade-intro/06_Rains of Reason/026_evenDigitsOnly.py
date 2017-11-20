def evenDigitsOnly(n):
    '''
    Check if all digits of the given integer are even
    '''
    digits = [int(i) for i in str(n)]
    for d in digits:
        if d % 2 != 0:
            return False
    return True

print(evenDigitsOnly(248622))
print(evenDigitsOnly(642386))