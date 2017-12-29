def stringsConstruction(a, b):
    '''
    How many strings equal to a can be constructed using letters from the string b? Each letter can be used only once and in one string only.

Example

For a = "abc" and b = "abccba", the output should be
stringsConstruction(a, b) = 2.

We can construct 2 strings a with letters from b.
    '''
    continueSearching = True
    r = 0
    while continueSearching:
        for i in a:
            j = 0
            while j < len(b) and i != b[j]:
                j+=1
            if j >= len(b):
                return r
            b = b[:j] + b[j+1:]
        r += 1
    return r
                