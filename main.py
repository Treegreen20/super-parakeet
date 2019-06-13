import turtle

win = turtle.Screen()
turtle = turtle.Turtle()

def right():
    turtle.right(45)

def left ():
    turtle.left(45)

def forward():
    turtle.forward(75)

def penup():
    turtle.penup()

def pendown():
    turtle.pendown()

def center():
    turtle.setx(0)
    turtle.sety()

turtle.color("white")
win.bgcolor("black")



win.listen()

win.onkey(right,"Right")
win.onkey(left,"Left")
win.onkey(forward,"Up")
win.onkey(penup,"q")
win.onkey(pendown,"w")
win.onkey(center,"Q")






win.mainloop()