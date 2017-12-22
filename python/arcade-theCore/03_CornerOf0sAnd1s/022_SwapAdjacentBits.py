def swapAdjacentBits(n):
    '''
    You're given an arbitrary 32-bit integer n. 
    Take its binary representation, split bits into it in pairs 
    (bit number 0 and 1, bit number 2 and 3, etc.) and swap bits in each pair. 
    Then return the result as a decimal number.
    '''
    return ((0x55555555 & n) << 1) | ((0xAAAAAAAA & n) >> 1)