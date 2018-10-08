import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def star(sides, sidelength):
    for i in range(0, sides):
        Tom.forward(sidelength)
        Tom.right(2 * (360 / sides))


for i in range(0, 5):
    Tom.left(144)
    Tom.forward(350)
    star(5, 100)
Window.mainloop()
