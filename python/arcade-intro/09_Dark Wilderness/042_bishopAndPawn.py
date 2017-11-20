def bishopAndPawn(bishop, pawn):
    '''
    Given the positions of a white bishop and a black pawn on the standard chess board,
    determine whether the bishop can capture the pawn in one move.
    
    The bishop has no restrictions in distance for each move, but is limited to diagonal
    movement.
    '''
    # we use the ascii value, the numbers are not important as 
    # long as the int values for a to h are incremental by 1
    x1 = ord(bishop[0])
    y1 = int(bishop[1])
    x2 = ord(pawn[0])
    y2 = int(pawn[1])
    
    return abs(y1-y2) == abs(x1-x2)
