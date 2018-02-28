import turtle

turtle.speed("fast")

angle = 117

for step in range(0, 500):
    turtle.forward(step)
    turtle.right(angle)


turtle.mainloop()
