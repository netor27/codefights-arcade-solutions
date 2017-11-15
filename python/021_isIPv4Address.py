def isIPv4Address(inputString):
    '''
    Given a string, find out if it satisfies the IPv4 address naming rules.
    IPv4 addresses are represented in dot-decimal notation, which consists 
    of four decimal numbers, each ranging from 0 to 255 inclusive, separated by dots, e.g., 172.16.254.1.
    '''
    splitted = inputString.split(".")
    if len(splitted) != 4:
        return False
    
    try:
        for n in splitted:
            if not n.isdigit():
                return False
            aux = int(n)
            if 0 > aux or aux > 255:
                return False
    except ValueError:
        return False
    
    return True
        
print(isIPv4Address("192.168.1.1"))
print(isIPv4Address("192.2.1.1"))
print(isIPv4Address("192.259.1.1"))
print(isIPv4Address("192..."))