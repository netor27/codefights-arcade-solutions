def sudoku(grid):
    # check columns    
    for col in range(9):
        if not validColumn(grid, col):
            print("Failed in column ", col)
            return False            
    # check rows
    for row in range(9):
        if not validRow(grid, row):
            print("Failed in row ", row)
            return False
    # check 3x3 squares    
    for x in range(3):
        for y in range(3):
            if not validSquare(grid, x*3, y*3):
                print("Failed in square ", x, y)
                return False
    return True


def validColumn(grid, col):
    nums = [0 for _ in range(9)]
    for i in range(9):
        if nums[grid[i][col]-1] > 0:
            return False
        nums[grid[i][col]-1] = 1   
    return True

    
def validRow(grid, row):
    nums = [0 for _ in range(9)]
    for i in range(9):
        if nums[grid[row][i]-1] > 0:
            return False
        nums[grid[row][i]-1] = 1  
    return True
            
    
def validSquare(grid, x, y):
    nums = [0 for _ in range(9)]
    for i in range(3):
        for j in range(3):
            if nums[grid[x+i][y+j]-1] > 0:   
                return False
            nums[grid[x+i][y+j]-1] = 1
    return True


print(sudoku([  [1,3,2,5,4,6,9,8,7], 
                [4,6,5,8,7,9,3,2,1], 
                [7,9,8,2,1,3,6,5,4], 
                [9,2,1,4,3,5,8,7,6], 
                [3,5,4,7,6,8,2,1,9], 
                [6,8,7,1,9,2,5,4,3], 
                [5,7,6,9,8,1,4,3,2], 
                [2,4,3,6,5,7,1,9,8], 
                [8,1,9,3,2,4,7,6,5]]))