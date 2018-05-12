''''
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example

For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.


''''

# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def addTwoHugeNumbers(a, b):
    a = reverseList(a)
    b = reverseList(b)
    helper = ListNode(None)   
    r = helper
    carry = 0
    while a != None or b != None or carry > 0:
        aValue = 0 if a == None else a.value
        bValue = 0 if b == None else b.value
        total = aValue + bValue + carry
        carry = total // 10000
        total = total % 10000
        r.next = ListNode(total)
        r = r.next
        if a != None:
            a = a.next
        if b != None:
            b = b.next
        
    return reverseList(helper.next)

    
def reverseList(a):
    if a == None:
        return None
    
    stack = []
    while a != None:
        stack.append(a.value)
        a = a.next
    
    r = ListNode(stack.pop())
    head = r
    while len(stack) > 0:        
        r.next = ListNode(stack.pop())        
        r = r.next
    
    return head

def printList(a):
    while a != None:
        print (a.value)
        a = a.next
    