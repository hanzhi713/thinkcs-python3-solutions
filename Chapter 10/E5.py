import turtle  # Tess becomes a traffic light.

turtle.setup(400, 500)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(0)
red = turtle.Turtle()
green = turtle.Turtle()
orange = turtle.Turtle()


def draw_housing():
    """ Draw a nice housing to hold the traffic lights """
    tess.pensize(3)
    tess.color("black", "darkgrey")
    tess.begin_fill()
    tess.forward(80)
    tess.left(90)
    tess.forward(200)
    tess.circle(40, 180)
    tess.forward(200)
    tess.left(90)
    tess.end_fill()


draw_housing()


def initialization(obj, color, position):
    obj.speed(0)
    obj.forward(40)
    obj.left(90)
    obj.forward(50)
    obj.shape("circle")
    obj.shapesize(3)
    obj.fillcolor(color)
    obj.forward(position)


initialization(red, "grey", 140)
initialization(green, "grey", 0)
initialization(orange, "grey", 70)

state_num = 0
wn.listen()  # Listen for events


# 3 seconds in the Green state, followed by one second in the Green+Orange state,
# then one second in the Orange state, and then 2 seconds in the Red state.
def advance_state_machine():
    global state_num
    if state_num == 0:
        orange.fillcolor("orange")
        green.fillcolor("green")
        wn.ontimer(advance_state_machine, "1000")
        state_num = 1
    elif state_num == 1:
        green.fillcolor("grey")
        wn.ontimer(advance_state_machine, "1000")
        state_num = 2
    elif state_num == 2:
        red.fillcolor("red")
        orange.fillcolor("grey")
        wn.ontimer(advance_state_machine, "3000")
        state_num = 3
    elif state_num == 3:
        red.fillcolor("grey")
        green.fillcolor("green")
        wn.ontimer(advance_state_machine, "3000")
        state_num = 0


green.fillcolor("green")
wn.ontimer(advance_state_machine, "3000")
wn.mainloop()
