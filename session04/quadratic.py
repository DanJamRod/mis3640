#For brevity and readability did not add/modify isinstance() code from my_abs.py
print(f"Daniel James Rodgers HW4b\n")

print(f"Quadratic Equation Solver")

def quadratic(a,b,c):
    x_1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    if b**2 - 4*a*c == 0:
        return(f"The sole root of {a}x^2 {b:+d}x {c:+d} = 0 is {x_1}")
    else:
        return(f"The roots of {a}x^2 {b:+d}x {c:+d} = 0 are {x_1} and {x_2}")

# # Test
# print(quadratic(2,-7,5))
# print(quadratic(1,-4,4))
# print(quadratic(1,4,5))