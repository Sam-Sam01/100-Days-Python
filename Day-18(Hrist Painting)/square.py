from turtle import *

sam_square = Turtle()
sam_square.shape("turtle")
sam_square.color("black")
sam_square.speed(1)

# for i in range (0,4):
#     sam_square.forward(100)
#     sam_square.left(90)

for i in range (0,4):
    if i % 2 == 0:
        sam_square.forward(100)
        sam_square.right(45)
    else:
        sam_square.fd(100)
        sam_square.right(135)


# sam_square.fd(100)
# sam_square.right(45)
# sam_square.fd(100)