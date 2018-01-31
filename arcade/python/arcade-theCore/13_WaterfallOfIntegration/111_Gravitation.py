'''
You are given a vertical box divided into equal columns. Someone dropped several stones from its top through the columns. Stones are falling straight down at a constant speed (equal for all stones) while possible (i.e. while they haven't reached the ground or they are not blocked by another motionless stone). Given the state of the box at some moment in time, find out which columns become motionless first.

Example

For

rows = ["#..##",
        ".##.#",
        ".#.##",
        "....."]
the output should be gravitation(rows) = [1, 4].
'''


def gravitation(rows):
    matrix = [list(s) for s in rows]
    while(True):        
        #check the current state before doing a motion
        print(matrix)
        withoutMotion = []
        for i in range(len(matrix[0])):
            if not stillHaveMotion(matrix,i):
                withoutMotion.append(i)
        if len(withoutMotion) > 0:
            return withoutMotion
        
        # do a motion
        for i in range(len(matrix[0])):
            doColMotion(matrix, i)



def doColMotion(rows, col):
    n = len(rows)
    for i in range(n):
        if rows[n-1-i][col] == "#" or n-2-i < 0:
            continue
        
        if rows[n-2-i][col] == "#":
            rows[n-1-i][col] = rows[n-2-i][col]
            rows[n-2-i][col] = "."
        

def stillHaveMotion(rows, col):
    res = False
    n = len(rows)
    hasSpace = False
    for i in range(n):
        if rows[n-1-i][col] == ".":
            hasSpace = True
        elif hasSpace:
            res = True
    return res