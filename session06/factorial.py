def factorial(n):
    """
    Return n!
    """
    if not isinstance(n, int):
        return "Incorrect input"
    elif n < 0:
        return "Incorrect input"
    else:
        fact = 1
        for i in range(1,n+1): 
            fact = fact * i
        return fact

# print(factorial(1))
# print(factorial(2))
# print(factorial(3))
# print(factorial(19))
# print(factorial(-1))
# print(factorial("hello"))