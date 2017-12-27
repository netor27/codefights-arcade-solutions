def increaseNumberRoundness(n):
    '''
    Define an integer's roundness as the number of trailing zeroes in it.
    Given an integer n, check if it's possible to increase n's roundness by swapping some pair of its digits.
    '''
    return re.search('\d*0[1-9]+', str(n)) is not None

