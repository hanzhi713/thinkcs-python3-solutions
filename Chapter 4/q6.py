import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def draw_poly(t, n, z):
    for i in range(0, n):
        t.forward(z)
        t.left(360 / n)


def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)


draw_equitriangle(Tom, 100)
Window.mainloop()
