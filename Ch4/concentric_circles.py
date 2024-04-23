# Concentric circles
import turtle

# Named Constants
NUM_CIRCLES = 20
STARTING_RADIUS=20
OFFSET = 10
ANIMATION_SPEED = 0

#  Setup the turtle
turtle.speed(ANIMATION_SPEED)
turtle.hideturtle()

# Set the radius of the first circle
radius = STARTING_RADIUS

# Draw the circles
for count in range(NUM_CIRCLES):
    # Draw the circle
    turtle.circle(radius)

    # get the co-ordinates for the next circle
    x = turtle.xcor()
    y = turtle.ycor() - OFFSET

    # Calculate the radius for the next circle
    radius = radius + OFFSET

    # Position the turtle for the next circle
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

turtle.done()
