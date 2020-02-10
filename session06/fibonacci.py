def fibonacci(n):
    """
    Return the nth number in the fibonacci sequence
    """ 
    a = 0
    b = 1
    if not isinstance(n, int):
        return "Incorrect input"
    elif n < 0:
        return "Incorrect input"
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(1,n): 
            c = a + b 
            a = b 
            b = c 
        return b

# print(fibonacci(0))
# print(fibonacci(1))
# print(fibonacci(2))
# print(fibonacci(3))
# print(fibonacci(191))
# print(fibonacci(-1))
# print(fibonacci("hello"))