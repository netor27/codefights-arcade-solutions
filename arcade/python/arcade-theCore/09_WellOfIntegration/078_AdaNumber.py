'''
Consider two following representations of a non-negative integer:

A simple decimal integer, constructed of a non-empty sequence of digits from 0 to 9;
An integer with at least one digit in a base from 2 to 16 (inclusive), enclosed between # characters, and preceded by the base, which can only be a number between 2 and 16 in the first representation. For digits from 10 to 15 characters a, b, ..., f and A, B, ..., F are used.
Additionally, both representations may contain underscore (_) characters; they are used only as separators for improving legibility of numbers and can be ignored while processing a number.

Your task is to determine whether the given string is a valid integer representation.

Note: this is how integer numbers are represented in the programming language Ada.

Example

For line = "123_456_789", the output should be
adaNumber(line) = true;
For line = "16#123abc#", the output should be
adaNumber(line) = true;
For line = "10#123abc#", the output should be
adaNumber(line) = false;
For line = "10#10#123ABC#", the output should be
adaNumber(line) = false;
For line = "10#0#", the output should be
adaNumber(line) = true;
For line = "10##", the output should be
adaNumber(line) = false.
'''
def adaNumber(line):    
    line = line.replace('_','')
    splitted = line.split('#')
    n = len(splitted)
    
    # base case, a decimal number without a specific base
    if n == 1:
        if len(line) > 0:
            return validNumberString(line, 10)    
        else:
            return False
        
    # Check edge cases    
    if n != 1 and n != 3:
        return False    
    if len(splitted[0]) == 0 or len(splitted[1]) == 0:
        return False
    if not splitted[0].isdigit():
        return False
    base = int(splitted[0])
    if base < 2 or base > 16:
        return False
    
    return validNumberString(splitted[1], base)
        

def validNumberString(s, base):    
    try:
        i = int(s, base)
        return True    
    except ValueError:
        return False
       
    