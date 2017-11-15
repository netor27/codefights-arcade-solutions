def reverseParentheses(s):    
    '''
    You have a string s that consists of English letters, punctuation marks, whitespace characters, and brackets. 
    It is guaranteed that the parentheses in s form a regular bracket sequence.
    
    Your task is to reverse the strings contained in each pair of matching parentheses, starting from the innermost pair.    
    The results string should not contain any parentheses.
    '''
    l = list(s)
    stack = []
    for i in range(len(l)):
        if l[i] == '(':
            # opens a parenthesis, we must reverse this at some point
            stack.append(i)
        elif l[i] == ')':
            # close a parenthesis, reverse this from the last opening parenthesis found
            start = stack.pop()
            l[start + 1:i] = l[start + 1:i][::-1]
    return ''.join([i for i in l if (i != ')' and i != '(' )])

print(reverseParentheses("a(bc)de"))