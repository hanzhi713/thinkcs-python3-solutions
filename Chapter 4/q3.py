import turtle

Window = turtle.Screen()
Tom = turtle.Turtle()


def draw_poly(t, n, z):
    for i in range(0, n):
        t.forward(z)
        t.left(360 / n)


draw_poly(Tom, 8, 50)
Window.mainloop()
