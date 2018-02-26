'''
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:


Example

For bishop = "a1" and pawn = "c3", the output should be
bishopAndPawn(bishop, pawn) = true.



For bishop = "h1" and pawn = "h3", the output should be
bishopAndPawn(bishop, pawn) = false.


'''
def bishopAndPawn(bishop, pawn):
    # get matrix index position
    x1,y1 = getIndexPosFromChessPos(bishop)
    x2,y2 = getIndexPosFromChessPos(pawn)
    
    # to check diagonally, abs(y1-y2) == abs(x1-x2)
    return abs(y1-y2) == abs(x1-x2)

def getIndexPosFromChessPos(p):
    y = int(p[1])-1
    x = ord(p[0])-ord('a')
    return x,y