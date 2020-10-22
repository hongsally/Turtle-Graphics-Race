import turtle
import random

player1 = turtle.Turtle()
player2 = turtle.Turtle()
lines = turtle.Turtle()

lines.penup()
lines.setposition(0,300)
lines.pendown()
lines.write("--Turtle Graphics Race--",font=("Calibri", 30, "bold"))
lines.speed(100)
lines.penup()
lines.setposition(-250,-300)
lines.left(90)
lines.pendown()
lines.forward(650)
lines.penup()
lines.setposition(250,-300)
lines.pendown()
lines.forward(650)

player1.shape("turtle")
player1.color("red")

turtle.mainloop()