from turtle import *
speed(1)
bgcolor("Black")
color("greenyellow")
pensize(5)

for i in range(6):
    left(60)
    for i in range(6):
        forward(100)
        left(60)

hideturtle()
done()