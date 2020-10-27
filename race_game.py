import turtle
import random
import time
runprogram = True

player1 = turtle.Turtle()
player2 = turtle.Turtle()
lines = turtle.Turtle()

lines.penup()
lines.setposition(-100,250)
lines.pendown()
lines.write("Turtle Race", font=("Arial", 34, "normal"))
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
lines.penup()
lines.setposition(-60,200)
lines.pendown()

player1.shape("turtle")
player1.color("red")
player1.speed(10)
player1.penup()
player1.setposition(-265,-150)
player1.pendown()

player2.shape("turtle")
player2.color("blue")
player1.speed(10)
player2.penup()
player2.setposition(-265,150)
player2.pendown()

move1 = [20,50,60,0,90,-5,-10,-50,5,10]
move2 = [20,50,60,0,90,-5,-10,-50,5,10]

movement1 = 0
movement2 = 0
while(runprogram):
    pick1 = random.choice(move1)
    player1.forward(pick1)
    movement1 += pick1
    pick2 = random.choice(move2)
    player2.forward(pick2)
    movement2 += pick2
    time.sleep(.5)
    if movement1 >= 510:
        runprogram = False
        lines.write("Red wins!", font=("Arial", 24, "normal"))
    elif movement2 >= 510:
        runprogram = False
        lines.write("Blue wins!", font=("Arial", 24, "normal"))


lines.penup()
lines.setposition(-245,140)
lines.pendown()
lines.write(f'distance: {movement2}')
lines.penup()
lines.setposition(-245,-160)
lines.pendown()
lines.write(f'distance: {movement1}')

    

    

turtle.mainloop()