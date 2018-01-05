def additionWithoutCarrying(param1, param2):
    '''
    A little boy is studying arithmetics. 
    He has just learned how to add two integers, written one below another, column by column. 
    But he always forgets about the important part - carrying.
    
    Given two integers, find the result which the little boy will get.
    '''
    result = 0
    currentDigit = 0
    while(param1 != 0 or param2 != 0):
        result = result + (param1 + param2) % 10 * 10 ** currentDigit
        currentDigit += 1
        param1 = param1 // 10
        param2 = param2 // 10        
    
    return result

print(additionWithoutCarrying(456, 1734))
print(additionWithoutCarrying(99999, 0))
print(additionWithoutCarrying(999, 999))
print(additionWithoutCarrying(0, 0))

