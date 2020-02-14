def count(str, a):
    """ Counts how many times a substring appears in a string
    """
    count = 0
    for i in range(len(str)):
        if str[i] == a:
            count += 1
    return count

print(count("New England Patriots", "a"))