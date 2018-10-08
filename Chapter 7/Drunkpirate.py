import turtle

Tom = turtle.Turtle()
Wn = turtle.Screen()
coordinates = [(160, 20), (-43, 10), (270, 8), (-43, 12)]
for (x, y) in coordinates:
    Tom.forward(x)
    Tom.right(y)
Wn.mainloop()
