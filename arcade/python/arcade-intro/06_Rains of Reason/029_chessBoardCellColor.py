def chessBoardCellColor(cell1, cell2):
    '''
    Given two cells on the standard chess board, determine whether they have the same color or not.
    '''
    pos1, pos2 = list(cell1), list(cell2)
    return isWhiteColor(pos1) == isWhiteColor(pos2)

def isWhiteColor(pos):    
    # we substract 64 to get A as 0, B as 1, and so on
    col = ord(pos[0]) - 64 
    row = int(pos[1])    
    pos = col + (row % 2)        
    return pos % 2 != 0

print(chessBoardCellColor("A1", "C3"))
print(chessBoardCellColor("A2", "C3"))