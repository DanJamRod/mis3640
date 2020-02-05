print(f"Daniel James Rodgers HW5\n")
# Lines 50 - 52 have the functions 

import turtle
import math
import my_polyline

t = turtle.Turtle()

def petals():
    for i in range (3):
        my_polyline.arc(t, r=200, angle=60)
        my_polyline.turn(t, angle=120)
        my_polyline.arc(t, r=200, angle=60)

def flower():
    petals()
    my_polyline.turn(t, angle=60)
    petals()
    my_polyline.move(t, 0, -200)
    my_polyline.turn(t, angle=300)
    my_polyline.circle(t, r=200)

def yin_yang():
    my_polyline.arc(t, r=60, angle=180)
    my_polyline.circle(t, 120)
    my_polyline.move(t, 0, 0)
    my_polyline.arc(t, r=60, angle=180)
    my_polyline.move(t, 0, 50)
    my_polyline.circle(t, 10)
    my_polyline.move(t, 0, -70)
    my_polyline.circle(t, 10)

def tri_circ():
    my_polyline.turn(t, angle=-30)
    my_polyline.polyline(t,n=1,length=200, angle=120)
    my_polyline.polyline(t,n=1,length=100, angle=0)
    my_polyline.circle(t, 200*3**0.5/6)
    my_polyline.polyline(t,n=1,length=100, angle=120)
    my_polyline.polyline(t,n=1,length=200, angle=60)

def illuminati():
    for i in range (4):
        tri_circ()
    my_polyline.move(t, 0, -200)
    my_polyline.circle(t,200)


# # Uncomment to run a program
# flower()
# yin_yang()
# illuminati()

turtle.mainloop()