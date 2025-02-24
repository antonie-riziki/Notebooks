import turtle

myTurtle = turtle.Turtle()
myTurtle.speed(0)


def circleToSquare(length, angle):
    for i in range(4):
        myTurtle.forward(length)
        myTurtle.right(angle)
        #myTurtle.color(color)

for i in range(500):
     for color in ["black"]:#["white", "green", "yellow", "magenta", "cyan"]:
            myTurtle.color(color)
            circleToSquare(100, 90)
            myTurtle.right(11)
            myTurtle.hideturtle()

for i in range(50):
    circleColor = ["red", "cyan", "yellow", "blue", "magenta", "green"]
    for colour in circleColor:
        myTurtle.color(colour)
        myTurtle.circle(100)
        myTurtle.left(11)
        myTurtle.hideturtle()


