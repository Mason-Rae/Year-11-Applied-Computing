#Challenge 34(Technically 33)
import turtle
wn = turtle.Screen()
tom = turtle.Turtle()
#Gets turtle and screen

def square(length):
#Defines a new function
    for a in range (4):
    #Has the line be called 4 times
        tom.forward(length)
        tom.right(90)
    wn.exitonclick()

size = int(input("Enter the length of the square: "))
square(size)
#Gets user input for square size