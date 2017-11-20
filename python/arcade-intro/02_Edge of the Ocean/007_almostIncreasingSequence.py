def almostIncreasingSequence(sequence):
    '''
    Given a sequence of integers as an array, determine whether 
    it is possible to obtain a strictly increasing sequence by 
    removing no more than one element from the array.
    '''
    j = analizeArray(sequence)
    if j == -1 :
        return True
    
    if analizeArray(sequence[j-1:j] + sequence[j+1:]) == -1:
        return True
    if analizeArray(sequence[j:j+1] + sequence[j+2:]) == -1:
        return True
    return False    

def analizeArray(array):
    '''Returns the first index of a pair of elements where the earlier element 
       is not less than the later elements. If no such pair exists, return -1.'''
    for i in range(len(array) - 1):
        if array[i] >= array[i + 1]:
            return i
    return -1    

print(almostIncreasingSequence([1, 3, 2, 1]))
print(almostIncreasingSequence([1, 3, 2]))