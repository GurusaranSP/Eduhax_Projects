from turtle import *

speed(5)
bgcolor("Black")
pensize(2)

for i in range(6):
    for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
        color(colours)
        circle(100)
        left(10)
hideturtle()
done()