def houseOfCats(legs):
    maxPeople = legs // 2
    result = []
    for i in range(maxPeople+1):
        if (legs - i*2) % 4 == 0:
            result.append(i)
    return result

