def isSmooth(arr):
    '''
    We define the middle of the array arr as follows:
    
    if arr contains an odd number of elements, its middle is the element whose index number 
        is the same when counting from the beginning of the array and from its end;

    if arr contains an even number of elements, its middle is the sum of the two elements 
        whose index numbers when counting from the beginning and from the end of the array differ by one.

    An array is called smooth if its first and its last elements are equal to one another and to the middle. 
    
    Given an array arr, determine if it is smooth or not.

    '''
    length = len(arr)
    if length % 2 == 1:
        middle = arr[length//2]
    else:
        middle = arr[length//2] + arr[length//2 - 1]
        
    return arr[0] == middle and arr[length-1] == middle


print(isSmooth([7, 2, 2, 5, 10, 7]))
print(isSmooth([-5, -5, 10]))
print(isSmooth([4, 2]))
print(isSmooth([45, 23, 12, 33, 12, 453, -234, -45]))