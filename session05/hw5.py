print(f"Daniel James Rodgers HW5\n")

import turtle
import math
import my_polyline

t = turtle.Turtle()
for i in range (1):
    my_polyline.arc(t, 300, 40)
    my_polyline.arc(t, 0, 140)
    my_polyline.arc(t, 300, 40)
    my_polyline.arc(t, 0, 80)


turtle.mainloop()