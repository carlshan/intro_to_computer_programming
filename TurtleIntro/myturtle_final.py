import turtle

turtle.speed('fastest')

angle = 117

for step in range(0, 500):
    turtle.forward(step)
    turtle.right(angle)

turtle.mainloop()
