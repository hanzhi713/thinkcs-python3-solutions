import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()
Tom.hideturtle()
Tom.speed(0)


def Spirals(increment, angle):
    x = 3
    for i in range(0, 180):
        Tom.forward(x)
        Tom.left(angle)
        x += increment


Spirals(10, 150)
Window.mainloop()
