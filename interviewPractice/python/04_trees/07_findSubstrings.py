''''
You have two arrays of strings, words and parts. Return an array that contains the strings from words, modified so that any occurrences of the substrings from parts are surrounded by square brackets [], following these guidelines:

If several parts substrings occur in one string in words, choose the longest one. If there is still more than one such part, then choose the one that appears first in the string.

Example

For words = ["Apple", "Melon", "Orange", "Watermelon"] and parts = ["a", "mel", "lon", "el", "An"], the output should be
findSubstrings(words, parts) = ["Apple", "Me[lon]", "Or[a]nge", "Water[mel]on"].

While "Watermelon" contains three substrings from the parts array, "a", "mel", and "lon", "mel" is the longest substring that appears first in the string.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.string words

An array of strings consisting only of uppercase and lowercase English letters.

Guaranteed constraints:
0 ≤ words.length ≤ 104,
1 ≤ words[i].length ≤ 30.

[input] array.string parts

An array of strings consisting only of uppercase and lower English letters. Each string is no more than 5 characters in length.

Guaranteed constraints:
0 ≤ parts.length ≤ 105,
1 ≤ parts[i].length ≤ 5,
parts[i] ≠ parts[j].

[output] array.string
''''

#
# Definition for binary tree:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        

def findSubstrings(words, parts):
    trie = buildTrieFromParts(parts)
    r = [findSubString(x, trie) for x in words]
    return r


def findSubString(word, trie):
    maxLen = 0
    maxStartPos = 0

    for startPos in range(len(word)):
        current = trie
        for pos in range(startPos, len(word)):
            if word[pos] not in current.children:
                break
            current = current.children[word[pos]]
            
            length = pos - startPos + 1
            if current.terminal and length > maxLen:
                maxLen = length
                maxStartPos = startPos
    
    if maxLen == 0:
        return word
    
    return word[:maxStartPos] + "[" + word[maxStartPos:maxStartPos+maxLen] +"]" + word[maxStartPos+maxLen:]
    

def buildTrieFromParts(parts):
    root = TrieNode(None)
    for p in parts:
        addFragmentToTrie(root, p)
        
    return root


def addFragmentToTrie(root, fragment):
    current = root
    
    for c in fragment:
        if c not in current.children:
            current.children[c] = TrieNode(c)
        current = current.children[c]
        
    current.terminal = True   
    

    
class TrieNode(object):
    def __init__(self, c):
        self.children = dict()
        self.char = c
        self.terminal = False

        

        
def printTrie(t, level=0):
    print("  "*level, t.char, t.terminal)
    for c in t.children.values():
        printTrie(c, level+1)
    
