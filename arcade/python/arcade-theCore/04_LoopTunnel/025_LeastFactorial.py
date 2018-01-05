def leastFactorial(n):
'''
Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

'''

    k = 1
    i = 1
    while k < n:
        k = k * i
        i += 1
    return k

print(leastFactorial(5))
print(leastFactorial(1))
print(leastFactorial(17))