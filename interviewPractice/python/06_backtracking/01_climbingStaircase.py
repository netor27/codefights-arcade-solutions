''''
You need to climb a staircase that has n steps, and you decide to get some extra exercise by jumping up the steps. You can cover at most k steps in a single jump. Return all the possible sequences of jumps that you could take to climb the staircase, sorted.

Example

For n = 4 and k = 2, the output should be

climbingStaircase(n, k) =
[[1, 1, 1, 1],
 [1, 1, 2],
 [1, 2, 1],
 [2, 1, 1],
 [2, 2]]
There are 4 steps in the staircase, and you can jump up 2 or fewer steps at a time. There are 5 potential sequences in which you jump up the stairs either 2 or 1 at a time.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 10.

[input] integer k

Guaranteed constraints:
0 ≤ k ≤ n.

[output] array.array.integer

An array containing all of the possible sequences in which you could climb n steps by taking them k or fewer at a time.
''''

steps = []

def climbingStaircase(n, k):
    climb(n, k, [])
    return steps

def climb(n, k, stepsTaken):
    if n == 0:
        steps.append(stepsTaken)
        return
    
    for i in range(1, k+1):
        if n - i >= 0:
            newList = list(stepsTaken)
            newList.append(i)
            climb(n-i, k, newList)
            
            