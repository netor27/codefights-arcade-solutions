'''
n the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

minesweeper(matrix) = [[1, 2, 1],
                       [2, 1, 1],
                       [1, 1, 1]]       

'''
def minesweeper(matrix):
    
    # initialize our result matrix
    mineCount = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]
    
    # iterate through the matrix
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                # we found a mine
                sumOneToNeighbors(mineCount, row, col)
    return mineCount                


def sumOneToNeighbors(mineCount, row, col):
    # Top row
    if row-1 >= 0:
        mineCount[row-1][col] += 1
        if col-1 >= 0:
            mineCount[row-1][col-1] += 1
        if col+1 < len(mineCount[row]):    
            mineCount[row-1][col+1] += 1
    
    # Same row
    if col-1 >= 0:
        mineCount[row][col-1] += 1
    if col+1 < len(mineCount[row]):    
        mineCount[row][col+1] += 1
        
    # Bottom row
    if row+1 < len(mineCount):                
        mineCount[row+1][col] += 1
        if col-1 >= 0:
            mineCount[row+1][col-1] += 1
        if col+1 < len(mineCount[row]):    
            mineCount[row+1][col+1] += 1

print(minesweeper([[True, False, False],
          [False, True, False],
          [False, False, False]]))