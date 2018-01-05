def messageFromBinaryCode(code):
    '''
    You are taking part in an Escape Room challenge designed specifically for programmers. 
    In your efforts to find a clue, you've found a binary code written on the wall behind a 
    vase, and realized that it must be an encrypted message. After some thought, your first 
    guess is that each consecutive 8 bits of the code stand for the character with the 
    corresponding extended ASCII code.
    
    Assuming that your hunch is correct, decode the message.
    '''
    x = 8
    parts = [code[i: i+x] for i in range(0,len(code),x)]
    chars = [chr(int(i,2)) for i in parts]
    print(chars)
    res = "".join(chars)
    return res