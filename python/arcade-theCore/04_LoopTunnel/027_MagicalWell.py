def magicalWell(a, b, n):
    '''
    You are standing at a magical well. It has two positive integers written on it: a and b. 
    Each time you cast a magic marble into the well, it gives you a * b dollars and then 
    both a and b increase by 1. You have n magic marbles. How much money will you make?
    '''
    res = 0
    for i in range(n):
        res += (a * b)
        a += 1
        b += 1
    return res

print(magicalWell(1, 2, 2))
print(magicalWell(6, 5, 3))

