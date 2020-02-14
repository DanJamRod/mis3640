def any_lowercase1(s):
    """Bool - True if the first character is lowercase
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Bool - True if "c" is lowercase (always True)
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Bool - True if the last character is lowercase
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Bool - True if any of the characters are lowercase (correct solution)
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Bool - True if all of the characters are lowercase
    """
    for c in s:
        if not c.islower():
            return False
    return True