import turtle

Tom = turtle.Turtle()
wn = turtle.Screen()
pensi = 5
Tom.pencolor("black")
Tom.speed(0)


def color_red():
    Tom.pencolor("red")


def color_green():
    Tom.pencolor("green")


def color_blue():
    Tom.pencolor("blue")


def increase_size():
    global pensi
    if pensi <= 19:
        pensi += 1
        Tom.pensize(pensi)


def decrease_size():
    global pensi
    if pensi >= 2:
        pensi -= 1
        Tom.pensize(pensi)


def move(x, y):
    Tom.goto(x, y)


wn.listen()
wn.onclick(move)
wn.onkey(color_red, "r")
wn.onkey(color_blue, "b")
wn.onkey(color_green, "g")
wn.onkeypress(increase_size, "=")
wn.onkeypress(decrease_size, "-")
wn.mainloop()
