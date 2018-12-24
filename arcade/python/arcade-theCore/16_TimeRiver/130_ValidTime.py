def validTime(time):
    if time is None:
        return False
    splitted = time.split(":")
    if len(splitted) != 2:
        return False

    if int(splitted[0]) < 0 or int(splitted[0]) > 23:
        return False
    if int(splitted[1]) < 0 or int(splitted[1]) > 59:
        return False
    return True
