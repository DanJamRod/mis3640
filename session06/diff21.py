def diff21(n):
    """
    Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21
    """
    if n <=21:
        return 21-n
    else:
        return (n-21)*2

print(diff21(19))
print(diff21(21))
print(diff21(23))