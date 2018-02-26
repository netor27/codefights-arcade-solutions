'''
In the Land Of Chess, bishops don't really like each other. In fact, when two bishops happen to stand on the same diagonal, they immediately rush towards the opposite ends of that same diagonal.

Given the initial positions (in chess notation) of two bishops, bishop1 and bishop2, calculate their future positions. Keep in mind that bishops won't move unless they see each other along the same diagonal.

Example

For bishop1 = "d7" and bishop2 = "f5", the output should be
bishopDiagonal(bishop1, bishop2) = ["c8", "h3"].



For bishop1 = "d8" and bishop2 = "b5", the output should be
bishopDiagonal(bishop1, bishop2) = ["b5", "d8"].

The bishops don't belong to the same diagonal, so they don't move.

'''

def bishopDiagonal(bishop1, bishop2):
    print(bishop1, bishop2)
    b1 = indexPos(bishop1)
    b2 = indexPos(bishop2)
    
    if not abs(b1[1]-b2[1]) == abs(b1[0]-b2[0]):
        return sorted([bishop1, bishop2])
    
    move1 = (b1[0]-b2[0], b1[1]-b2[1])
    move2 = (b2[0]-b1[0], b2[1]-b1[1])
    
    return sorted([chessPos(getEndPos(b1, move1)), chessPos(getEndPos(b2, move2))])
    
    

def indexPos(p):
    y = int(p[1])-1
    x = ord(p[0])-ord('a')
    return x,y

def chessPos(p):
    y = str(p[1]+1)
    x = chr(p[0] + ord('a'))
    return x+y

def getEndPos(p, move):
    if move[0] == 0 or move[1] == 0:
        return p    
    
    move = (move[0]//abs(move[0]), move[1]//abs(move[1]))
    newPos = (p[0]+move[0], p[1]+move[1])
    
    while newPos[0] >= 0 and newPos[0]< 8 and newPos[1] >= 0 and newPos[1] < 8:
        p = newPos
        newPos = (p[0]+move[0], p[1]+move[1])
    
    return p
