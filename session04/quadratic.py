print(f"Daniel James Rodgers HW4b\n")

print(f"Quadratic Equation Solver")

def quadratic(a,b,c):
    """
    Solves quadratic equation of the form ax^2 + bx + c, when a, b, and c are of type int or float
    """
    if isinstance(a,bool) or isinstance(b,bool) or isinstance(c,bool): # Special handling as bool is a sub class of int. 
        return(f"It is not possible to find the roots of this equation as it contains an input that is a boolean")
    elif isinstance(a,complex) or isinstance(b,complex) or isinstance(c,complex): # Special handling of complex for formatting reasons
        x_1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        x_2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        if b**2 - 4*a*c == 0:
            return(f"The sole root of ({a.real}{a.imag:+}j)x^2 + ({b.real:+}{b.imag:+}j)x + ({c.real:+}{c.imag:+}j) = 0 is ({x_1.real:+.2f}{x_1.imag:+.2f}j)")
        else:
            return(f"The roots of ({a.real}{a.imag:+}j)x^2 + ({b.real:+}{b.imag:+}j)x + ({c.real:+}{c.imag:+}j) = 0 are ({x_1.real:+.2f}{x_1.imag:+.2f}j) and ({x_2.real:+.2f}{x_2.imag:+.2f}j)")
    elif isinstance(a,(int,float)) and isinstance(b,(int,float)) and isinstance(c,(int,float)):
        x_1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
        x_2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
        if b**2 - 4*a*c == 0:
            return(f"The sole root of {a}x^2 {b:+d}x {c:+d} = 0 is {x_1}")
        else:
            return(f"The roots of {a}x^2 {b:+d}x {c:+d} = 0 are {x_1} and {x_2}")
    else:
        return(f"It is not possible to find the roots of this equation as it contains an input that is not an integer or float")


# # Test
# print(quadratic(2,-7,5))
# print(quadratic(1,-4,4))
# print(quadratic(1,4,5))
# print(quadratic(True,-4,4))
# print(quadratic(complex(3,1), complex(2,-1), complex(5,2)))