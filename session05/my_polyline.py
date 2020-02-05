import turtle
import math

andrew = turtle.Turtle()

def polyline(t, n, length, angle):
    """
    Draws n line segments with given length and angle (in degrees) between them
    t is a turtle
    """
    for i in range (n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """
    Draws a polygon with given length and n sides between them
    t is a turtle
    """
    angle = 360/n
    polyline(t, n, length, angle)

def square(t, length):
    """
    Draws a sqaure with given length
    t is a turtle
    """
    polygon(t, 4, length)

def arc(t, r, angle):
    """
    Draws an arc with given radius r and angle (in degrees) between them
    t is a turtle
    """
    arc_length = 2*math.pi*r*angle/360
    n = int(arc_length/3) + 1
    step_length = arc_length/n
    step_angle = angle/n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    """
    Draws a circle with given radius r
    t is a turtle
    """
    arc(t, r, 360)

def turn(t, angle):
    """
    Turns the turtle anti-clockwise by given angle (degrees)
    t is a turtle
    """
    polyline(t, 1, 0, angle)

def move(t, x, y):
    """
    Move Turtle (t) forward (x, y) units without leaving a trail.
    Leaves the pen down.
    """
    t.pu()
    t.setpos(x, y)
    t.pd()

# def main():    
#     t = turtle.Turtle()
#     turtle.mainloop()
# if __name__ == "__main__":
#     main()