'''
You have a rectangular white board with some black cells. The black cells create a connected black figure, i.e. it is possible to get from any black cell to any other one through connected adjacent (sharing a common side) black cells.

Find the perimeter of the black figure assuming that a single cell has unit length.

It's guaranteed that there is at least one black cell on the table.

Example

For

matrix = [[false, true,  true ],
          [true,  true,  false],
          [true,  false, false]]
the output should be
polygonPerimeter(matrix) = 12.



For

matrix = [[true, true,  true],
          [true, false, true],
          [true, true,  true]]
the output should be
polygonPerimeter(matrix) = 16.


'''    
def polygonPerimeter(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == False:
                continue
                
            left = j-1
            if left < 0:
                res += 1
            elif matrix[i][left] == False:
                res += 1
            
            right = j+1
            if right >= len(matrix[i]):
                res += 1
            elif matrix[i][right] == False:
                res += 1
            
            up = i-1
            if up < 0:
                res += 1
            elif matrix[up][j] == False:
                res += 1
                
            down = i+1
            if down >= len(matrix):
                res += 1
            elif matrix[down][j] == False:
                res += 1
    return res
            
                