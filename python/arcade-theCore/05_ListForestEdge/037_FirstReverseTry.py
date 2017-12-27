def firstReverseTry(arr):
    '''
    Reversing an array can be a tough task, especially for a novice programmer. 
    Mary just started coding, so she would like to start with something basic at first. 
    Instead of reversing the array entirely, she wants to swap just its first and last elements.
    Given an array arr, swap its first and last elements and return the resulting array.
    '''
    if len(arr) <= 1:
        return arr
    
    temp = arr[0]
    arr[0] = arr[len(arr)-1]
    arr[len(arr)-1] = temp
    return arr
    