from asyncore import write
from turtle import *
import turtle as t
from turtle import Turtle, Screen, goto

brush = t.Turtle()
turtles = ['brush','Init_T', 'Slider_T']
pensize = 1
wn = t.Screen()

def TpTurtle(x,y):
    if (y > -200):
        brush.penup()
        brush.goto(x,y)

def MousePos(x,y):
    print('{},{}'.format(x,y))
    #check if square button is clicked
    if (x > -760 and x < -660 and y < -205 and y > -255):
        #save turtle x and y position as variables
        x1 = brush.xcor()
        y1 = brush.ycor()
        if (y1 >= -100):
            square(x = x1, y = y1, size = 100, color = colorname, pen_thickness = pensize, turtle = brush)
        else: 
            brush.write('too close to the border to produce square', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(brush.undo(), t = 2000)
    #check if rectangle button is clicked
    elif (x > -540 and x < -440 and y < -205 and y > -255):
        #save turtle x and y position as variables
        x1 = brush.xcor()
        y1 = brush.ycor()
        if (y1 >= -100):
            rectangle(x = x1, y = y1, length = 100, width = 50, color = 'black', pen_thickness = pensize, turtle = brush)
        else: 
            brush.write('too close to the border to produce rectangle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(brush.undo(), t = 2000)
    #check if circle button is clicked
    elif (x > -650 and x < -550 and y < -205 and y > -255):
        #save turtle x and y position as variables
        x1 = brush.xcor()
        y1 = brush.ycor()
        if (y1 >= -100):
            circle(x = x1, y = y1, radius = 50, color = 'black', pen_thickness = pensize, turtle = brush)
        else: 
            brush.write('too close to the border to produce circle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(brush.undo(), t = 2000)
    #check if triangle button is clicked
    elif (x > -430 and x < -330 and y < -205 and y > -255):
        #save turtle x and y position as variables
        x1 = brush.xcor()
        y1 = brush.ycor()
        if (y1 >= -100):
            triangle(x = x1, y = y1, length = 100, color = 'black', pen_thickness = pensize, turtle = brush)
        else: 
            brush.write('too close to the border to produce triangle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(brush.undo(), t = 2000)


#sets our base turtle color
color = 1
colorname = 'black'

#freedraw function
def Draw(x, y):
    if (y > -200):
        brush.ondrag(None)
        brush.pensize(pensize)
        brush.pendown()
        brush.setheading(brush.towards(x,y))
        brush.goto(x,y)
        brush.ondrag(Draw)
        print(pensize)

#allows color to change forwards
def ColorSwitchRight():
    global color
    global colorname
    if color == 1:
        brush.color('blue')
        colorname = 'blue'
        print('blue')
        color = 2
    elif color == 2:
        brush.color('green')
        colorname = 'green'
        print('green')
        color = 3
    elif color == 3:
        brush.color('red')
        colorname = 'red'
        print('red')
        color = 4
    elif color == 4:
        brush.color('black')
        colorname = 'black'
        print('black')
        color = 1
#allows color to change backwards
def ColorSwitchLeft():
    global color
    global colorname
    if color == 1:
        brush.color('red')
        colorname = 'red'
        print('red')
        color = 4
    elif color == 2:
        brush.color('black')
        colorname = 'black'
        print('black')
        color = 1
    elif color == 3:
        brush.color('blue')
        colorname = 'blue'
        print('blue')
        color = 2
    elif color == 4:
        brush.color('green')
        colorname = 'green'
        print('green')
        color = 3

#enables window to listen for input
wn.listen()

#sets turtle speed to fastest
brush.speed('fastest')

#on click return cordinates
wn.onclick(MousePos, 1)

#when right click is pressed TpTurtle is called
wn.onclick(TpTurtle, 3)

#changes color when right or left arrow pressed
wn.onkey(ColorSwitchRight, 'Right')
wn.onkey(ColorSwitchLeft, 'Left')

#lets turtle to draw when dragged
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
    # turtle.goto(x + (size/2), y - (size/1.5))

#rectangle function
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
    # turtle.goto(x + (length/2), y - (width/1.5))
    # x1 = turtle.xcor()
    # y1 = turtle.ycor()
    # print('{},{}'.format(x1,y1))

#circle function
def circle(turtle,x,y, radius, color, pen_thickness):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(pen_thickness)
    turtle.circle(radius)
    turtle.penup()

#triangle function
def triangle(turtle, x, y, length, color, pen_thickness):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.pensize(pen_thickness)
    turtle.setheading(0)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.penup()

#initializes the program and sets up buttons
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
    turtles[1].goto(-710, -238.34)
    turtles[1].write('Square', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -650, -205, 100, 50, 'black', 1)
    turtles[1].goto(-600, -238.34)
    turtles[1].write('Circle', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -540, -205, 100, 50, 'black', 1)
    turtles[1].goto(-490, -238.34)
    turtles[1].write('Rectangle', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -430, -205, 100, 50, 'black', 1)
    turtles[1].goto(-380, -238.34)
    turtles[1].write('Triangle', align = "center",font = ('Arial', 10, 'normal'))
    InitDone = True
    if (InitDone == True):
        turtles[1].hideturtle()
        turtles.remove(turtles[1])
    mySlider = Slider(-100, -300, 'black')


#create a square turtle to use as a slider that the user can drag to change the size of the shape
class Slider(Turtle):
    def __init__(self, x, y, color):
        Turtle.__init__(self)
        self.color(color)
        self.speed('fastest')
        self.shape('square')
        self.pensize(5)
        self.shapesize(2,2,2)
        self.penup()
        self.goto(125,y)
        self.pendown()
        self.goto(-125,y)
        self.ondrag(self.drag)
    def drag(self, x, y):
        if(x<=125 and x>=-125):
            self.setx(x)
            global pensize
            pensize = (self.xcor()+126)
            print(pensize)

#initializes the program and makes the buttons
init()
wn.mainloop()
