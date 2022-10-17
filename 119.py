from turtle import *
from tkinter import *
import turtle as t

#i've done extensive research on how to perform certain tasks we were not taught yet which is why you might not recognize some of these built in functions
#the turtle module is a more restricted version of the tkinter module, which is why i'm using tkinter to several windows
#extensive research is made of reviewing tkinter and turtle documentation along with python documentation on classes
turtle = t
wn = t.Screen()

brush = t.Turtle()

#this Drag function prevents the the turtle from glitching out all over the place because you've dragged it too fast. 
def Drag(x,y):
    brush.ondrag(None) #makes the turtle, brush, stop performing the drag function
    brush.setheading(brush.towards(x,y)) #makes the turtle face the direction of the mouse
    brush.goto(x,y) #makes the turtle go to the mouse's position
    brush.ondrag(Drag) #makes the turtle, brush, perform the drag function again
    #this process is repeated over and over again until the mouse is released and makes the brush move pixel by pixel thus making it look like it's drawing smoothly


wn.listen() #makes the window "listen" for the mouse to be clicked
brush.speed('fastest') #makes the turtle, brush, move as fast as possible
brush.ondrag(Drag) #makes the turtle, brush, perform the drag function

#dont uncomment this part down here
# class Window(Tk):
#     def __init__(self, title, geometry):
#         super().__init__()
#         self.running = True
#         self.geometry(geometry)
#         self.title(title)
#         self.protocol("WM_DELETE_WINDOW", self.destroy_window)
#         self.canvas = Canvas(self)
#         self.canvas.pack(side=LEFT, expand=True, fill=BOTH)
#         self.turtle = RawTurtle(TurtleScreen(self.canvas))

#     def update_window(self):
#         if self.running:
#             self.update()

#     def destroy_window(self):
#         self.running = False
#         self.destroy()


# # create windows
# win1 = Window('Turtle Window 1', '640x480+0+0')
# win2 = Window('Turtle Window 2', '640x480+650+0')

# # assign turtles
# t1 = win1.turtle
# t2 = win2.turtle

# # draw stuff
# t1.pendown()
# t1.forward(100)
# t2.pendown()
# t2.backward(100)

# # update windows (the mainloop)
# while win1.running or win2.running:
#     win1.update_window()
#     win2.update_window()
#dont uncomment this code up here

wn.mainloop()