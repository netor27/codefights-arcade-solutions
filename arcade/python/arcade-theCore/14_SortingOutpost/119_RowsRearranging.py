'''
Given a rectangular matrix of integers, check if it is possible to rearrange its rows in such a way that all its columns become strictly increasing sequences (read from top to bottom).

Example

For

matrix = [[2, 7, 1], 
          [0, 2, 0], 
          [1, 3, 1]]
the output should be
rowsRearranging(matrix) = false;

For

matrix = [[6, 4], 
          [2, 2], 
          [4, 3]]
the output should be
rowsRearranging(matrix) = true.
'''

import operator
import functools

def rowsRearranging(matrix):
    width = len(matrix[0])
    
    for i in range(width):
        sortedMatrix = sorted(matrix, key=operator.itemgetter(i))
        if all(map(functools.partial(isRowOrdered, matrix=sortedMatrix), [x for x in range(width)])):
            return True
    return False
        

def isRowOrdered(row, matrix):
    for i in range(len(matrix)-1):
        if matrix[i][row] >= matrix[i+1][row]:
            return False
    return True
        
        
                    

