from asyncore import write
import string
from turtle import *
import turtle as t
from turtle import Turtle, Screen, goto

wn = t.Screen()

brush = t.Turtle()
writeT = Turtle()
writeT.penup()
writeT.goto(50, -240)
turtles = ['brush','Init_T','SquareT','RectangleT','CircleT','TriangleT']
turtles[2] = Turtle()
turtles[3] = Turtle()
turtles[4] = Turtle()
turtles[5] = Turtle()

brush.shape('circle')
# brush.shapesize(150,150)
# r, g, b, a = 100, 100, 100, 0
# brush.fillcolor(r,g,b,a)

pensize = 1
shapesize = 100

ShapeSpawnClick = False
SpawnSquare = False
SpawnTriangle = False
SpawnRectangle = False
SpawnCircle = False
SquareSpawnActive = False
CircleSpawnActive = False
TriangleSpawnActive = False
RectangleSpawnActive = False
SquareSize = 100
RectangleLength = 100
RectangleWidth = 100
CircleSize = 100
TriangleSize = 100
Rectangle = RectangleLength

#do this
#if(LengthActive == True):
    #Rectangle Length = etc
    #clear RectangleT
    #wriite "Rectangle Length = etc etc"
#elif(WidthActive == True):
    #Rectangle Width = etc
    #clear RectangleT
    #write "Rectangle Width = etc etc"
#do this

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
    global SquareSpawnActive
    global RectangleSpawnActive
    global CircleSpawnActive
    global TriangleSpawnActive
    global ShapeSpawnClick
    global SpawnSquare
    global SpawnCircle
    global SpawnRectangle
    global SpawnTriangle
    global SquareSize
    global CircleSize
    global RectangleLength
    global RectangleWidth
    global TriangleSize
    if (x > -760 and x < -660 and y < -205 and y > -255):

 
        if (SquareSpawnActive == False):

            SquareSpawnActive = True
            print('square spawn active')

            ShapeSpawnClick = True
            SpawnSquare = True
            SpawnCircle = False
            SpawnTriangle = False
            SpawnRectangle = False

            writeT.goto(50,-240)
            writeT.write('Click on the canvas to draw square', align = "center",font = ('Arial', 10, 'normal'))
            print('prompted user to click on canvas')

    #check if rectangle button is clicked
    elif (x > -540 and x < -440 and y < -205 and y > -255):

        if (RectangleSpawnActive == False):
                RectangleSpawnActive = True
                print('rectangle spawn active')
    
                ShapeSpawnClick = True
                SpawnSquare = False
                SpawnCircle = False
                SpawnTriangle = False
                SpawnRectangle = True
    
                writeT.goto(50,-240)
                writeT.write('Click on the canvas to draw rectangle', align = "center",font = ('Arial', 10, 'normal'))
                print('prompted user to click on canvas')

        # if (y1 >= -100):
        #     rectangle(x = x1, y = y1, length = 100, width = 50, color = 'black', pen_thickness = pensize, turtle = brush)
        # else: 
        #     brush.write('too close to the border to produce rectangle', align = "center",font = ('Arial', 10, 'normal'))
        #     #pause for 2 seconds then delete text
        #     wn.ontimer(undoB(1), t = 1000)
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
        undoB(5)

    #check square sizer

    #check if square size -1 button is clicked
    elif (x > 45 and x < 115 and y < -260 and y > -310):
        SquareSize -= 1
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size +1 button is clicked
    elif (x > 125 and x < 195 and y < -260 and y > -310):
        SquareSize += 1
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size -10 button is clicked
    elif (x > 45 and x < 115 and y < -315 and y > -365):
        SquareSize -= 10
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size +10 button is clicked
    elif (x > 125 and x < 195 and y < -315 and y > -365):
        SquareSize += 10
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    
    #check triangle sizer
    
    #check if TriangleSize -1 button is clicked
    elif (x > 510 and x < 580 and y < -260 and y > -310):
        TriangleSize -= 1
        print(TriangleSize)
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if TriangleSize +1 button is clicked
    elif (x > 590 and x < 660 and y < -260 and y > -310):
        TriangleSize += 1
        print(TriangleSize)
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if triangle size -10 button is clicked
    elif (x > 510 and x < 580 and y < -315 and y > -365):
        TriangleSize -= 10
        print(TriangleSize)
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if triangle size +10 button is clicked
    elif (x > 590 and x < 660 and y < 225 and y > -365):
        TriangleSize += 10
        print(TriangleSize)
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))

    #check circle sizer
    #check if circle size -1 button is clicked
    elif (x > 205 and x < 275 and y < -260 and y > -310):
        CircleSize -= 1
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +1 button is clicked
    elif (x > 285 and x < 355 and y < -260 and y > -310):
        CircleSize += 1
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size -10 button is clicked
    elif (x > 205 and x < 275 and y < -315 and y > -365):
        CircleSize -= 10
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +10 button is clicked
    elif (x > 285 and x < 355 and y < -225 and y > -365):
        CircleSize += 10
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))

    #check rectangle sizer
    #check if rectangle size -1 button is clicked
    elif (x > 205 and x < 275 and y < -260 and y > -310):
        CircleSize -= 1
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +1 button is clicked
    elif (x > 285 and x < 355 and y < -260 and y > -310):
        CircleSize += 1
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size -10 button is clicked
    elif (x > 205 and x < 275 and y < -315 and y > -365):
        CircleSize -= 10
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +10 button is clicked
    elif (x > 285 and x < 355 and y < -225 and y > -365):
        CircleSize += 10
        print(CircleSize)
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    
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

#square function
def SquareSpawn(turtle,x,y, size):
    
    global ShapeSpawnClick
    global SquareSpawnActive

    turtle.setheading(0)
    turtle.pensize(pensize)
    minY = -200 + size
    print(minY)


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
        SquareSpawnActive = False
    elif (y < minY ):
        if (y > -200):
            writeT.goto(x,y+20)
            writeT.write('too close to the border to produce square', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(writeT.undo(), t = 1000)
            writeT.undo()

#rectangle function
def RectangleSpawn(turtle,x,y, length, width):
    
    global RectangleSpawnActive
    global ShapeSpawnClick
    global SpawnRectangle
    global SpawnSquare
    global SpawnCircle
    global SpawnTriangle

    turtle.setheading(0)
    turtle.pensize(pensize)
    minY = -200 + width

    if (y > minY):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for i in range(2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(width)
            turtle.right(90)
        turtle.penup()
        undoW(1)
        ShapeSpawnClick = False
        RectangleSpawnActive = False
    else:
        writeT.goto(x,y+20)
        writeT.write('too close to the border to produce rectangle', align = "center",font = ('Arial', 10, 'normal'))
        #pause for 2 seconds then delete text
        wn.ontimer(writeT.undo(), t = 1000)
        writeT.undo()


#rectangle init function
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
    rectangle(turtles[1], -320, -205, 100, 50, 'black', 1)
    turtles[1].goto(-270, -238.34)
    turtles[1].write('Clear', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -210, -205, 100, 50, 'black', 1)
    turtles[1].goto(-160, -238.34)
    turtles[1].write('Undo', align = "center",font = ('Arial', 10, 'normal'))
    

    #initalize shape size for each turtle
    for i in range(2, 6):
        shapetype = (i - 2) * 155
        turtles[i].hideturtle()
        turtles[i].penup()
        turtles[i].goto(120 + shapetype, -238.34)
        shape = ['Square', 'Circle', 'Rectangle', 'Triangle']
        rectangle(turtles[1], 45 + shapetype, -205, 150, 50, 'black', 1)
        turtles[i].write(shape[i-2] + ' Size ' + str(shapesize), align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 45 + shapetype, -260, 70, 50, 'black', 1)
        turtles[1].goto(80 + shapetype, -293.34)
        turtles[1].write('-1', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 125 + shapetype, -260, 70, 50, 'black', 1)
        turtles[1].goto(160 + shapetype, -293.34)
        turtles[1].write('+1', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 45 + shapetype, -315, 70, 50, 'black', 1)
        turtles[1].goto(80 + shapetype, -348.34)
        turtles[1].write('-10', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 125 + shapetype, -315, 70, 50, 'black', 1)
        turtles[1].goto(160 + shapetype, -348.34)
        turtles[1].write('+10', align = "center",font = ('Arial', 10, 'normal'))
        # rectangle(turtles[1], 45 + shapetype, -370, 150, 50, 'black', 1)
        # turtles[1].goto(120 + shapetype, -403.34)
        # turtles[1].write('Square', align = "center",font = ('Arial', 10, 'normal'))
    
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
        self.goto(-50,y)
        self.pencolor('blue')
        self.pendown()
        self.goto(-300,y)
        self.penup()
        for i in range(0, 11):
            self.goto(-300 + (i * 25), y)
            self.pendown()
            self.goto(-300 + (i * 25), y + 10)
            self.penup()
        self.pencolor('black')
        self.goto(-300,-300)

        self.onrelease(self.drag)
    def drag(self, x, y):
        if(x<=-37.5 and x>=-300):
            x1 = -287.5
            i = 1
            global pensize
            if (x < -275):
                self.goto(-300,-300)
                pensize = 1
            while i < 11:
                if (x >= x1 and x < x1+25):
                    self.setx(x1+12.5)
                    print(i)
                    pensize = (i * 5)
                    #write pensize on the screen


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
            SquareSpawn(brush,x,y,shapesize)
        elif (SpawnCircle == True):
            CircleSpawn(x,y)
        elif (SpawnRectangle == True):
            print('Rectangle')
            print('{},{}'.format(x,y))
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

