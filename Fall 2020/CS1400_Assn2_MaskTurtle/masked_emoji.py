# September 8, 2020
# Josh Bothell
# CS1400 Section 02
# Assignment 2

# setting up libraries and variables
import turtle
screen = turtle.getscreen()
t = turtle.Turtle()
mask = "#83CFF3"
accent = "#1285BA"
emoji = "#FFDC5D"
w = 'white'
b = 'black'


# setting up function to draw a filled circle to avoid repitition
def draw_circle(x, y, r, color):
    t.begin_fill()
    t.pu()
    t.goto(x, y)
    t.pd()
    t.color(color)
    t.circle(r)
    t.end_fill()


# drawing the main circle in the 'emoji' color
t.up()
t.fd(100)
t.lt(90)
t.down()
t.color(emoji)
t.begin_fill()
t.circle(100)
t.end_fill()
t.seth(0)

# drawing the eyes and making them less dead inside
draw_circle(40, 10, 15, b)
draw_circle(-40, 10, 15, b)
draw_circle(40, 5, 12.5, emoji)
draw_circle(-40, 5, 12.5, emoji)

# drawing the mask with a loop
t.goto(-75, 0)
t.color(mask)
t.begin_fill()
for i in range(2):
    t.fd(150)
    t.rt(90)
    t.fd(75)
    t.rt(90)
t.end_fill()

# drawing the 'folds' on the mask
t.goto(-65, -15)
t.color(accent)
step_a = -15
for i in range(4):
    t.fd(130)
    step_a -= 15
    t.pu()
    t.goto(-65, step_a)
    t.pd()

# setting up lists and drawing the mask strings by iteration
str_x = [-75, 75, -75, 75]
str_y = [-15, -15, -60, -60]
str_theta = [180, 0, 180, 0]
t.color(w)
for i in range(4):
    t.pu()
    t.goto(str_x[i], str_y[i])
    t.seth(str_theta[i])
    t.pd()
    t.fd(50)

# drawing text below the emoji
t.pu()
t.color(mask)
t.goto(0, -150)
t.write("Thanks for wearing a mask!", True, align="center", font=("Arial", 24, "normal"))
t.fd(20)
t.rt(90)
t.fd(100)
t.lt(90)

# adding in a unique twist in the form of a spiral frame.
t.pd()
step_b = 440
step_c = 1
for i in range(40):
    t.pensize(i)
    t.lt(90)
    t.fd(step_b)
    step_b += step_c
    step_c += 1

turtle.done()
