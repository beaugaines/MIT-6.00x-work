def isIn(char, str):
    if str == '':
        return False
    str = ''.join(sorted(str))
    middleIndex = int(len(str)/2)
    middleChar = str[middleIndex]
    if (len(str) == 1 and char != middleChar):
        return False
    elif middleChar == char:
        return True
    elif middleChar < char:
        return isIn(char, str[middleChar:])
    elif middleChar > char:
        return isIn(char, str[:middleChar])