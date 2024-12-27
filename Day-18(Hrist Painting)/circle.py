from turtle import *
import turtle as tt
import random

cc = Turtle()
cc.speed("fastest")
tt.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        cc.color(random_color())
        cc.circle(100)
        current_heading = cc.heading()
        cc.setheading(current_heading + gap_size)

# for _ in range(360):
#     cc.circle(100)
#     cc.color(random_color())
#     current_heading = cc.heading()
#     cc.setheading(current_heading + 1)

draw_spirograph(4)

screen = tt.Screen()
screen.exitonclick()