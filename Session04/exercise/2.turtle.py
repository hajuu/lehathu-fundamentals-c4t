from turtle import *
speed(0)
penup()
backward(200)
pendown()
for i in range(4):
    left(30)
    forward(50)
    right(60)
    forward(50)
    right(120)
    forward(50)
    right(60)
    forward(50)
    right(60)
penup()
forward(300)
pendown()
pencolor("magenta")
for i in range(3):
    forward(100)
    left(120)
pencolor("green")
for i in range(4):
    forward(100)
    left(90)
pencolor("magenta")
for i in range(5):
    forward(100)
    left(72)
pencolor("green")
for i in range(6):
    forward(100)
    left(60)
done()
