def fileNaming(names):
    '''
    You are given an array of desired filenames in the order of their creation. 
    Since two files cannot have equal names, the one which comes later will have an 
    addition to its name in a form of (k), where k is the smallest positive integer such 
    that the obtained name is not used yet.
    
    Return an array of names that will be given to the files.
    '''
    # this dict will contain the name of the file as key and the current minumum value used for duplicates
    namesSet = {}
    result = []
    # iterate over the list of names
    for n in names:        
        # check the dict for current name
        if n not in namesSet:
            # if it's a new one, insert it with a 0 value for duplicate
            namesSet[n] = 0
            newName = n
        else:
            # if it's a duplicate, get the value and try to build a unique new name, if it already
            # exists, try adding 1 to the key
            newId = namesSet[n]
            newId += 1
            newName = "{}({})".format(n, newId)
            while newName in namesSet:
                newId += 1
                newName = "{}({})".format(n, newId)
            # here we have a unique name, add it to our set, with a 0 value for duplicates
            namesSet[n] = newId            
            namesSet[newName] = 0            
        # add the new name to the result list
        result.append(newName)
    return result
