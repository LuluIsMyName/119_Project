
# #i've done extensive research on how to perform certain tasks we were not taught yet which is why you might not recognize some of these built in functions
# #the turtle module is a more restricted version of the tkinter module, which is why i'm using tkinter to several windows
# turtle = t
# wn = t.Screen()

# brush = t.Turtle()

# #this Drag function prevents the the turtle from glitching out all over the place because you've dragged it too fast. 
# def Drag(x,y):
#     brush.ondrag(None) #makes the turtle, brush, stop performing the drag function
#     brush.setheading(brush.towards(x,y)) #makes the turtle face the direction of the mouse
#     brush.goto(x,y) #makes the turtle go to the mouse's position
#     brush.ondrag(Drag) #makes the turtle, brush, perform the drag function again
#     #this process is repeated over and over again until the mouse is released and makes the brush move pixel by pixel thus making it look like it's drawing smoothly



# wn.listen() #makes the window "listen" for the mouse to be clicked
# brush.speed('fastest') #makes the turtle, brush, move as fast as possible
# brush.ondrag(Drag) #makes the turtle, brush, perform the drag function