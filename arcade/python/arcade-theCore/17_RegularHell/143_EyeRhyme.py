def eyeRhyme(pairOfLines):
    pattern = "^.*(.{3})\t.*(.{3})$"
    match = re.match(pattern, pairOfLines)
    return match.group(1) == match.group(2)
