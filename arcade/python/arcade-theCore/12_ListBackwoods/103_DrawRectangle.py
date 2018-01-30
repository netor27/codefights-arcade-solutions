'''
You are implementing a command-line version of the Paint app. Since the command line doesn't support colors, you are using different characters to represent pixels. Your current goal is to support rectangle x1 y1 x2 y2 operation, which draws a rectangle that has an upper left corner at (x1, y1) and a lower right corner at (x2, y2). Here the x-axis points from left to right, and the y-axis points from top to bottom.

Given the initial canvas state and the array that represents the coordinates of the two corners, return the canvas state after the operation is applied. For the details about how rectangles are painted, see the example.

Example

For

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
and rectangle = [1, 1, 4, 3], the output should be


drawRectangle(canvas, rectangle) = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
                                    ['a', '*', '-', '-', '*', 'a', 'a', 'a'],
                                    ['a', '|', 'a', 'a', '|', 'a', 'a', 'a'],
                                    ['b', '*', '-', '-', '*', 'b', 'b', 'b'],
                                    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
Note that rectangle sides are depicted as -s and |s, asterisks (*) stand for its corners and all of the other "pixels" remain the same. Color in the example is used only for illustration.
'''

def drawRectangle(canvas, rectangle):
    corners = getRectangeCorners(rectangle)
    # setting corners
    for c in corners:
        canvas[c[0]][c[1]] = "*"
    # setting | sides
    for i in range(corners[0][0]+1, corners[2][0]):
        canvas[i][corners[0][1]] = "|"
        canvas[i][corners[1][1]] = "|"
    # setting - sides
    for i in range(corners[0][1]+1, corners[1][1]):
        canvas[corners[0][0]][i] = "-"
        canvas[corners[3][0]][i] = "-"
    
    return canvas
    

def getRectangeCorners(r):
    topLeft = (r[1], r[0])
    topRight = (r[1], r[2])
    bottomLeft = (r[3], r[0])
    bottomRight = (r[3], r[2])
    return topLeft, topRight, bottomLeft, bottomRight


