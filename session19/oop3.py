# # Exercise 1 in Time1.py, but for your reference
# def time_to_int(self):
#     """ Computes the number of seconds since midnight.
#     """
#     minutes = self.hour * 60 + self.minute
#     seconds = minutes * 60 + self.second
#     return seconds

print(f"\nExercises 2, 3, 4")

class Point:
    """ Represents a point in 2-D space.
    """
    def __init__(self, x=0, y=0):
        """ Initializes a point object.
        x: float
        y: float
        """
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

a = Point(3,-5)
b = Point(1.9,1.9)

c = a + b
print(f"{a} + {b} = {c}")

d = a - b
print(f"{a} - {b} = {d}")