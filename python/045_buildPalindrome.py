def buildPalindrome(st):
    '''
    Given a string, find the shortest possible string which can be achieved by adding 
    characters to the end of initial string to make it a palindrome.
    '''
    n = len(st)
    rev = st[::-1]
    depth = 0
    while depth < n and st[depth:] != rev[:n-depth]:
        depth += 1    
    return st + rev [n-depth:]