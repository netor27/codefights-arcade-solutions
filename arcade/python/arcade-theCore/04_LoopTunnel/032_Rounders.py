def rounders(value):
    '''
    We want to turn the given integer into a number that has only one non-zero digit using a tail rounding approach. 
    This means that at each step we take the last non 0 digit of the number and round it to 0 or to 10. 
    If it's less than 5 we round it to 0 if it's larger than or equal to 5 we round it to 10 
    (rounding to 10 means increasing the next significant digit by 1). 
    The process stops immediately once there is only one non-zero digit left.

    '''
    return roundLast(value, 0)
    

def roundLast(value, digit):
    if value < 10:
        return value * 10 ** digit    
    if value % 10 >= 5:
        value += 10
    value -= (value %10)    
    return roundLast(value//10, digit+1)


print(rounders(15))
print(rounders(145))
print(rounders(144))
print(rounders(545))
print(rounders(544))
print(rounders(1445))
print(rounders(1444))


