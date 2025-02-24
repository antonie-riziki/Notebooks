import time
import turtle
from random import randint
from turtle import Turtle

#window setup
window = turtle.Screen()
turtle.title("Turtle Race")
turtle.speed(1)
turtle.bgcolor("green")
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("TURTLE RACE GAME", font=("Times New Roman", 30, "bold"))
turtle.penup()

#ground setup
turtle.setpos(-140, -180)
turtle.color("chocolate")
turtle.begin_fill()
turtle.pendown()
turtle.forward(1000)
turtle.right(90)
turtle.forward(190)
turtle.right(90)
turtle.forward(1900)
turtle.right(90)
turtle.forward(190)
turtle.right(90)
turtle.forward(500)
turtle.end_fill()

#finish line
stampSize = 20
squareSize = 15
finishLine = 500

turtle.color("black")
turtle.shape("square")
turtle.shapesize(squareSize / stampSize)
turtle.penup()

for i in range(11):
    turtle.setpos(finishLine, (150 - (i * squareSize * 2)))
    turtle.stamp()

for j in range(11):
    turtle.setpos(finishLine + squareSize, ((150 - squareSize) - (j * squareSize * 2)))
    turtle.stamp()


#turtle design
turtle.setpos(-600, 150)
turtle.shape("turtle")
turtle.forward(randint(1, window.window_width(randint(1, window.window_width()))))
turtle.setposition(window.window_height() / 2, 0)




window.exitonclick()

