'''
Consider the following ciphering algorithm:

For each character replace it with its code.
Concatenate all of the obtained numbers.
Given a ciphered string, return the initial one if it is known that it consists only of lowercase letters.

Note: here the character's code means its decimal ASCII code, the numerical representation of a character used by most modern programming languages.

Example

For cipher = "10197115121", the output should be
decipher(cipher) = "easy".

Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and charCode('y') = 121.
'''

def decipher(cipher):
    start = 0
    end = 0
    result =[]
    for i in range(len(cipher)):
        temp = castToValidLetter(cipher, start, end)
        if temp != '':
            result.append(temp)
            start = i+1
            end = i+1
        else:
            end +=1
    return ''.join(result)
        
        
def castToValidLetter(cipher, start, end):
    temp = int(cipher[start:end+1])
    if ord('a') <= temp <= ord('z'):
        return chr(temp)
    else:
        return ''