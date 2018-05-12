''''
ote: Try to solve this task in-place (with O(1) additional memory), since this is what you'll be asked to do during an interview.

You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer a

Guaranteed constraints:
1 ≤ a.length ≤ 100,
a[i].length = a.length,
1 ≤ a[i][j] ≤ 104.

[output] array.array.integer
''''

def rotateImage(a):
    n = len(a)
    if n <= 1:
        return a
    
    layers = n // 2
    
    for i in range(layers):
        bound = n-1-(i*2)
        for j in range(bound):
            
            # save top
            top = a[i][i+j]
            
            # left to top
            a[i][i+j] = a[n-1-i-j][i]
            
            # bottom to left
            a[n-1-i-j][i] = a[n-1-i][n-1-i-j]
            
            # right to bottom
            a[n-1-i][n-1-i-j] = a[i+j][n-1-i]
            
            # top to right
            a[i+j][n-1-i] = top
            
    return a
            
            