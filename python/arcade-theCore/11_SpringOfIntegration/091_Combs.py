'''
Miss X has only two combs in her possession, both of which are old and miss a tooth or two. She also has many purses of different length, in which she carries the combs. The only way they fit is horizontally and without overlapping. Given teeth' positions on both combs, find the minimum length of the purse she needs to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.
Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
combs(comb1, comb2) = 5.

Although it is possible to place the combs like on the first picture, the best way to do this is either picture 2 or picture 3.


'''
def combs(comb1, comb2):
    n1, n2 = len(comb1), len(comb2)
    res = n1 + n2
    m1, m2 = mask(comb1), mask(comb2)
    
    for i in range(n1 + 1):
        if (m2 << i) & m1 == 0:
            temp = max(n2 + i, n1)
            if temp < res:
                res = temp
    
    for i in range(n2 + 1):
        if (m1 << i) & m2 == 0:
            temp = max(n1 + i, n2)
            if temp < res:
                res = temp
    
    return res
    
    
def mask(s):
    r = 0
    for c in s:
        digit = 0
        if c == '*':
            digit = 1
        r = (r << 1) + digit
    return r

