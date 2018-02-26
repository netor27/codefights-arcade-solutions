'''
Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.



Example

For cell = "a1", the output should be
chessKnightMoves(cell) = 2.



For cell = "c2", the output should be
chessKnightMoves(cell) = 6.


'''

def chessKnightMoves(cell):
    possibleMoves = [(-2,1), (-1,2),
                     (1,2),  (2,1),
                     (2,-1), (1,-2),
                     (-1,-2),(-2,-1)]
    pos = getIndexPosFromChessPos(cell)    
    return sum([1 for x in possibleMoves if validMove(pos, x)])

def getIndexPosFromChessPos(p):
    y = int(p[1])-1
    x = ord(p[0])-ord('a')
    return x,y

def validMove(pos, move):
    x = pos[0] + move[0]
    y = pos[1] + move[1]    
    return x >= 0 and x < 8 and y >= 0 and y < 8