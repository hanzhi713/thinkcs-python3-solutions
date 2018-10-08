import turtle

Tom = turtle.Turtle()
Tom.speed(0)
Tom.hideturtle()
sc = turtle.Screen()


def koch(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size / 3)
            t.left(angle)


def shape(t, order, size, sides):
    for i in range(sides):
        koch(t, order, size)
        t.right(360 / sides)


size = 400
Tom.penup()
Tom.goto(-size / 2, size / 2)
Tom.pendown()
shape(Tom, 3, size, 3)
sc.mainloop()
