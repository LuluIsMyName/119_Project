from asyncore import write
import string
from turtle import *
import turtle as t
from turtle import Turtle, Screen, goto

#1.1.9 made by Erica Lu, Luis Sanchez

wn = t.Screen()

turtle_image = "blankturtle.gif"
wn.addshape(turtle_image)

#Luis
brush = t.Turtle(shape=turtle_image)
brush.penup()
writeT = Turtle()
writeT.penup()
writeT.goto(-20, -85)
colorT = t.Turtle()
colorT.hideturtle()
colorT.penup()
turtles = ['brush','Init_T','SquareT','CircleT', 'RectangleT','TriangleT']
turtles[2] = Turtle()
turtles[3] = Turtle()
turtles[4] = Turtle()
turtles[5] = Turtle()
Drawing = False

colorname = ['black','yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 'brown', 'gray']

# brush.shape('square')

pensize = 1
shapesize = 100

#Erica & Luis
InitDone = False
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
RectangleWidth = 50
CircleSize = 100
TriangleSize = 100
Rectangle = [RectangleLength, RectangleWidth]
RectListIndex = 0       
RectangleSizeMod = 'Rectangle Length'

#Luis
#sets our base turtle color
color = 0
# colorname = 'black'

#Luis
#enables window to listen for input
wn.listen()

#Luis
#sets turtles speed to fastest
brush.speed('fastest')
writeT.speed('fastest')

#Luis
def undoB(e):
    i = 0
    while i < e:
        brush.undo()
        i += 1

#Luis
def undoW(e):
    i = 0
    while i < e:
        writeT.undo()
        i += 1

#Luis
# def TpTurtle(x,y):
#     if (y > -200):
#         brush.penup()
#         brush.goto(x,y)


#Erica & Luis
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
    global Rectangle
    global RectListIndex
    global RectangleSizeMod
    if (x > -760 and x < -660 and y < 385 and y > 335):

 
        if (SquareSpawnActive == False):

            SquareSpawnActive = True
            print('square spawn active')

            ShapeSpawnClick = True
            SpawnSquare = True
            SpawnCircle = False
            SpawnTriangle = False
            SpawnRectangle = False

            writeT.goto(-20,-85)
            writeT.write('Click on the canvas to draw square', align = "center",font = ('Arial', 10, 'normal'))
            print('prompted user to click on canvas')

    #check if rectangle button is clicked
    elif (x > -540 and x < -440 and y < 385 and y > 335):

        if (RectangleSpawnActive == False):
                RectangleSpawnActive = True
                print('rectangle spawn active')
    
                ShapeSpawnClick = True
                SpawnSquare = False
                SpawnCircle = False
                SpawnTriangle = False
                SpawnRectangle = True
    
                writeT.goto(-20,-85)
                writeT.write('Click on the canvas to draw rectangle', align = "center",font = ('Arial', 10, 'normal'))
                print('prompted user to click on canvas')

    #check if circle button is clicked
    elif (x > -650 and x < -550 and y < 385 and y > 335):
            
            if (CircleSpawnActive == False):
                CircleSpawnActive = True
                print('circle spawn active')
    
                ShapeSpawnClick = True
                SpawnSquare = False
                SpawnCircle = True
                SpawnTriangle = False
                SpawnRectangle = False
    
                writeT.goto(-20,-85)
                writeT.write('Click on the canvas to draw circle', align = "center",font = ('Arial', 10, 'normal'))
                print('prompted user to click on canvas')

    #check if triangle button is clicked
    elif (x > -430 and x < -330 and y < 385 and y > 335):

        if (TriangleSpawnActive == False):
            TriangleSpawnActive = True
            print('triangle spawn active')

            ShapeSpawnClick = True
            SpawnSquare = False
            SpawnCircle = False
            SpawnTriangle = True
            SpawnRectangle = False

            writeT.goto(-20,-85)
            writeT.write('Click on the canvas to draw triangle', align = "center",font = ('Arial', 10, 'normal'))
            print('prompted user to click on canvas')

    #check if clear button is clicked
    elif (x > -320 and x < -220 and y < 385 and y > 335):
        brush.clear()
    #check if undo button is clicked
    elif (x > -210 and x < -110 and y < 385 and y > 335):
        undoB(5)

    #check square sizer

    #check if square size -1 button is clicked
    elif (x > 45 and x < 115 and y < 330 and y > 280):
        SquareSize -= 1
        if (SquareSize < 0):
            SquareSize = 1
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size +1 button is clicked
    elif (x > 125 and x < 195 and y < 330 and y > 280):
        SquareSize += 1
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size -10 button is clicked
    elif (x > 45 and x < 115 and y < 275 and y > 225):
        SquareSize -= 10
        if SquareSize < 0:
            SquareSize = 1
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if square size +10 button is clicked
    elif (x > 125 and x < 195 and y < 275 and y > 225):
        SquareSize += 10
        print(SquareSize)
        turtles[1].clear()
        turtles[1].write("Square Size " + str(SquareSize), align = "center",font = ('Arial', 10, 'normal'))
    
    

    #check circle sizer
    #check if circle size -1 button is clicked
    elif (x > 205 and x < 275 and y < 330 and y > 280):
        CircleSize -= 1
        if (CircleSize < 0):
            CircleSize = 1
        print('Circle Size' + str(CircleSize))
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +1 button is clicked
    elif (x > 285 and x < 355 and y < 330 and y > 280):
        CircleSize += 1
        print('Circle Size' + str(CircleSize))
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size -10 button is clicked
    elif (x > 205 and x < 275 and y < 275 and y > 225):
        CircleSize -= 10
        if(CircleSize < 0):
            CircleSize = 1
        print('Circle Size' + str(CircleSize))
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if circle size +10 button is clicked
    elif (x > 285 and x < 355 and y < 275 and y > 225):
        CircleSize += 10
        print('Circle Size' + str(CircleSize))
        turtles[2].clear()
        turtles[2].write("Circle Size " + str(CircleSize), align = "center",font = ('Arial', 10, 'normal'))

    #check rectangle sizer

    #check if changing from rectangle width to rectangle length
    elif (x > 355 and x < 505 and y < 220 and y > 170): 
        if (RectListIndex == 0):
            print(Rectangle[RectListIndex])
            RectListIndex = 1
            RectangleSizeMod = 'Rectangle Width'
            turtles[3].clear()
            turtles[3].write("Rectangle Width " + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
            print('Rectangle Width ' + str(Rectangle[RectListIndex]))
        elif (RectListIndex == 1):
            RectListIndex = 0
            RectangleSizeMod = 'Rectangle Length'
            turtles[3].clear()
            turtles[3].write("Rectangle Length " + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
            print('Rectangle Length ' + str(Rectangle[RectListIndex]))
            
    #check if rectangle size -1 button is clicked
    elif (x > 365 and x < 435 and y < 330 and y > 280):
        Rectangle[RectListIndex] -= 1
        if (Rectangle[RectListIndex] < 0):
            Rectangle[RectListIndex] = 1
        print('width ' + str(Rectangle[1]))
        print('length' + str(Rectangle[0]))
        turtles[3].clear()
        turtles[3].write(RectangleSizeMod + ' ' + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
    #check if rectangle size +1 button is clicked
    elif (x > 445 and x < 515 and y < 330 and y > 280):
        Rectangle[RectListIndex] += 1
        print('width ' + str(Rectangle[1]))
        print('length' + str(Rectangle[0]))
        turtles[3].clear()
        turtles[3].write(RectangleSizeMod + ' ' + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
    #check if rectangle size -10 button is clicked
    elif (x > 365 and x < 435 and y < 275 and y > 225):
        Rectangle[RectListIndex] -= 10
        if (Rectangle[RectListIndex] < 0):
            Rectangle[RectListIndex] = 1
        print('width ' + str(Rectangle[1]))
        print('length' + str(Rectangle[0]))
        turtles[3].clear()
        turtles[3].write(RectangleSizeMod + ' ' + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
    #check if rectangle size +10 button is clicked
    elif (x > 445 and x < 515 and y < 275 and y > 225):
        Rectangle[RectListIndex] += 10
        print('width ' + str(Rectangle[1]))
        print('length' + str(Rectangle[0]))
        turtles[3].clear()
        turtles[3].write(RectangleSizeMod + ' ' + str(Rectangle[RectListIndex]), align = "center",font = ('Arial', 10, 'normal'))
    
    #check triangle sizer
    
    #check if TriangleSize -1 button is clicked
    elif (x > 510 and x < 580 and y < 330 and y > 280):
        TriangleSize -= 1
        if(TriangleSize < 0):
            TriangleSize = 1
        print(TriangleSize)
        print('Triangle Size ' + str(TriangleSize))
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if TriangleSize +1 button is clicked
    elif (x > 590 and x < 660 and y < 330 and y > 280):
        TriangleSize += 1
        print(TriangleSize)
        print('Triangle Size ' + str(TriangleSize))
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if triangle size -10 button is clicked
    elif (x > 510 and x < 580 and y < 275 and y > 225):
        TriangleSize -= 10
        if(TriangleSize < 0):
            TriangleSize = 1
        print('Triangle Size ' + str(TriangleSize))
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
    #check if triangle size +10 button is clicked
    elif (x > 590 and x < 660 and y < 275 and y > 225):
        TriangleSize += 10
        print('Triangle Size ' + str(TriangleSize))
        turtles[4].clear()
        turtles[4].write("Triangle Size " + str(TriangleSize), align = "center",font = ('Arial', 10, 'normal'))
        

#Luis
#freedraw function
def Draw(x, y):
    global Drawing
    if (InitDone == True):
        if (y < 160):
            Drawing = True
            brush.ondrag(None)
            brush.goto(x, y)
            brush.pendown()
            brush.pensize(pensize)
            brush.setheading(brush.towards(x,y))
            brush.ondrag(Draw)
            print(pensize)

#allows color to change forwards
def ColorSwitchRight():
    global color
    global colorname
    if color == 0:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 1
    elif color == 1:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 2
    elif color == 2:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 3
    elif color == 3:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 4
    elif color == 4:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 5
    elif color == 5:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 6
    elif color == 6:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 7
    elif color == 7:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 8
    elif color == 8:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 9
    elif color == 9:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 10
    elif color == 10:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 11
    elif color == 11:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 12
    elif color == 12:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 13
    elif color == 13:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 14
    elif color == 14:
        brush.color(colorname[color])
        print(colorname[color])
        color = 15
    elif color == 15:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 16
    elif color == 16:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 17
    elif color == 17:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 18
    elif color == 18:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 19
    elif color == 19:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 0

#Luis
#allows color to change backwards
def ColorSwitchLeft():
    global color
    global colorname
    if color == 0:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 19
    elif color == 1:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 0
    elif color == 2:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 1
    elif color == 3:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 2
    elif color == 4:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 3
    elif color == 5:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 4
    elif color == 6:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 5
    elif color == 7:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 6
    elif color == 8:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 7
    elif color == 9:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 8
    elif color == 10:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 9
    elif color == 11:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 10
    elif color == 12:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 11
    elif color == 13:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 12
    elif color == 14:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 13
    elif color == 15:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 14
    elif color == 16:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 15
    elif color == 17:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 16
    elif color == 18:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 17
    elif color == 19:
        brush.color(colorname[color])
        colorT.clear()
        colorT.write("color: " + colorname[color], align = "center",font = ('Arial', 10, 'normal'))
        print(colorname[color])
        color = 18
#Erica & Luis
#square function
def SquareSpawn(turtle,x,y, size):
    
    global ShapeSpawnClick
    global SquareSpawnActive

    turtle.setheading(0)
    turtle.pensize(pensize)
    maxY = 160 - size
    print(maxY)


    if (y < maxY):
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
    elif (y > maxY ):
        if (y < 160):
            writeT.goto(x,y+20)
            writeT.write('too close to the border to produce square', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(writeT.undo(), t = 1000)
            writeT.undo()

#Erica & Luis
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
    maxY = 160 - length

    if (y < maxY):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        for i in range(2):
            turtle.forward(width)
            turtle.right(90)
            turtle.forward(length)
            turtle.right(90)
        turtle.penup()
        undoW(1)
        ShapeSpawnClick = False
        RectangleSpawnActive = False
    elif (y > maxY ):
        if (y < 160):
            writeT.goto(x,y+20)
            writeT.write('too close to the border to produce rectangle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(writeT.undo(), t = 1000)
            writeT.undo()

#Erica & Luis
def CircleSpawn(turtle,x,y, radius):

    global CircleSpawnActive
    global ShapeSpawnClick
    global SpawnRectangle
    global SpawnSquare
    global SpawnCircle
    global SpawnTriangle

    turtle.setheading(270)
    turtle.pensize(pensize)
    maxY = 160 - radius

    if (y < maxY):
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.circle(radius)
        turtle.penup()
        undoW(1)
        ShapeSpawnClick = False
        CircleSpawnActive = False
    elif (y > maxY ):
        if (y < 160):
            writeT.goto(x,y+20)
            writeT.write('too close to the border to produce circle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(writeT.undo(), t = 1000)
            writeT.undo()

#Erica & Luis     
def TriangleSpawn(turtle,x,y, size):
    
        global TriangleSpawnActive
        global ShapeSpawnClick
        global SpawnRectangle
        global SpawnSquare
        global SpawnCircle
        global SpawnTriangle
    
        turtle.setheading(0)
        turtle.pensize(pensize)
        maxY = 160 - size
    
        if (y < maxY):
            turtle.penup()
            turtle.goto(x,y)
            turtle.pendown()
            for i in range(3):
                turtle.forward(size)
                turtle.right(120)
            turtle.penup()
            undoW(1)
            ShapeSpawnClick = False
            TriangleSpawnActive = False
        else:
            writeT.goto(x,y+20)
            writeT.write('too close to the border to produce triangle', align = "center",font = ('Arial', 10, 'normal'))
            #pause for 2 seconds then delete text
            wn.ontimer(writeT.undo(), t = 1000)
            writeT.undo()

#Erica & Luis
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

#Erica & Luis
#initializes the program and sets up buttons
def init():
    global InitDone
    #Luis
    turtles[1] = t.Turtle()
    turtles[1].penup()
    turtles[1].goto(-770, 160)
    turtles[1].pendown()
    turtles[1].color('black')
    turtles[1].pensize(1)
    turtles[1].speed('fastest')
    turtles[1].goto(765,160)
    rectangle(turtles[1], -760, 385, 100, 50, 'black', 1)
    turtles[1].goto(-710, 351.66)
    turtles[1].write('Square', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -650, 385, 100, 50, 'black', 1)
    turtles[1].goto(-600, 351.66)
    turtles[1].write('Circle', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -540, 385, 100, 50, 'black', 1)
    turtles[1].goto(-490, 351.66)
    turtles[1].write('Rectangle', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -430, 385, 100, 50, 'black', 1)
    turtles[1].goto(-380, 351.66)
    turtles[1].write('Triangle', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -320, 385, 100, 50, 'black', 1)
    turtles[1].goto(-270, 351.66)
    turtles[1].write('Clear', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -210, 385, 100, 50, 'black', 1)
    turtles[1].goto(-160, 351.66)
    turtles[1].write('Undo', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], -100, 385, 100, 50, 'black', 1)
    colorT.goto(-50, 351.66)
    colorT.write('Color: ' + colorname[0], align = "center",font = ('Arial', 10, 'normal'))

    #Erica
    #initalize shape size for each turtle
    for i in range(2, 6):
        shapetype = (i - 2) * 155
        turtles[i].hideturtle()
        turtles[i].penup()
        turtles[i].goto(120 + shapetype, 351.66)
        shape = ['Square Size', 'Circle Size', 'Rectangle Length', 'Triangle Size']
        rectangle(turtles[1], 45 + shapetype, 385, 150, 50, 'black', 1)
        turtles[i].write(shape[i-2] + '100', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 45 + shapetype, 330, 70, 50, 'black', 1)
        turtles[1].goto(80 + shapetype, 296.66)
        turtles[1].write('-1', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 125 + shapetype, 330, 70, 50, 'black', 1)
        turtles[1].goto(160 + shapetype, 296.66)
        turtles[1].write('+1', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 45 + shapetype, 275, 70, 50, 'black', 1)
        turtles[1].goto(80 + shapetype, 241.66)
        turtles[1].write('-10', align = "center",font = ('Arial', 10, 'normal'))
        rectangle(turtles[1], 125 + shapetype, 275, 70, 50, 'black', 1)
        turtles[1].goto(160 + shapetype, 241.66)
        turtles[1].write('+10', align = "center",font = ('Arial', 10, 'normal'))
    rectangle(turtles[1], 355, 220, 150, 50, 'black', 1)
    turtles[1].goto(430, 186.66)
    turtles[1].write('Length/Width', align = "center",font = ('Arial', 10, 'normal'))
    
    InitDone = True
    print('init done')
    if (InitDone == True):
        turtles[1].hideturtle()
        turtles.remove(turtles[1])
    mySlider = Slider(-100, 290, 'black')

#Erica
#create a square turtle to use as a slider that the user can drag to change the size of the shape
class Slider(Turtle):
    def __init__(self, x, y, color):
        Turtle.__init__(self)
        self.color(color)
        self.speed('fastest')
        self.shape('square')
        self.pensize(5)
        self.shapesize(.75,.75,.75)
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
        self.goto(-300,290)

        self.onrelease(self.drag)
    def drag(self, x, y):
        if(x<=-37.5 and x>=-300):
            x1 = -287.5
            i = 1
            global pensize
            if (x < -275):
                self.goto(-300,290)
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

#Erica & Luis
def mouseClicked(x,y):
    if (InitDone == True):
        if (ShapeSpawnClick == True):
            if (SpawnSquare == True):
                print('square')
                print('{},{}'.format(x,y))
                SquareSpawn(brush,x,y,SquareSize)
            elif (SpawnCircle == True):
                print('circle')
                print('{},{}'.format(x,y))
                CircleSpawn(brush,x,y,CircleSize)
            elif (SpawnRectangle == True):
                print('Rectangle')
                print('{},{}'.format(x,y))
                print(Rectangle[0], Rectangle[1])
                RectangleSpawn(brush,x,y, Rectangle[0], Rectangle[1])
            elif (SpawnTriangle == True):
                print('Triangle')
                print('{},{}'.format(x,y))
                TriangleSpawn(brush,x,y,TriangleSize)
        else:
            MousePos(x,y)

def PenUpBrush(x,y):
    global Drawing
    if (Drawing == True):
        brush.penup()
        Drawing = False

#Luis
#on click return cordinates
wn.onclick(mouseClicked)

#Luis
#when right click is pressed TpTurtle is called
# wn.onclick(TpTurtle, 3)

#Luis
#changes color when right or left arrow pressed
wn.onkey(ColorSwitchRight, 'Right')
wn.onkey(ColorSwitchLeft, 'Left')

#Luis
#lets turtle to draw when dragged
brush.ondrag(Draw)
brush.onrelease(PenUpBrush)

#initializes the program and makes the buttons
init()

wn.mainloop()

