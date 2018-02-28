import turtle

screen = turtle.Screen()

turtle.speed("fastest")

def square():
    for i in range(0, 4):
        turtle.forward(50)
        turtle.right(90)

screen.onkey(square, "Up")
screen.listen()

turtle.mainloop()
