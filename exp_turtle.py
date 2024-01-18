import turtle
t=turtle.Turtle()
t.pensize(3)
t.pencolor('green')
t.pen(fillcolor='light green')
t.begin_fill()
for i in range(4):
    t.fd(200)
    t.rt(90)
t.end_fill()
#---------
t.penup()
t.goto(100,100)
t.pendown()
t.pencolor('black')
t.pen(fillcolor='yellow')
t.begin_fill()
t.circle(50)
t.end_fill()
#---------triangel
t.penup()
t.goto(-100,300)
t.pendown()
t.pencolor('purple')
t.pen(fillcolor='red')
t.begin_fill()
for i in range(3):
    t.fd(200)
    t.rt(360/3)
t.end_fill()
#-----------------
t.penup()
t.goto(-300,100)
t.pendown()
t.pencolor('red')
t.pen(fillcolor='pink')
t.begin_fill()
for i in range(6):
    t.fd(100)
    t.rt(360/6)
t.end_fill()

t.hideturtle()
turtle.done()