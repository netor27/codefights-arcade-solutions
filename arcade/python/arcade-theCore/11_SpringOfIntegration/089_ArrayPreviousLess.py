'''
Given array of integers, for each position i, search among the previous positions for the last (from the left) position that contains a smaller value. Store this value at position i in the answer. If no such value can be found, store -1 instead.

Example

For items = [3, 5, 2, 4, 5], the output should be
arrayPreviousLess(items) = [-1, 3, -1, 2, 4].
'''
def arrayPreviousLess(items):
    result = [-1] * len(items)
    for i in range(len(items)):        
        for j in range(i):
            if items[i-j-1] < items[i]:
                result[i] = items[i-j-1]
                break
            if result[i-j-1] == -1:
                break
    return result