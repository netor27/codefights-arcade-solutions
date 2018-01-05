def weakNumbers(n):
    '''
    We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.
    
    It follows that the weaker the number, the greater overall weakness it has. For the given integer n, 
    you need to answer two questions:
    
    what is the weakness of the weakest numbers in the range [1, n]?
    how many numbers in the range [1, n] have this weakness?
    
    Return the answer as an array of two elements, where the first element is the answer to the first question, 
    and the second element is the answer to the second question.
    '''
    divisors = { i:numOfDivisors(i) for i in range(1, n + 1) }  
    maxWeakness = 0
    numsWithMaxWeakness = 0
    for i in range(1, n+1):
        weakness = sum([1 if divisors[j] > divisors[i] else 0 for j in range(1, i)])
        if weakness > maxWeakness:
            maxWeakness = weakness
            numsWithMaxWeakness = 1
        elif weakness == maxWeakness:
            numsWithMaxWeakness += 1
        
    return [maxWeakness, numsWithMaxWeakness]
    
    
def numOfDivisors(n):
    return sum([1 if n % i == 0 else 0 for i in range(1, n // 2 + 1)]) + 1

