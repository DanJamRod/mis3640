a = 42*60 + 42
b = 10/1.61
c = b/(a/60**2)
print("There are", a, "seconds in 42 minutes and 42 seconds")
print("There are", str(round(b, 2)), "miles in 10 kilometers")
print("If you run 10km in 42 minutes and 42 seconds, your average speed is", str(round(c,2)), "mph")