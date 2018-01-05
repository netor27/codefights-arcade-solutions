def validTime(time):
    '''
    Check if the given string is a correct time representation of the 24-hour clock.
    '''
    splitted = time.split(":")
    if len(splitted) != 2:
        return False
    
    if not splitted[0].isdigit() or not splitted[1].isdigit():
        return False
    
    hour = int(splitted[0])
    minute = int(splitted[1])
    return 0 <= hour < 24 and 0 < minute < 60

