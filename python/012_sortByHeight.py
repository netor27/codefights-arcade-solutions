def sortByHeight(a):
    '''
    Some people are standing in a row in a park. 
    There are trees between them which cannot be moved. 
    Your task is to rearrange the people by their heights
    in a non-descending order without moving the trees.
    '''
    withoutTrees = [i for i in a if i != -1]
    withoutTrees.sort()
    currentIndex = 0 
    for i in range(len(a)):
        if a[i] != -1:
            a[i] = withoutTrees[currentIndex]
            currentIndex += 1
    return a

print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))