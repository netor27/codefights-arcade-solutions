'''
Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
areSimilar(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
areSimilar(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
areSimilar(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.
'''
def areSimilar(a, b):
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