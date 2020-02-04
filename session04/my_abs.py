print(f"Daniel James Rodgers HW4a\n")

print(f"my_abs")

def my_abs(x):
    if isinstance(x,(bool)): # Special handling as bool is a sub class of int. 
        return(f"It is not possible to find the absolute value of '{x}' as it is a boolean and not an integer or a float")
    elif isinstance(x,(complex)): # Special handling as complex is a sub class of float. 
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
# print(my_abs(f"Hello, world!"))
# print(my_abs(5 == 5)) # Shows the importance of testing, would never have known bool or complex are a sub class of int and float respectively if hadn't have tested this and gotten weird results
# print(my_abs(complex(-3,4)))