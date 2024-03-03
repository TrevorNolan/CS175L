#Trevor Nolan

#CS 175L 01

#STOP

import math
import turtle


WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
ANIMATION_SPEED = 0
NUM_SIDES = 8
LENGTH = 100
ANGLE = 45
TEXT_X = -5
TEXT_Y = -10


turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)



s = LENGTH
x = s / math.sqrt(2)
diameter = s + (2 * x)


t = turtle.Turtle()
t.speed(ANIMATION_SPEED)


t.penup()
t.goto(-diameter / 2, s)
t.pendown()
t.penup()
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.pendown()


for _ in range(NUM_SIDES):
    t.forward(LENGTH)
    t.right(360 / NUM_SIDES)


t.penup()
t.goto(TEXT_X, TEXT_Y)
t.write("STOP", align="center", font=("Arial", 16, "bold"))

turtle.done()
