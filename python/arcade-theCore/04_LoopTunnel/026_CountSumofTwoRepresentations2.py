def countSumOfTwoRepresentations2(n, l, r):
    '''
    Given integers n, l and r, find the number of ways to represent n as a sum of two integers A and B such that l ≤ A ≤ B ≤ r.

    '''
    middle = n // 2
    if l <= middle <= r : 
        diffL = abs(middle-l)
        diffR = abs(middle-r)
        return min(diffL, diffR) + (n+1) % 2
    return 0

    print(countSumOfTwoRepresentations2(6,2,4))
    print(countSumOfTwoRepresentations2(10,9,11))