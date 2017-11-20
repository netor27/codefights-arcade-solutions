
def digitsProduct(product):
    '''
    Given an integer product, find the smallest positive (i.e. greater than 0) integer 
    the product of whose digits is equal to product. If there is no such integer, return -1 instead.
    '''
    if 0 < product < 10:
        return product
    if product == 0:
        return 10
    
    res = []
    while product > 1 :
        divisorFound = False
        divisor = 9        
        while not divisorFound:            
            if divisor == 1:
                return -1
            if product % divisor == 0:
                product = product // divisor
                res.append(str(divisor))                
                divisorFound = True
            divisor -= 1            
    
    return int(''.join(res[::-1]))
    