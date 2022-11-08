#   a123_apple_letters.py
import turtle as t
import random

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen 
wn = t.Screen()
wn.bgpic("background.gif")
apple_image = "apple.gif"
wn.addshape(apple_image)
number_of_apples = 5
t_list = []
letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", 
"l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters
for i in range(0, number_of_apples):
    #TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
    # calling your function that resets the apples by giving them a new random location
    # add the new apples to a list of apples to be used in the rest of the program.
    t_list.append(t.Turtle())
    t_list[i].shape(apple_image)
    t_list[i].penup()
    t_list[i].goto(random.randint(-200,200),random.randint(-200,200))
    t_list[i].showturtle()
    #TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter 
    # list and draws that letter on that turtle (apple)
    t_list[i].write(letter_list[random.randint(0,25)], font=("Arial", 16, "normal"))
Apple = t.Turtle(shape=apple_image)


# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
# for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.

wn.listen()
wn.mainloop()