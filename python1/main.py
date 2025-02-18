# Python Turtle project
import turtle
turtle.bgcolor("black")
turtle.pensize(2.5)
turtle.speed(0.5)
color = ["Red", "Pink","Yellow","White","Green","Orange","Purple"]
for x in range(10):
    for i in color:
        turtle.color(i)
        turtle.circle(150)
        turtle.right(10)
turtle.mainloop()