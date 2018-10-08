coordinates = [(-100, -100), (100, 100), (100, -100), (-100, -100), (-100, 100), (100, 100), (0, 200), (-100, 100),
               (100, -100)]
import turtle

Tom = turtle.Turtle()
Wn = turtle.Screen()
Tom.penup()
Tom.goto(-100, -100)
Tom.pendown()
for (x, y) in coordinates:
    Tom.goto(x, y)
Wn.mainloop()
