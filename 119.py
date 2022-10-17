
#requirments: 4 unique shapes, varying colors and sizes, some movement associated with our art, and using loops and if statements to control our drawing
#make sure to comment on what code you worked on, virak wants this
#Later on: explain how program works and how we made it

import turtle as t
#Start Luis
shapes = ['square', 'triangle', 'circle', 'rectangle']
colors = ['red', 'blue', 'green', 'yellow'] 

# turtle object
dimond_turtle = t.Turtle()
 
# the coordinates
# of each corner
shape =((0, 0), (10, 10), (20, 0), (10, -10))
 
# registering the new shape
t.register_shape('diamond', shape)
 
# changing the shape to 'diamond'
dimond_turtle.shape('diamond')
wn = t.Screen()
wn.mainloop()
#
#oh hmmm