import turtle

Tom = turtle.Turtle()
Tom.speed(0)
Tom.hideturtle()
sc = turtle.Screen()


def Cesaro(t, order, size, al):
    if order == 0:
        t.forward(size)
    else:
        for angle in [90 - al, -(180 - 2 * al), 180 - (90 + al), 0]:
            Cesaro(t, order - 1, size / 2, al)
            t.right(angle)


def shape(t, order, size, al, sides):
    for i in range(sides):
        Cesaro(t, order, size, al)
        t.right(360 / sides)


size = 400
Tom.penup()
Tom.goto(-size / 2, size / 2)
Tom.pendown()
shape(Tom, 4, size, 5, 4)
sc.mainloop()
