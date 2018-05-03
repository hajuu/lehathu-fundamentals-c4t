from turtle import *
speed(0)
colors=['red','blue','brown','yellow','grey']

# for i in range(3,8):
#     angle=int(180-180*(i-2)/i)
#     for j in range(i):
#         pencolor(colors[i-3])
#         forward(100)
#         left(angle)

for i in range(5,0,-1):
    pencolor(colors[i - 1])
    fillcolor(colors[i - 1])
    begin_fill()
    for j in range(2):
        forward(i*50)
        left(90)
        forward(100)
        left(90)
    end_fill()


done()