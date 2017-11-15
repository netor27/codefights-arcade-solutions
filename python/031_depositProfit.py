def depositProfit(deposit, rate, threshold):
    '''
    You have deposited a specific amount of dollars into your bank account. 
    Each year your balance increases at the same growth rate. Find out how 
    long it would take for your balance to pass a specific threshold with 
    the assumption that you don't make any additional deposits.
    '''
    current = deposit
    step = 0
    while current < threshold:
        current = current + (current * rate / 100)
        step+=1
    return step