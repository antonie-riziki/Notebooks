import turtle
from turtle import Turtle


window = turtle.Screen()
window.title("HEART GRAPHICS")
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(-8)
turtle.hideturtle()

def curve():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)

turtle.color("pink", "red")
turtle.begin_fill()
turtle.left(140)
turtle.forward(111.25)
curve()

turtle.left(120)
curve()
turtle.forward(111.25)
turtle.end_fill()

colors = ["red", "blue", "magenta", "yellow", "purple", "green"]

for i in range(50):
    for j in colors:
        turtle.color(j)
        turtle.circle(100)
        turtle.left(11)

for i in range(100):
    for color in ["white"]:
        turtle.color(color)
        turtle.left(11)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
        
        
