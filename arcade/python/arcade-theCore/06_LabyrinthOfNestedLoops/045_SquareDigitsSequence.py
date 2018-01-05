def squareDigitsSequence(a0):
    '''
    Consider a sequence of numbers a0, a1, ..., an, in which an element is equal 
    to the sum of squared digits of the previous element. 
    The sequence ends once an element that has already been in the sequence appears again.
    
    Given the first element a0, find the length of the sequence.
    '''
    sequence = set()
    current = a0
    while current not in sequence:
        sequence.add(current)
        current = getSumOfSquareDigits(current)
        
    return len(sequence) + 1

        
def getSumOfSquareDigits(n):
    temp = 0
    while n > 0:
        digit = n % 10
        temp += digit ** 2
        n = n // 10
    return temp

