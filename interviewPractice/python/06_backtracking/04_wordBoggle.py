''''
Boggle is a popular word game in which players attempt to find words in sequences of adjacent letters on a rectangular board.

Given a two-dimensional array board that represents the character cells of the Boggle board and an array of unique strings words, find all the possible words from words that can be formed on the board.

Note that in Boggle when you're finding a word, you can move from a cell to any of its 8 neighbors, but you can't use the same cell twice in one word.

Example

For

board = [
    ['R', 'L', 'D'],
    ['U', 'O', 'E'],
    ['C', 'S', 'O']
]
and words = ["CODE", "SOLO", "RULES", "COOL"], the output should be
wordBoggle(board, words) = ["CODE", "RULES"].

Example

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.char board

A two-dimensional array of uppercase English characters representing a rectangular Boggle board.

Guaranteed constraints:
2 ≤ board.length ≤ 4,
2 ≤ board[i].length ≤ 4,
'A' ≤ board[i][j] ≤ 'Z'.

[input] array.string words

An array of unique English words composed only of uppercase English characters.

Guaranteed constraints:
0 ≤ words.length ≤ 100,
2 ≤ words[i].length ≤ 16,
'A' ≤ words[i][j] ≤ 'Z'.

[output] array.string

Words from words that can be found on the Boggle board without duplicates and sorted lexicographically in ascending order.


''''

def wordBoggle(board, words):
    words = set(words)
    if len(words) == 0:
        return []
    
    result = set()
    maxWordLength = max([len(x) for x in words])
    n = len(board)
    m = len(board[0])
    
    def searchWord(x, y, visited, accum):
        if x < 0 or x >= n or y < 0 or y >= m:
            return
        
        if visited[x][y]:
            return
        
        if len(accum) >= maxWordLength:
            return
        
        accum += board[x][y]
        if accum in words:
            result.add(accum)
            
        visited[x][y] = True
        
        for i in range(-1,2):
            for j in range(-1,2):
                newVisited = [[x for x in y] for y in visited]
                searchWord(x + i, y + j, newVisited, accum)
    
    for x in range(n):
        for y in range(m):
            aux = [[False for _ in range(m)] for _ in range(n)]
            searchWord(x, y, aux, "")
    
    #print(result)
    return sorted(result)
    
    
    
        
        
        
        
        