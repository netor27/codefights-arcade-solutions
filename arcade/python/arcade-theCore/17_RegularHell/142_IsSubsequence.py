def isSubsequence(t, s):
    pattern = ''
    for ch in s :
        pattern += "["+ch+"]"+"+.*"
    return re.search(pattern, t) is not None
