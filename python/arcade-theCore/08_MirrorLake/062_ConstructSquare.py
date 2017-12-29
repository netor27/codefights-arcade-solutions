from collections import Counter

def constructSquare(s):
    '''
    Given a string consisting of lowercase English letters, find the largest square number which can be obtained by reordering the string's characters and replacing them with any digits you need (leading zeros are not allowed) where same characters always map to the same digits and different characters always map to different digits.

If there is no solution, return -1.

Example

For s = "ab", the output should be
constructSquare(s) = 81.
The largest 2-digit square number with different digits is 81.
For s = "zzz", the output should be
constructSquare(s) = -1.
There are no 3-digit square numbers with identical digits.
For s = "aba", the output should be
constructSquare(s) = 900.
It can be obtained after reordering the initial string into "baa" and replacing "a" with 0 and "b" with 9.
    '''
    # get the possible squares and sort them
    squares = getSquaresWithLength(len(s))  
    
    # count the ocurrences of letters in the string, and sort them
    ocurrences = sorted(Counter(s).values())
    
    # try with every possible square from the biggest to the smallest
    n = len(squares)
    for i in range(n):
        temp = sorted(Counter(str(squares[n-1-i])).values())        
        if ocurrences == temp:
            return squares[n-1-i]
    return -1
    
    
def getSquaresWithLength(length):
    res = []
    i = 1
    s = pow(i, 2)
    while (len(str(s)) <= length):
        if len(str(s)) == length:
            res.append(s)
        i += 1
        s = pow(i, 2)
    return res
    