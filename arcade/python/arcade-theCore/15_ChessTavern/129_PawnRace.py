def indexPos(p):
    x = int(p[1])-1
    y = ord(p[0])-ord('a')
    return (x, y)


def pawnRace(white, black, toMove):
    isBlackMove = True if toMove == "b" else False
    white = indexPos(white)
    black = indexPos(black)
    print("white", white, "black", black, "blackMoveNext" if isBlackMove else "whiteMoveNext")

    matchFinished = False
    while not matchFinished:
        matchFinished, result, white, black = movePiece(white, black, isBlackMove)
        isBlackMove = not isBlackMove
        print("white", white, "black", black, "blackMoveNext" if isBlackMove else "whiteMoveNext")

    print(result)
    return result


def movePiece(white, black, isBlackMove):
    if isBlackMove:
        if black[0] == 0:
            # check finished moving
            matchFinished, result = True, "black"
            print("black reached end line, black wins!")
        elif white == addToPos(black, (-1,0)):
            # check for draw
            matchFinished, result = True, "draw"
            print("black faces white, draw")
        elif white == addToPos(black, (-1,1)) or white == addToPos(black, (-1,-1)):
            # we kill the other pawn
            print("black killed white pawn in {} from {}".format(white, black))
            black = white
            white = None
            matchFinished, result = True, "black"
        elif black[0] == 6 and white != (addToPos(black,(-2,0))):
            # check for 2 spaces movement
            # move 2 only if we don't hit white, if we hit white, we should move only 1 space
            if white == addToPos(black,(-3,1)) or white == addToPos(black,(-3,-1)):
                # if the double movement make us loose, only move one
                black = addToPos(black, (-1,0))
            else:
                black = addToPos(black, (-2,0))
            matchFinished, result = False, None
        else:
            black = addToPos(black, (-1,0))
            matchFinished, result = False, None

        return matchFinished, result, white, black
    else:
        if white[0] == 7:
            # check finished moving
            matchFinished, result = True, "white"
            print("white reached end line, white wins!")
        elif black == addToPos(white, (1,0)):
            # check for draw
            matchFinished, result = True, "draw"
            print("black faces white, draw")
        elif black == addToPos(white, (1,1)) or black == addToPos(white, (1,-1)):
            # we kill the other pawn
            print("white killed black pawn in {} from {}".format(black, white))
            white = black
            black = None
            matchFinished, result = True, "white"
        elif white[0] == 1 and black != (addToPos(white,(2,0))):
            # check for 2 spaces movement
            # move 2 only if we don't hit black, if we hit black, we should move only 1 space
            if black == addToPos(white,(3,1)) or black == addToPos(white,(3,-1)):
                # if the double movement make us loose, only move one
                white = addToPos(white, (1,0))
            else:
                white = addToPos(white, (2,0))
            matchFinished, result = False, None
        else:
            white = addToPos(white, (1,0))
            matchFinished, result = False, None

        return matchFinished, result, white, black


def addToPos(cell, delta):
    return (cell[0]+delta[0], cell[1]+delta[1])