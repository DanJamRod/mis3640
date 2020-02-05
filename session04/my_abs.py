print(f"Daniel James Rodgers HW4a\n")

print(f"my_abs")
"""
returns the absolute value of an int, float, or complex number
"""

def my_abs(x):
    if isinstance(x,(bool)): # Special handling as bool is a sub class of int. 
        return(f"It is not possible to find the absolute value of '{x}' as it is a boolean and not an integer or a float")
    elif isinstance(x,(complex)): # Special handling of complex
        return(f"The absolute value of {x} is {((x.real)**2 + ((x.imag)**2))**0.5}")
    elif not isinstance(x,(int,float)):
        return(f"It is not possible to find the absolute value of '{x}' as it is a {type(x)} and not an integer or a float")    
    elif x < 0:
        return(f"The absolute value of {x} is {x*-1}")
    else:
        return(f"The absolute value of {x} is {x}")

# # Test
# print(my_abs(5))
# print(my_abs(-2.5))
# print (my_abs([1, 5, 9]))
# print(my_abs(f"Hello, world!"))
# print(my_abs(5 == 5))
# print(my_abs(complex(-3,4)))