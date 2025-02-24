import turtle

myTurtle = turtle.Turtle()
#myTurtle.title("SPIROGRAPH")
myTurtle.pensize(2)
myTurtle.speed(0)

for i in range(6):
    circleColor = ["red", "cyan", "yellow", "blue", "magenta", "green"]
    for colour in circleColor:
        myTurtle.color(colour)
        myTurtle.circle(100)
        myTurtle.left(10)

myTurtle.hideturtle()
