def lineEncoding(s):
    '''
    Given a string, return its encoding defined as follows:
    
    First, the string is divided into the least possible number of disjoint substrings consisting of identical characters
    for example, "aabbbc" is divided into ["aa", "bbb", "c"]
    
    Next, each substring with length greater than one is replaced with a concatenation of its length and the repeating character
    for example, substring "bbb" is replaced by "3b"
    
    Finally, all the new strings are concatenated together in the same order and a new string is returned.
    
    For s = "aabbbc", the output should be lineEncoding(s) = "2a3bc".
    '''
    current = s[0]
    count = 1
    res = []
    for i in range(1, len(s)):
        if s[i] == current:
            count += 1
        else:
            if count > 1:
                res.append(str(count))
            res.append(current)
            current = s[i]
            count = 1
    # append last value
    if count > 1:
        res.append(str(count))
    res.append(current)
    
    return "".join(res)