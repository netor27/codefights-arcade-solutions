'''
The longest diagonals of a square matrix are defined as follows:

the first longest diagonal goes from the top left corner to the bottom right one;
the second longest diagonal goes from the top right corner to the bottom left one.
Given a square matrix, your task is to reverse the order of elements on both of its longest diagonals.

Example

For

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
the output should be

reverseOnDiagonals(matrix) = [[9, 2, 7],
                              [4, 5, 6],
                              [3, 8, 1]]
'''
def reverseOnDiagonals(matrix):
        middle = len(matrix) // 2
        n = len(matrix) - 1
        for i in range(middle):
                # left to right
                aux = matrix[i][i]
                matrix[i][i] = matrix[n-i][n-i]
                matrix[n-i][n-i] = aux
        
                # right to left
                aux = matrix[i][n-i]
                matrix[i][n-i] = matrix[n-i][i]
                matrix[n-i][i] = aux
        return matrix