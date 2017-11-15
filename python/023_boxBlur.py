def boxBlur(image):
    '''
    Apply the box blur algorithm to the photo to hide its content.
    
    The pixels in the input image are represented as integers. 
    The algorithm distorts the input image in the following way: 
    Every pixel x in the output image has a value equal to the average 
    value of the pixel values from the 3 × 3 square that has its center at x,
    including x itself. All the pixels on the border of x are then removed.
    
    Return the blurred image as an integer, with the fractions rounded down.
    '''
    result = []
    for row in range(1, len(image)-1):
        result.append([])
        for col in range(1, len(image[row])-1):
            result[row-1].append(getBoxAverage(image, row, col))
    return result


def getBoxAverage(image, row, col):
    sum = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            sum += image[i][j]    
    return sum // 9

print(boxBlur([[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]))

print(boxBlur( [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]))