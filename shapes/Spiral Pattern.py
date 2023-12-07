from turtle import *

t=Turtle()
clr =['red','green','blue','orange','brown', 'purple']
t =Pen()
t.speed(50)
bgcolor('black')
for i in range(360):
    t.pencolor(clr[i%6])
    t.width(i//100+1)
    t.forward(i)
    t.left(59)

done()
hideturtle()





