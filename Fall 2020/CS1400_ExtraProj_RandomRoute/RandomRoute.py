import turtle
import random

LOWER = -400
UPPER = 400

turtle.speed(0)
turtle.penup()
turtle.goto(LOWER, LOWER)
turtle.pendown()
for i in range(LOWER, UPPER + 10, 10):
    turtle.goto(turtle.xcor(), UPPER)
    turtle.penup()
    turtle.goto(turtle.xcor() + 10, LOWER)
    turtle.pendown()

turtle.penup()
turtle.goto(LOWER, LOWER)
turtle.pendown()
for i in range(LOWER, UPPER + 10, 10):
    turtle.pendown()
    turtle.goto(UPPER, turtle.ycor())
    turtle.penup()
    turtle.goto(LOWER, turtle.ycor() + 10)

turtle.penup()
turtle.speed(6)
turtle.goto(0, 0)
turtle.pendown()
turtle.width(2)
while True:
    dir = random.randint(1, 4)
    if dir == 1:
        turtle.goto(turtle.xcor() + 10, turtle.ycor())
    if dir == 2:
        turtle.goto(turtle.xcor() - 10, turtle.ycor())
    if dir == 3:
        turtle.goto(turtle.xcor(), turtle.ycor() + 10)
    if dir == 4:
        turtle.goto(turtle.xcor(), turtle.ycor() - 10)
    if turtle.xcor() >= UPPER:
        break
    if turtle.xcor() <= LOWER:
        break
    if turtle.ycor() >= UPPER:
        break
    if turtle.ycor() <= LOWER:
        break

turtle.done()
