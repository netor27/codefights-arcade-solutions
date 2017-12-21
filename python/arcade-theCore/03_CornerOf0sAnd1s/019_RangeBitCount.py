def rangeBitCount(a, b):    
    '''
    You are given two numbers a and b where 0 ≤ a ≤ b. 
    Imagine you construct an array of all the integers from a to b inclusive. 
    You need to count the number of 1s in the binary representations of all 
    the numbers in the array.
    '''
    return sum([bin(i).count('1') for i in range(a, b+1)])


print(rangeBitCount(2, 7))
print(rangeBitCount(0, 10))