def chessNotation(notation):
    matrix = getMatrixFromNotation(notation)
    rotatedMatrix = list(rotate(matrix, 90))
    res = getNotationFromMatrix(rotatedMatrix)
    print(res)
    return res


def rotate(matrix, degree):
    if abs(degree) not in [0, 90, 180, 270, 360]:
        return matrix
    if degree == 0:
        return matrix
    elif degree > 0:
        return rotate(zip(*matrix[::-1]), degree-90)
    else:
        return rotate(zip(*matrix)[::-1], degree+90)



def getMatrixFromNotation(notation):
    rows = notation.split("/")
    matrix = []
    for r in rows:
        row = []
        for piece in r:
            if piece.isdigit():
                row = row + ([None] * int(piece))
            else:
                row.append(piece)
        matrix.append(row)
    return matrix


def getNotationFromMatrix(matrix):
    notation = []
    for row in matrix:
        counter = 0
        for piece in row:
            if piece == None:
                counter += 1
            else:
                if counter > 0:
                    notation.append(str(counter))
                    counter = 0
                notation.append(piece)
        if counter > 0:
            notation.append(str(counter))
        notation.append("/")

    # join every char except the last diagonal "/"
    return "".join(notation[:-1])








