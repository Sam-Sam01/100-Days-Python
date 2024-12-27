import turtle as tt
import random

tim = tt.Turtle()
tt.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(600):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))