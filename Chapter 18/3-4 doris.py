import turtle

Doris = turtle.Turtle()
Doris.speed(0)
Doris.hideturtle()
sc = turtle.Screen()


def Sierpinski(depth, step, size):
    if step == 0:
        for i in range(3):
            Doris.forward(size)
            Doris.left(120)
    elif step == depth:
        for i in ['red', 'blue', 'yellow']:
            Doris.penup()
            Doris.forward(size)
            Doris.pendown()
            Doris.pencolor(i)
            Doris.left(120)
            Sierpinski(depth, step - 1, size / 2)
    else:
        for i in range(3):
            Doris.penup()
            Doris.forward(size)
            Doris.pendown()
            Doris.left(120)
            Sierpinski(depth, step - 1, size / 2)


Sierpinski(0, 3, 400)
sc.mainloop()
