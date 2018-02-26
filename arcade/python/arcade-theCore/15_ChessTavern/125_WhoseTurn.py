'''
Imagine a standard chess board with only two white and two black knights placed in their standard starting positions: the white knights on b1 and g1; the black knights on b8 and g8.



There are two players: one plays for white, the other for black. During each move, the player picks one of his knights and moves it to an unoccupied square according to standard chess rules. Thus, a knight on d5 can move to any of the following squares: b6, c7, e7, f6, f4, e3, c3, and b4, as long as it is not occupied by either a friendly or an enemy knight.



The players take turns in making moves, starting with the white player. Given the configuration p of the knights after an unspecified number of moves, determine whose turn it is.

Example

For p = "b1;g1;b8;g8", the output should be
whoseTurn(p) = true.

The configuration corresponds to the initial state of the game. Thus, it's white's turn.
'''
def whoseTurn(conf):
    sp = conf.split(";")
    knights = [indexPos(x) for x in sp]
    parities = [getParity(x) for x in knights]
    # if our parity is 0 is white's turn, if the parity is 1 is black's turn
    return sum(parities) % 2 == 0
    
def indexPos(p):
    y = int(p[1])-1
    x = ord(p[0])-ord('a')
    return x,y

def getParity(p):
    # parity is 0 if we are in a black square, 1 if in a white square
    return (p[0] + (p[1]%2)) % 2

