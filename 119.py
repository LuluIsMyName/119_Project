from turtle import *
from tkinter import *
import tkinter as tk
import turtle as t

#i've done extensive research on how to perform certain tasks we were not taught yet which is why you might not recognize some of these built in functions
#the turtle module is a more restricted version of the tkinter module, which is why i'm using tkinter to initiate several windows
#extensive research was done reviewing tkinter and turtle documentation along with python documentation on classes

#initiates 2 seperate windows
class Window(Tk): 
    def __init__(self, title, geometry):
        super().__init__() 
        self.running = True
        self.geometry(geometry) 
        self.title(title) 
        self.protocol("WM_DELETE_WINDOW", self.destroy_window) 
        self.canvas = Canvas(self)
        self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
        self.turtle = RawTurtle(TurtleScreen(self.canvas))


    def update_window(self): #updates the window
        if self.running:
            self.update()

    def destroy_window(self): #destroys the window
        self.running = False
        self.destroy()


# create windows
win1 = Window('Turtle Window 1', '640x480')
win2 = Window('Turtle Window 2', '640x480+650+0')

# assign turtles
t1 = win1.turtle
t2 = win2.turtle
t1.shape('circle')
t1.shapesize(0.5,0.5,0.5)

def t2rectangle(x, y, width, height, color):
    t2.fillcolor(color)
    t2.begin_fill()
    t2.goto(x, y)
    t2.goto(x + width, y)
    t2.goto(x + width, y + height)
    t2.goto(x, y + height)
    t2.goto(x, y)
    t2.end_fill()
def t2circle(x, y, radius, color):
    t2.fillcolor(color)
    t2.begin_fill()
    t2.goto(x, y)
    t2.circle(radius)
    t2.end_fill()
def t2triangle(x, y, width, height, color):
    t2.fillcolor(color)
    t2.begin_fill()
    t2.goto(x, y)
    t2.goto(x + width, y)
    t2.goto(x + width, y + height)
    t2.goto(x, y)
    t2.end_fill()
def t2square(x, y, width, color):
    t2.fillcolor(color)
    t2.begin_fill()
    t2.goto(x, y)
    t2.goto(x + width, y)
    t2.goto(x + width, y + width)
    t2.goto(x, y + width)
    t2.goto(x, y)
    t2.end_fill()

#draws when turtle dragged
def Drag(x,y):
    t1.ondrag(None)
    t1.setheading(t1.towards(x,y)) 
    t1.goto(x,y) 
    t1.ondrag(Drag) 

#when window 2 is clicked checks if clicked on box
def Win2Click(x,y):
    t2.goto(x,y)
    if (t2.xcor() > 0 and t2.xcor() < 100 and t2.ycor() > 0 and t2.ycor() < 100):
        t2.write("You clicked the red box", font=("Arial", 16, "normal"))

#turtle calls Drag function when dragged
t1.ondrag(Drag)

def Turtle2Pos(x,y):
    print('{}, {}'.format(x, y))
    t2square(x, y, 100, 'red')
t2.screen.onclick(Turtle2Pos)



#sets turtle speed to fastest
t1.speed('fastest') 
t2.speed('fastest')

# update windows (the mainloop)
while win1.running or win2.running:
    win1.update_window()
    win2.update_window()

