def mirrorBits(a):    
    '''
    Reverse the order of the bits in a given integer.
    '''
    binary = bin(a)[2:]
    integer = int(binary[::-1], 2)
    return integer


print(mirrorBits(97))