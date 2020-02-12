import math

def my_sqrt(a):
    """
    Returns a**0.5
    """
    if isinstance(a,bool) or not isinstance(a,(float,int)):
        return (f"'{a}' is a {type(a)}, please enter a number")
    elif a < 0:
        a = a * -1
        x = a * 0.5
        b = 0.5 * (x + a/x)
        while b != x:
            x = b
            b = 0.5 * (x + a/x)
        return complex(0, x)
    elif a == 0:
        return a
    else:
        x = math.log(a+1)**1.5 + a/500
        b = 0.5 * (x + a/x)
        while b != x:
            x = b
            b = 0.5 * (x + a/x)
        return x

# print(my_sqrt(25))
# print(my_sqrt(3682561))
# print(my_sqrt(0.25))
# print(my_sqrt(0))
# print(my_sqrt(-25))

def test_my_sqrt(*a):
    """
    Creates a table comparing output of my_sqrt(a) and math.sqrt(a)
    """
    print(f"\na                 my_sqrt(a)        math.sqrt(a)      difference")
    print(f"----------------  ----------------  ----------------  ----------------")
    for a in a:
        print(f"{a:<16.2f}  {my_sqrt(a):<16.6f}  {math.sqrt(a):<16.6f}  {abs(my_sqrt(a)-math.sqrt(a)):<16.1e}")

test_my_sqrt(1,2,3,4,5,6,7,8,9)