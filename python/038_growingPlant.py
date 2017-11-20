def growingPlant(upSpeed, downSpeed, desiredHeight):
    if desiredHeight == 0:
        return 0
    
    currentHeight = upSpeed
    count = 1
    while currentHeight < desiredHeight:
        currentHeight -= downSpeed
        currentHeight += upSpeed
        count += 1
    return count
