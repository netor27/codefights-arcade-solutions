def arithmeticExpression(a, b, c):
    '''
Consider an arithmetic expression of the form a#b=c. Check whether it is possible to replace # with one of the four signs: +, -, * or / to obtain a correct expression.
    '''
    return a + b == c or a - b == c or a * b == c or a / b == c

print(arithmeticExpression(2, 3, 5))
print(arithmeticExpression(8, 3, 2))