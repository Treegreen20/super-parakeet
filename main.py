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


turtle.color("white")
win.bgcolor("black")



win.listen()

win.onkey(right,"Right")
win.onkey(left,"Left")
win.onkey(forward,"Up")
win.onkey(penup,"q")
win.onkey(pendown,"Q")



win.mainloop()