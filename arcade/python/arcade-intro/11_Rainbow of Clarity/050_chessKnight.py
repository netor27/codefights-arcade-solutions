def chessKnight(cell):
    '''
    Given a position of a knight on the standard chessboard, find the number 
    of different moves the knight can perform.
    
    The knight can move to a square that is two squares horizontally and one 
    square vertically, or two squares vertically and one square horizontally 
    away from it. The complete move therefore looks like the letter L. 
    '''
    # get the current position 0 based
    x = ord(cell[0])-97
    y = int(cell[1])-1
    
    # get the positions of possible movements
    movs2 = [-2, 2]
    movs1 = [-1, 1]
    
    n = 0
    for i in movs2:
        for j in movs1:
            if isValidPosition(x + i, y + j):
                n += 1
            if isValidPosition(x + j, y + i):
                n += 1
    return n
    
    
def isValidPosition(x, y):
    return 0 <= x < 8 and 0 <= y < 8