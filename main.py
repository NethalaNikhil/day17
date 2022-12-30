from turtle import Screen, Turtle
from random import randint

screen = Screen()
tim = Turtle()
size = [120, 90, 72, 60, 51, 45, 40, 36]
tim.color("red")
color = ["red","red","red","yellow","blue","black","orange","pink","violet","green","red"]
k=0
for i in range(3, 11, 1):
    for j in range(i):
        tim.right(size[k])
        tim.forward(100)
    tim.color(color[i])
    k = k + 1

screen.exitonclick()
