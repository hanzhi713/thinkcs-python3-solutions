import turtle
import random


class Point:
    # I use my point class for convenience

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def mid_point(self, target):
        return Point(0.5 * (self.x + target.x), 0.5 * (self.y + target.y))


Tom = turtle.Turtle()
Tom.speed(0)
Tom.hideturtle()
sc = turtle.Screen()
sc.colormode(255)


# draw a triangle by connecting p0-p1, p1-p2, and p2-p0, respectively
def draw_triangle(t, p0, p1, p2):
    t.penup()
    t.goto(p0.x, p0.y)
    t.pendown()
    t.goto(p1.x, p1.y)
    t.goto(p2.x, p2.y)
    t.goto(p0.x, p0.y)


def Sierpinski(t, p0, p1, p2, order, penColor="Black", colorDepth=-1):
    if colorDepth == -1:
        t.pencolor(penColor[0], penColor[1], penColor[2])
    if order <= 0:
        return
    draw_triangle(t, p0, p1, p2)
    p0_1 = p0.mid_point(p1)
    p1_2 = p1.mid_point(p2)
    p2_0 = p2.mid_point(p0)
    color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    Sierpinski(t, p0_1, p1, p1_2, order - 1, color1, colorDepth - 1)
    Sierpinski(t, p0, p0_1, p2_0, order - 1, color2, colorDepth - 1)
    Sierpinski(t, p2_0, p1_2, p2, order - 1, color3, colorDepth - 1)


Tom.pensize(1)
startPoint = Point(-400, -350)  # coordinate of the bottom left corner
size = 800  # side length of the biggest triangle
color = "Black"  # the color shown when colorDepth = -1
colorDepth = 5  # color rendering depth -- value must not exceed order - 2
# if colorDepth = order - 2, then the basic units will have distinct color
order = 7  # recursion depth
# the recursion depth

Sierpinski(Tom, startPoint, Point(startPoint.x + size / 2, startPoint.y + size / 2 * 3 ** 0.5),
           Point(startPoint.x + size, startPoint.y), order, color, colorDepth)
sc.mainloop()
