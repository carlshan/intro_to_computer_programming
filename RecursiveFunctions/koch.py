import turtle

turtle.speed("fastest")

def koch(distance, order):
    if order == 0:
        turtle.forward(distance)
    else:
        koch(distance/3, order-1)
        turtle.left(60)
        koch(distance/3, order-1)
        turtle.right(120)
        koch(distance/3, order-1)
        turtle.left(60)
        koch(distance/3, order-1)

def snowflake(distance, order):
    for i in range(0, 3):
        koch(distance, order)
        turtle.right(120)

turtle.tracer(100)
snowflake(100, 2)
turtle.update()
turtle.done()
