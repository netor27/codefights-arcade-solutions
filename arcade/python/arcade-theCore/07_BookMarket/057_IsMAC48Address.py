def isMAC48Address(inputString):
    '''
    A media access control address (MAC address) is a unique identifier assigned to network 
    interfaces for communications on the physical network segment.
    
    The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is 
    six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).
    
    Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.
    '''
    splitted = inputString.split('-')
    if len(splitted) != 6:
        return False
    
    for i in range(6):
        if not isValid2HexValue(splitted[i]):
            return False    
    return True

def isValid2HexValue(st):
    if len(st) != 2:
        return False
    
    if not st[0].isdigit():
        if ord(st[0]) < 65 or ord(st[0]) > 70:
            return False
        
    if not st[1].isdigit(): 
        if ord(st[1]) < 65 or ord(st[1]) > 70:
            return False
        
    return True