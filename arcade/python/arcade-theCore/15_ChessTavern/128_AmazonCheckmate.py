'''
An amazon (also known as a queen+knight compound) is an imaginary chess piece that can move like a queen or a knight (or, equivalently, like a rook, bishop, or knight). The diagram below shows all squares which the amazon attacks from e4 (circles represent knight-like moves while crosses correspond to queen-like moves).



Recently you've come across a diagram with only three pieces left on the board: a white amazon, white king and black king. It's black's move. You don't have time to determine whether the game is over or not, but you'd like to figure it out in your head. Unfortunately, the diagram is smudged and you can't see the position of the black's king, so it looks like you'll have to check them all.

Given the positions of white pieces on a standard chessboard, determine the number of possible black king's positions such that:

it's checkmate (i.e. black's king is under amazon's attack and it cannot make a valid move);
it's check (i.e. black's king is under amazon's attack but it can reach a safe square in one move);
it's stalemate (i.e. black's king is on a safe square but it cannot make a valid move);
black's king is on a safe square and it can make a valid move.
Note that two kings cannot be placed on two adjacent squares (including two diagonally adjacent ones).

Example

For king = "d3" and amazon = "e4", the output should be
amazonCheckmate(king, amazon) = [5, 21, 0, 29].



Red crosses correspond to the checkmate positions, orange pluses refer to checks and green circles denote safe squares.

For king = "a1" and amazon = "g5", the output should be
amazonCheckmate(king, amazon) = [0, 29, 1, 29].



Stalemate position is marked by a blue square.
'''

kingMoves = [(-1,-1), (-1,0), (-1,1),
                 (0,-1), (0,1),
                 (1,-1), (1,0), (1,1)]

knightMoves = [(-2,1), (-1,2),
                     (1,2),  (2,1),
                     (2,-1), (1,-2),
                     (-1,-2),(-2,-1)]

memoizationAttack = dict()

def indexPos(p):
    x = int(p[1])-1
    y = ord(p[0])-ord('a')
    return (x, y)


def validPosition(cell, king, amazon):
    if cell == king or cell == amazon:
        return False
    for k in kingMoves:
        if cell[0] == k[0]+king[0] and cell[1] ==k[1]+king[1]:
            return False
    return True


def canBeAttacked(cell, king, amazon):
    if cell in memoizationAttack:
        return  memoizationAttack[cell]
    
    # check king moves
    for k in kingMoves:
        if cell[0] == k[0]+king[0] and cell[1] == k[1]+king[1]:
            memoizationAttack[cell] = True
            return True
    
    # if with this attack we kill the amazon we shouldn't check for the amazon's moves
    if cell == amazon:
        memoizationAttack[cell] = False
        return False
    
    # check amazon moves    
    # horizontal
    if cell[0] == amazon[0]:
        # check the white king is not in our way
        if king[0] != amazon[0]:
            memoizationAttack[cell] = True
            return True
        elif ((king[1] < cell[1]  and king[1] < amazon[1]) or 
             (king[1] > cell[1]  and king[1] > amazon[1])):
            memoizationAttack[cell] = True
            return True
    
    # vertical
    if cell[1] == amazon[1]:
        # check the white king is not in our way
        if king[1] != amazon[1]:
            memoizationAttack[cell] = True
            return True
        elif ((king[0] < cell[0]  and king[0] < amazon[0]) or 
             (king[0] > cell[0]  and king[0] > amazon[0])):
            memoizationAttack[cell] = True
            return True
        
        
    # diagonal
    if abs(cell[0]-amazon[0]) == abs(cell[1]-amazon[1]):
        print(cell, "same diagonal")
        # check the white king is not in our way
        if (abs(cell[0]-king[0]) != abs(cell[1]-king[1]) or
            abs(amazon[0]-king[0]) != abs(amazon[1]-king[1])):
            print(cell, "King is not in the same diagonal, a hit")
            memoizationAttack[cell] = True
            return True
        
        if ((king[0] < cell[0] and king[0] < amazon[0]) or 
            (king[0] > cell[0] and king[0] > amazon[0])):
            print(cell, "king is not in the middle")
            memoizationAttack[cell] = True
            return True
        
        print(cell, "same diagonal, but king is in the middle")
        
    # check amazon bishop-like moves
    for k in knightMoves:
        if cell[0] == k[0] + amazon[0] and cell[1] == k[1] + amazon[1]:
            memoizationAttack[cell] = True
            return True
        
    memoizationAttack[cell] = False
    return False


def haveValidMove(cell, king, amazon):
    for k in kingMoves:
        newPos = (cell[0]+k[0], cell[1]+k[1])
        if 0 <= newPos[0] < 8 and 0 <= newPos[1] < 8:
            if not canBeAttacked(newPos, king, amazon):
                return True
    return False


def amazonCheckmate(king, amazon):
    checkmate, check, stalemate, safe = 0, 0, 0, 0
    king = indexPos(king)
    amazon = indexPos(amazon)
    
    print("king", king)
    print("amazon", amazon)
    
    for row in range(8):
        for col in range(8):
            cell = (row,col)
            if validPosition(cell, king, amazon):
                if canBeAttacked(cell, king, amazon):
                    # do something
                    if haveValidMove(cell, king, amazon):
                        print("====",cell, "is check")
                        check += 1
                    else:
                        print("====",cell, "is checkmate")
                        checkmate += 1
                elif haveValidMove(cell, king, amazon):
                    print("====",cell, "is safe")
                    safe += 1
                else:
                    print("====",cell, "is stalemate")
                    stalemate += 1
            else:
                print("invalid position for ", cell)
    return [checkmate, check, stalemate, safe]
                    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
    

