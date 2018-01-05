def knapsackLight(value1, weight1, value2, weight2, maxW):
        '''
    You found two items in a treasure chest! The first item weighs weight1 and is worth value1,
    and the second item weighs weight2 and is worth value2. What is the total maximum value of 
    the items you can take with you, assuming that your max weight capacity is maxW and you 
    can't come back for the items later?
    '''
    # Take both items
    if weight1 + weight2 <= maxW:
        return value1 + value2    
    
    # If we can choose from the two, chose the one with that values the most
    if weight1 <= maxW and weight2 <= maxW:
        return max(value1, value2)
    
    # If we can't decide choose the one we can carry
    if weight1 <= maxW:
        return value1
    if weight2 <= maxW:
        return value2
    
    # WE can't carry any item
    return 0
