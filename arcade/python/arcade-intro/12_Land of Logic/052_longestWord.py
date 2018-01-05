def longestWord(text):
    '''
    Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
    '''
    maxLen, maxStart, currStart, currLen = 0, 0, 0, 0
    
    for i in range(len(text)):
        if text[i].isalpha():
            if currLen == 0:
                currStart = i
            currLen += 1
        else:
            if currLen > maxLen:
                maxLen = currLen
                maxStart = currStart
            currLen = 0
            
    if currLen > maxLen:
        maxLen = currLen
        maxStart = currStart    
    
    return text[maxStart:maxStart + maxLen]