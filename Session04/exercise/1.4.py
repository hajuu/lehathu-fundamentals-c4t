from turtle import *
shape("turtle")
speed(0)
for i in range(4):
    forward(100)
    left(90)
penup()
backward(50)
pendown()
for i in range(3):
    backward(120)
    right(120)
penup()
right(90)
forward(50)
left(90)
pendown()
for i in range (360):
    forward(1)
    right(1)
penup()
forward(350)
pendown()
for i in range (360):
    for i in range(360):
        forward(1)
        right(1)
    right(7)

