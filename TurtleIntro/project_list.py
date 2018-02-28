import turtle
import random

turtle.speed('fastest')

colors = ['red', 'green', 'black', 'orange']

angle = 117
for step in range(0, 500):
    turtle.forward(step)
    turtle.right(angle)
    if step % 50 == 0:
        new_color = random.choice(colors)
        turtle.color(new_color)

turtle.mainloop()
