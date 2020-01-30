print(f"Daniel James Rodgers HW3\n")

# 1.1: 5, int
a = 3
print(f"1.1\nif a = 3\na + 2 = {a+2}, which is of {type(a+2)}\n")

# 1.2: 4.0, float
a = a + 1.0
print(f"1.2\nif a = 3\na + 1.0 = {a}, which is of {type(a)}\n")

# 1.3: none, nonetype
a = 3
print(f"1.3\nif a = 3\nb = none, which is of <class 'nonetype'>\n")

# 1.4: False, bool (3 is equal to 5 which is False)
a = 3
print(f"1.4\nif a = 3\na == 5.0 is {a == 5.0}, which is of {type(a == 5.0)}\n")

# 1.5: True, bool (10 is greater than 9 which is True)
b = 10
c = b > 9
print(f"1.5\nif b = 10\nb > 9 is {c}, which is of {type(c)}\n")

# 1.6: True, bool (2.5 is equal to 2.5 which is True, would also be True for 2 = 2.0)
5/2 == 5/2.0
print(f"1.6\n5/2 == 5/2.0 is {5/2 == 5/2.0}, which is of {type(5/2 == 5/2.0)}\n")

# 2.1 False (2 is not equal to 2, which is False)
3.0 - 1.0 != 5.0 - 3.0
print(f"2.1\n3.0 - 1.0 != 5.0 - 3.0 is {3.0 - 1.0 != 5.0 - 3.0}\n")

# 2.2 False (False or (True and False) = False or False = False)
3 > 4 or (2 < 3 and 9 > 10)
print(f"2.2\n3 > 4 or (2 < 3 and 9 > 10) is {3 > 4 or (2 < 3 and 9 > 10)}\n")

# 2.3 True (False or True and True = True and True = True)
4 > 5 or 3 < 4 and 9 > 8
print(f"2.3\n4 > 5 or 3 < 4 and 9 > 8 is {4 > 5 or 3 < 4 and 9 > 8}\n")

# 2.4 False (Not[True and True] = Not[True] = False)
not(4 > 3 and 100 > 6)
print(f"2.4\nnot(4 > 3 and 100 > 6) is {not(4 > 3 and 100 > 6)}\n")

# 3
import time
seconds = time.time()
result = time.gmtime(seconds)
print(f"3\nIt is currently {result.tm_hour:02d}:{result.tm_min:02d}:{result.tm_sec:02d} UTC")
print(f"It has been {int(seconds/(60*60*24))} days since the epoch")