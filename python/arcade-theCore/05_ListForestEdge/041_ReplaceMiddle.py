def replaceMiddle(arr):
    '''
    We define the middle of the array arr as follows:
    
    if arr contains an odd number of elements, its middle is the element whose index number 
        is the same when counting from the beginning of the array and from its end;

    if arr contains an even number of elements, its middle is the sum of the two elements 
        whose index numbers when counting from the beginning and from the end of the array differ by one.
        
    Given array arr, your task is to find its middle, and, if it consists of two elements, replace 
    those elements with the value of middle. Return the resulting array as the answer.
    '''
    length = len(arr)
    if length % 2 == 1:
        return arr
    else:
        middle = arr[length//2] + arr[length//2 - 1]
        return arr[:length//2-1] + [middle] + arr[length//2+1:]