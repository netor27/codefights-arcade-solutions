def arrayPacking(a):
    '''
    You are given an array of up to four non-negative integers, each less than 256.

Your task is to pack these integers into one number M in the following way:

The first element of the array occupies the first 8 bits of M;
The second element occupies next 8 bits, and so on.
Return the obtained integer M.

Note: the phrase "first bits of M" refers to the least significant bits of M - the right-most bits of an integer. For further clarification see the following example.
    '''
    result = 0
    for i in a[::-1]: 
        result = result << 8
        result += i
    return result


print(arrayPacking([24, 85, 0]))
print(arrayPacking([23, 45, 39]))