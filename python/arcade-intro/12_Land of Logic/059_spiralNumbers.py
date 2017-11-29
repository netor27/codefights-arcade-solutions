from pprint import pprint

def spiralNumbers(n):
    '''
    Construct a square matrix with a size N × N containing integers from 1 to N * N 
    in a spiral order, starting from top-left and in clockwise direction.
    '''
    # initialize matrix with zeros
    res = [[0 for _ in range(n)] for _ in range(n)]
    count = 1
    numSquares = n // 2 + 1
    for i in range(numSquares):
        # set top row
        for x in range(i, n-i-1):
            res[i][x] = count
            count += 1
        
        # set right column
        for x in range(i, n-i-1):
            res[x][n-i-1] = count
            count+=1
        
        # set bottom row
        for x in range(i, n-i-1):
            res[n-i-1][n-x-1] = count
            count += 1
        
        # set left column
        for x in range(i,n-i-1):
            res[n-x-1][i]= count
            count += 1
    
    # setting middle cell
    if n % 2 == 1:
        res[numSquares-1][numSquares-1] = count
    return res    

print("n=",5)
pprint(spiralNumbers(5))

print("n=",6)
pprint(spiralNumbers(6))

print("n=",7)
pprint(spiralNumbers(7))