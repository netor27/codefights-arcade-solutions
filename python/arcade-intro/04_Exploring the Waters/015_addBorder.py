def addBorder(picture):
    '''
    Given a rectangular matrix of characters, add a border of asterisks(*) to it.
    '''
    for i in range(len(picture)):
        picture[i] = "*" + picture[i] + "*"
    border = ["*" * len(picture[0])]
    picture = border + picture + border
    return picture

print(addBorder( ["abc", "ded"]))