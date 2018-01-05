def isSubstitutionCipher(s1, s2):
    '''
    A ciphertext alphabet is obtained from the plaintext alphabet by means of rearranging some characters. For example "bacdef...xyz" will be a simple ciphertext alphabet where a and b are rearranged.

A substitution cipher is a method of encoding where each letter of the plaintext alphabet is replaced with the corresponding (i.e. having the same index) letter of some ciphertext alphabet.

Given two strings, check whether it is possible to obtain them from each other using some (possibly, different) substitution ciphers.

Example

For string1 = "aacb" and string2 = "aabc", the output should be
isSubstitutionCipher(string1, string2) = true.

Any ciphertext alphabet that starts with acb... would make this transformation possible.

For string1 = "aa" and string2 = "bc", the output should be
isSubstitutionCipher(string1, string2) = false.
    '''
    n = len(s1)
    d = dict()
    d2 = dict()
    for i in range(n):
        if s1[i] in d:
            if d[s1[i]] != s2[i]:
                return False
        elif s2[i] in d2:
            if d2[s2[i]] != s1[i]:
                return False
        else:
            d[s1[i]] = s2[i]
            d2[s2[i]] = s1[i]
    return True