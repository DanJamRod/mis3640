print(f"Daniel James Rodgers HW4\n")

print(f"Quadratic Equation Solver")

def quadratic(a,b,c):
    x_1 = (-b - (b**2 - 4*a*c)**0.5)/(2*a)
    x_2 = (-b + (b**2 - 4*a*c)**0.5)/(2*a)
    if b**2 - 4*a*c == 0:
        print(f"The sole root of {a}x^2 {b:+d}x {c:+d} = 0 is {x_1}")
    else:
        print(f"The roots of {a}x^2 {b:+d}x {c:+d} = 0 are {x_1} and {x_2}")

quadratic(2,-7,5)
quadratic(1,-4,4)
quadratic(1,4,5)