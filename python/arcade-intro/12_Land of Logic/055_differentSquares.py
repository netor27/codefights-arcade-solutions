def differentSquares(m):
    '''
    Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.
    '''
    mySet = set()
    for i in range(len(m)-1):
        for j in range(len(m[i])-1):
            hashable = "{}{}{}{}".format(m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1])
            mySet.add(hashable)
    return len(mySet)