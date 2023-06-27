import turtle

from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple' ])

def draw_circle(size, angle, shift) :
    turtle.bgcolor('white')
    turtle.pencolor (next (colors))
    turtle.circle(size)
    turtle.right (angle)
    turtle.forward(shift)
    draw_circle(size+8, angle-21, shift-8)

turtle.bgcolor ('black')
turtle. speed( 'fastest')
turtle.pensize (1)
draw_circle(30,0, 1)
