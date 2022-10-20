from asyncore import write
from turtle import *
import turtle as t
from turtle import Turtle, Screen, goto

wn = t.Screen()

brush = t.Turtle()
writeT = Turtle()
writeT.penup()
writeT.goto(-80, -250)
turtles = ['brush','Init_T']
brush.shape('circle')
# brush.shapesize(150,150)
# r, g, b, a = 100, 100, 100, 0
# brush.fillcolor(r,g,b,a)

pensize = 1

ShapeSpawnClick = False
SpawnSquare = False
SpawnTriangle = False
SpawnRectangle = False
SpawnCircle = False

#sets our base turtle color
color = 1
colorname = 'black'


#enables window to listen for input
wn.listen()

#sets turtles speed to fastest
brush.speed('fastest')
writeT.speed('fastest')

def undoB(e):
    i = 0
    while i < e:
        brush.undo()
        i += 1

def undoW(e):
    i = 0
    while i < e:
        writeT.undo()
        i += 1

def TpTurtle(x,y):
    if (y > -200):
        brush.penup()
        brush.goto(x,y)

def MousePos(x,y):
    print('{},{}'.format(x,y))
    #check if square button is clicked
    if (x > -760 and x < -660 and y < -205 and y > -255):
        global ShapeSpawnClick
        global SpawnSquare
        global SpawnCircle
        global SpawnRectangle
        global SpawnTriangle

        #save turtle x and y position as variables
        x1 = brush.xcor()
        y1 = brush.ycor()

        ShapeSpawnClick = True
        SpawnSquare = True
        SpawnCircle = False
        SpawnTriangle = False
        SpawnRectangle = False

        writeT.goto(50,-240)
        writeT.write('Click on the canvas to draw square', align = "center",font = ('Arial', 10, 'normal'))
        # if (y1 >= -100):
        #     square(x = x1, y = y1, size = 100, color = colorname, pen_thickness = pensize, turtle = brush)
        # else: 
        #     brush.write('too close to the border to produce square', align = "center",font = ('Arial', 10, 'normal'))
        #     #pause for 2 seconds then delete text
        #     wn.ontimer(brush.undo(), t = 2000)
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
            wn.ontimer(undoB(1), t = 2000)
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
            wn.ontimer(undoB(1), t = 2000)
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
    #check if clear button is clicked
    elif (x > -320 and x < -220 and y < -205 and y > -255):
        brush.clear()
    #check if undo button is clicked
    elif (x > -210 and x < -110 and y < -205 and y > -255):
        i = 0
        undoB(5)



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

# #square function
# def square(turtle,x,y, size, color, pen_thickness):
#     global clicked
#     turtle.penup()
#     writeT.goto(50,-240)
#     writeT.write('Click on the canvas to draw square', align = "center",font = ('Arial', 10, 'normal'))

#     clicked = False
#     while clicked == False:
#         wn.onclick(SquareSpawn)
#     MousePos(x,y)
#     # while (clicked != True):
#     #   
#     # turtle.goto(x + (size/2), y - (size/1.5))

def SquareSpawn(turtle,x,y, size):
    global ShapeSpawnClick
    turtle.setheading(0)
    turtle.pensize(pensize)
    minY = -200 + size
    if (y > minY):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for i in range(4):
            turtle.forward(size)
            turtle.right(90)
        turtle.penup()
        undoW(1)
        ShapeSpawnClick = False
    else:
        writeT.goto(x,y+20)
        writeT.write('too close to the border to produce square', align = "center",font = ('Arial', 10, 'normal'))
        #pause for 2 seconds then delete text
        wn.ontimer(undoW(2), t = 1000)

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

def RectangleSpawn(turtle,x,y, length, width, color, pen_thickness):
    global ShapeSpawnClick
    global SpawnRectangle
    global SpawnSquare
    global SpawnCircle
    global SpawnTriangle

    turtle.setheading(0)
    turtle.color(color)
    turtle.pensize(pen_thickness)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.forward(width)
        turtle.right(90)
    turtle.penup()
    writeT.undo()
    ShapeSpawnClick = False
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
    rectangle(turtles[1], -320, -205, 100, 50, 'black', 1)
    turtles[1].goto(-270, -238.34)
    turtles[1].write('Clear', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -210, -205, 100, 50, 'black', 1)
    turtles[1].goto(-160, -238.34)
    turtles[1].write('Undo', align = "center",font = ('Arial', 10, 'normal'))

    InitDone = True
    if (InitDone == True):
        turtles[1].hideturtle()
        turtles.remove(turtles[1])
    mySlider = Slider(-100, -300, 'black')


#create a square turtle to use as a slider that the user can drag to change the size of the shape
class Slider(Turtle):
    def __init__(self, x, y, color):
        Turtle.__init__(self)
        #make lines every 25 pixels to show the user where the slider is
        self.color(color)
        self.speed('fastest')
        self.shape('square')
        self.pensize(5)
        self.shapesize(1,1,1)
        self.penup()
        self.goto(112.5,y)
        self.pencolor('blue')
        self.pendown()
        self.goto(-137.5,y)
        self.penup()
        for i in range(0, 11):
            self.goto(-137.5 + (i * 25), y)
            self.pendown()
            self.goto(-137.5 + (i * 25), y + 10)
            self.penup()
        self.pencolor('black')
        self.goto(-137.5,-300)

        self.onrelease(self.drag)
    def drag(self, x, y):
        if(x<=125 and x>=-137.5):
            x1 = -125
            i = 1
            global pensize
            if (x < -112.5):
                self.goto(-137.5,-300)
                pensize = 1
            while i < 11:
                if (x >= x1 and x < x1+25):
                    self.setx(x1+12.5)
                    print(i)
                    pensize = (i * 5)
                    break
                else:
                    x1 += 25
                i += 1
            
            print(x)



def mouseClicked(x,y):
    if (ShapeSpawnClick == True):
        if (SpawnSquare == True):
            print('square')
            print('{},{}'.format(x,y))
            SquareSpawn(brush,x,y,100)
        elif (SpawnCircle == True):
            CircleSpawn(x,y)
        elif (SpawnRectangle == True):
            RectangleSpawn(x,y)
        elif (SpawnTriangle == True):
            TriangleSpawn(x,y)
    else:
        MousePos(x,y)

#on click return cordinates
wn.onclick(mouseClicked)

#when right click is pressed TpTurtle is called
wn.onclick(TpTurtle, 3)

#changes color when right or left arrow pressed
wn.onkey(ColorSwitchRight, 'Right')
wn.onkey(ColorSwitchLeft, 'Left')

#lets turtle to draw when dragged
brush.ondrag(Draw)
           
        

#initializes the program and makes the buttons
init()

wn.mainloop()

