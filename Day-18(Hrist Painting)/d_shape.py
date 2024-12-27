from turtle import *
import random

d_shape = Turtle()

d_shape.speed(1)
def draw_shape(num_sides):
    angle = 360/num_sides
    for i in range (num_sides):
        d_shape.forward(100)
        d_shape.right(angle)

# for sides in range (3, 11):
#     for i in range (sides):
#         d_shape.forward(100)
#         d_shape.right(360/sides)
#     d_shape.penup()
#     d_shape.forward(200)
#     d_shape.pendown()

for sides in range (3, 11):
    d_shape.color(random.choice(["red", "green", "blue", "yellow", "black", "purple", "orange", "pink"]))
    draw_shape(sides)