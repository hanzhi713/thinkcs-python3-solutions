import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def DrawASquare(sidelength, CentXcor, CentYcor):
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)
    Tom.goto(Tom.xcor() - sidelength / 2, Tom.ycor())
    Tom.pendown()
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.goto(Tom.xcor() + sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() - sidelength)
    Tom.goto(Tom.xcor() - sidelength, Tom.ycor())
    Tom.goto(Tom.xcor(), Tom.ycor() + sidelength / 2)
    Tom.penup()
    Tom.goto(CentXcor, CentYcor)


for i in range(20, 120, 20):
    DrawASquare(i, 0, 0)
Window.mainloop()
