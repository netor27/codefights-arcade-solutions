def deleteDigit(n):
    '''
    Given some integer, find the maximal number you can obtain by deleting exactly one digit of the given number.
    '''
    l = [int(i) for i in str(n)]
    foundBigger = False
    i = 0
    while not foundBigger and i < len(l)-1:
        if l[i] < l[i+1]:
            foundBigger = True
        else:
            i+=1
    
    withoutMin = l[:i] + l[i+1:]    
    st = ''.join([str(j) for j in withoutMin])
    return int(st)
    