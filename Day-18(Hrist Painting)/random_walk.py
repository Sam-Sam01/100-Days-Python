from turtle import *
import random

colors = ["red", "green", "blue", "yellow", "black", "purple", "orange", "pink"]
directions = [0, 90, 180, 270]

robot_walk = Turtle()
robot_walk.speed("normal")
robot_walk.shape("turtle")
robot_walk.width(10)
robot_walk.setposition(0, 0)
for _ in range (500):
    robot_walk.color(random.choice(colors))
    robot_walk.forward(10)
    robot_walk.setheading(random.choice(directions))