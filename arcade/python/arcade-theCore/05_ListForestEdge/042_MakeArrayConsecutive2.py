def makeArrayConsecutive2(statues):
    '''
    Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, 
    each statue having an non-negative integer size. 
    Since he likes to make things perfect, he wants to arrange them from smallest to 
    largest so that each statue will be bigger than the previous one exactly by 1. 
    He may need some additional statues to be able to accomplish that. 
    Help him figure out the minimum number of additional statues needed.
    '''
    lower = min(statues)
    upper = max(statues)
    return upper - lower - (len(statues) - 2) - 1


print(makeArrayConsecutive2([6, 2, 3, 8]))
print(makeArrayConsecutive2([0, 3]))
print(makeArrayConsecutive2([5, 4, 6]))
print(makeArrayConsecutive2([6, 3]))
print(makeArrayConsecutive2([1]))