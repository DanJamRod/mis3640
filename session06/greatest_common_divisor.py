def gcd(a,b):
    """
    Return the gcd of a and b
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        return "Incorrect input"
    elif b == 0:
        return a      
    else:
        return gcd(b,a%b)

# print(gcd(2, 12))
# print(gcd(6, 12))
# print(gcd(9, 12))
# print(gcd(17, 12))