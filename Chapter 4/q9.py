import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def star(sides, sidelength):
    for i in range(0, sides):
        Tom.forward(sidelength)
        Tom.right(2 * (360 / sides))


star(int(input("Please enter the number of sides, odd number only.")), int(input("Please define the side length.")))
Window.mainloop()
