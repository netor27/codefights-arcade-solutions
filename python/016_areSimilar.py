def areSimilar(a, b):
    '''
    Two arrays are called similar if one can be obtained from another by swapping at most one pair
    of elements in one of the arrays.
    Given two arrays a and b, check whether they are similar.'''
    
    if len(a) != len(b):
        raise "The arrays must be of the same length"
    
    n = len(a)    
    diff = []
    numOfErrors = 0
    for i in range(n):
        if a[i] != b[i]:
            numOfErrors += 1
            if numOfErrors == 1:
                diff.append(a[i])
                diff.append(b[i])
            elif numOfErrors == 2:
                # check if swapping works
                if diff[0] != b[i] or diff[1] != a[i]:
                    return False
            else:
                return False
    return True

print(areSimilar([1, 2, 3], [1, 2, 3]))
print(areSimilar([1, 2, 3], [2, 1, 3]))
print(areSimilar([1, 2, 2], [2, 1, 1]))
