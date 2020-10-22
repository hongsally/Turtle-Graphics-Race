import turtle
import random
game = True

player1 = turtle.Turtle()
player2 = turtle.Turtle()
lines = turtle.Turtle()

lines.penup()
lines.setposition(0,300)
lines.pendown()
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
player1.penup()
player1.setposition(-265,-150)

player2.shape("turtle")
player2.color("blue")
player2.penup()
player2.setposition(-265,150)

move1 = [20,50,60,0,90,-5,-10,-50,100,10]
move2 = [20,50,60,0,90,-5,-10,-50,100,10]

    
    



turtle.mainloop()