def isLucky(n):
    '''
    Ticket numbers usually consist of an even number of digits. 
    A ticket number is considered lucky if the sum of the first half 
    of the digits is equal to the sum of the second half.
    
    Given a ticket number n, determine if it's lucky or not.
    '''
    list = [int(i) for i in str(n)]    
    mid = len(list) // 2
    return sum(list[:mid]) == sum(list[mid:])

print(isLucky(1230))
print(isLucky(239017))