# This prgram draws a design using repeated lines
import turtle

# Named Constants
START_X = -200
START_Y = 0
LINE_LENGTH = 400
NUM_LINES = 36
ANGLE = 170
ANIMATION_SPEED = 1

# Move the turtle to the initial position
turtle.hideturtle()
turtle.penup()
turtle.goto(START_X, START_Y)
turtle.pendown()

#  Setup the turtle
turtle.speed(ANIMATION_SPEED)

# Draw 36 lines, with the turtle tilted
# by 170 degrees after each line is drawn
for x in range(NUM_LINES):
    turtle.forward(LINE_LENGTH)
    turtle.left(ANGLE)

turtle.done()