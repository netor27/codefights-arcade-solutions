def isTandemRepeat(inputString):
    '''
    Determine whether the given string can be obtained by one concatenation of some string to itself.

    Example

        For inputString = "tandemtandem", the output should be
            isTandemRepeat(inputString) = true;
        For inputString = "qqq", the output should be
            isTandemRepeat(inputString) = false;
        For inputString = "2w2ww", the output should be
            isTandemRepeat(inputString) = false.
    '''
    middle = len(inputString) // 2
    return inputString[:middle] == inputString[middle:]


print(isTandemRepeat("tandemtandem"))
print(isTandemRepeat("qqq"))