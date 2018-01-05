def createArray(size):
    '''
    Given an integer size, return array of length size filled with 1s.
    '''
    return [1 for i in range(size)]

print(createArray(4))
print(createArray(40))
print(createArray(400))