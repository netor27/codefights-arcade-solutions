import itertools
import timeit

def crosswordFormation(words):    
    w1, w2, w3, w4 = words
    r = 0
    # sum the possible combinations if we pair w1 and w2 in opposite sides and w3 with w4. Then multiply it by 8 (8 possible rotations of the square)
    #r += sumOfCombinations(w1, w3, w2, w4) * 8

    # sum the possible combinations if we pair w1 and w3 in opposite sides and w2 with w4. Then multiply it by 8 (8 possible rotations of the square)
    #r += sumOfCombinations(w1, w2, w3, w4) * 8

    # sum the possible combinations if we pair w2 and w3 in opposite sides and w1 with w4. Then multiply it by 8 (8 possible rotations of the square)
    #r += sumOfCombinations(w2, w1, w3, w4) * 8

    r = 0
    for w in itertools.permutations(words):
        r += sumOfCombinations(*w)
    return r


def sumOfCombinations(left, up, right, bottom):
    lset = set(left)
    rset = set(right)
    uset = set(up)
    bset = set(bottom)
    r = 0
    for l1 in range(len(left) - 2):
        if left[l1] in uset:            
            for u1 in range(len(up) - 2):
                if left[l1] == up[u1]:
                    # we found a letter that match between left and up
                    # now, check from u1+2 till the end to find matches with right
                    for u2 in range(u1 + 2, len(up)):
                        if up[u2] in rset:
                            for r1 in range(len(right) - 2):
                                if up[u2] == right[r1]:
                                    # we found a letter that match between up and right
                                    # now, check from r1+2 till the end to find matches with bottom
                                    for r2 in range(r1 + 2, len(right)):
                                        if right[r2] in bset:
                                            for b1 in range(u2 - u1, len(bottom)):
                                                if right[r2] == bottom[b1]:
                                                    # we found a letter that matches with bottom
                                                    # now, check if by positioning bottom like this, it matches with left
                                                    # first check if the positioning of b at least covers the distance of upper
                                                    width = u2 - u1
                                                    height = r2 - r1
                                                    if b1 - width >= 0 and l1 + height < len(left):
                                                        if left[l1 + height] == bottom[b1 - width]:
                                                            r += 1
    return r




def test():
# print(crosswordFormation(["crossword", 
#  "square", 
#  "formation", 
#  "something"]))
    result = crosswordFormation(["aaaaaaaaaaaaaa", 
         "aaaaaaaaaaaaab", 
         "aaaaaaaaaaaaca", 
         "aaaaaaaaaaadaa"])
    print(result)

from __main__ import test
print(timeit.timeit(test, number=1))
