''''
Given an array of integers a and an integer sum, find all of the unique combinations in a that add up to sum.
The same number from a can be used an unlimited number of times in a combination.
Elements in a combination (a1 a2 … ak) must be sorted in non-descending order, while the combinations themselves must be sorted in ascending order.
If there are no possible combinations that add up to sum, the output should be the string "Empty".

Example

For a = [2, 3, 5, 9] and sum = 9, the output should be
combinationSum(a, sum) = "(2 2 2 3)(2 2 5)(3 3 3)(9)".

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer a

An array of positive integers.

Guaranteed constraints:
1 ≤ a.length ≤ 12,
1 ≤ a[i] ≤ 9.

[input] integer sum

Guaranteed constraints:
1 ≤ sum ≤ 30.

[output] string

All possible combinations that add up to a given sum, or "Empty" if there are no possible combinations.
''''

res = []

def combinationSum(a, s):
    # get an array with only unique values lower or equal than the sum and sort them
    a = sorted(set([x for x in a if x <= s]))
    
    sumCombination(a, s, 0, 0, "")
    if len(res) > 0:
        result = "".join(["({0}".format(x[1:]) for x in res])
    else:
        result = "Empty"
    
    return result

    
    
def sumCombination(a, s, i, accum, accumStr):
    if accum == s:
        accumStr += ")"
        res.append(accumStr)
        return
    
    if accum > s:
        return 
    
    for i in range(i, len(a)):
        if accum+a[i] <= s:
            sumCombination(a, s, i, accum + a[i], accumStr + " {0}".format(a[i]))

    