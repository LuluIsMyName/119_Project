import turtle as t
from turtle import Turtle, Screen

brush = t.Turtle()
turtles = ['brush','Init_T']
wn = t.Screen()

#free draw function
def Drag(x,y):
    brush.ondrag(None)
    brush.setheading(brush.towards(x,y))
    brush.goto(x,y)
    brush.ondrag(Drag)

def TpTurtle(x,y):
    turtles[1].penup()
    turtles[1].goto(x,y)
    turtles[1].pendown()

def MousePos(x,y):
    print('{},{}'.format(x,y))
color = 1
def ColorSwitchRight():
    global color
    if color == 1:
        brush.color('blue')
        print('blue')
        color = 2
    elif color == 2:
        brush.color('green')
        print('green')
        color = 3
    elif color == 3:
        brush.color('red')
        print('red')
        color = 4
    elif color == 4:
        brush.color('black')
        print('black')
        color = 1

def ColorSwitchLeft():
    global color
    if color == 1:
        brush.color('red')
        print('red')
        color = 4
    elif color == 2:
        brush.color('black')
        print('black')
        color = 1
    elif color == 3:
        brush.color('blue')
        print('blue')
        color = 2
    elif color == 4:
        brush.color('green')
        print('green')
        color = 3

wn.listen()
wn.onclick(MousePos, 1)
wn.onkey(TpTurtle, 'space')
wn.onkey(ColorSwitchRight, 'Right')
wn.onkey(ColorSwitchLeft, 'Left')


def Draw(x, y):
    brush.ondrag(None)
    brush.setheading(brush.towards(x,y))
    brush.goto(x,y)
    brush.ondrag(Draw)

#square function
def square(turtle,x,y, size, color, pen_thickness):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(pen_thickness)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.penup()
    turtle.goto(x + (size/2), y - (size/3))

def rectangle(turtle, x, y, length, width, color, pen_thickness):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(pen_thickness)
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.penup()
    turtle.goto(x + (length/2), y - (width/1.5))
#circle function
def circle(turtle,x,y, radius, color, pen_thickness):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(pen_thickness)
    turtle.circle(radius)

def init():
    InitDone = False
    turtles[1] = t.Turtle()
    turtles[1].penup()
    turtles[1].goto(-770,-200)
    turtles[1].pendown()
    turtles[1].color('black')
    turtles[1].pensize(1)
    turtles[1].speed('fastest')
    turtles[1].goto(765,-200)
    rectangle(turtles[1], -760, -205, 100, 50, 'black', 1)
    turtles[1].write('Square', align = "center",font = ('Arial', 10, 'normal'))
    InitDone = True
    if (InitDone == True):
        turtles[1].hideturtle()
        turtles.remove(turtles[1])

#lets window listen to mouse inputs


#sets turtle speed to fastest
brush.speed('fastest')

#lets turtle to draw when dragged
brush.ondrag(Drag)

#initializes the program and makes the buttons
init()

wn.mainloop()
