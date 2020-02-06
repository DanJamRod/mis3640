def a_b_compare(a,b):
    """
    Compare a to b
    """
    if isinstance(a, str) or isinstance(b, str):
        print(f"string involved")
    elif a>b:
        print(f"bigger")
    elif a==b:
        print(f"equal")
    else:
        print(f"smaller")

a_b_compare(1,2)
a_b_compare(1,1)
a_b_compare(2,1)
a_b_compare(1,"hello")