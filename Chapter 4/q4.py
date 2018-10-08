import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()
Tom.speed(10)


def draw_square(rotation, radius):
    Tom.left(rotation)
    Tom.fd(radius)
    Tom.left(90)
    Tom.fd(radius)
    for i in range(0, 3):
        Tom.left(90)
        Tom.fd(2 * radius)
    Tom.left(90)
    Tom.fd(radius)
    Tom.home()


for i in range(0, 360, 20):
    draw_square(i, 100)
Window.mainloop()
