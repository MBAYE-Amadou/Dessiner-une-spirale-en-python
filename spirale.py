import random
import turtle

colors =['red', 'yellow', 'orange', 'green', 'cyan', 'pink']
s =turtle.Turtle()
s.speed(10)
turtle.bgcolor("black")
length =100
angle =50
size =5

for i in range(length):
    color =random.choice(colors)
    s.pencolor(color)
    s.fillcolor(color)
    s.penup()
    s.forward(i+50)
    s.pendown()
    s.left(angle)
    s.begin_fill()
    s.circle(size)
    s.end_fill()
turtle.exitonclick()
turtle.bgcolor("black")