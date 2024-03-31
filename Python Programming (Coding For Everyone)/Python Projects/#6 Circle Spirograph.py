# Circle Spirogragph
import turtle

turtle.bgcolor("black")
turtle.pen(10)
turtle.speed(10)

for i in range(7):
    for color in ["red", "green", "blue", "white","cyan", "magenta", "yellow"]:
        turtle.color(color)
        turtle.circle(100)
        turtle.left(20)

turtle.hideturtle()