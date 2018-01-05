'''
Yesterday you found some shoes in the back of your closet. Each shoe is described by two values:

type indicates if it's a left or a right shoe;
size is the size of the shoe.
Your task is to check whether it is possible to pair the shoes you found in such a way that each pair consists of a right and a left shoe of an equal size.

Example

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [0, 23]]
the output should be
pairOfShoes(shoes) = true;

For

shoes = [[0, 21], 
         [1, 23], 
         [1, 21], 
         [1, 23]]
the output should be
pairOfShoes(shoes) = false.
'''
def pairOfShoes(shoes):
    if len(shoes) % 2 == 1:
        return False    
    
    d = dict()
    for s in shoes:
        key = s[1]
        value = (s[0] * -2) + 1
        if key in d:
            d[key] += value
        else:
            d[key] = value    
    return all(i == 0 for i in d.values())