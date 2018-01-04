'''
Check whether the given string is a subsequence of the plaintext alphabet.

Example

For s = "effg" or s = "cdce", the output should be
alphabetSubsequence(s) = false;
For s = "ace" or s = "bxz", the output should be
alphabetSubsequence(s) = true.
'''
def alphabetSubsequence(s):
    if len(s) < 1:
        return True
    current = -1
    for i in s:
        temp = ord(i)
        if temp <= current:
            return False
        current = temp
    return True