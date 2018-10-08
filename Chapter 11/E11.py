def swap(x, y):
    global arm
    global b
    print("before swap statement: x:", x, "y:", y)
    (a, b) = (y, x)
    print("after swap statement: x:", x, "y:", y)


arm = ["This", "is", "fun"]
b = [2, 3, 4]
print("before swap function call: a:", arm, "b:", b)
swap(arm, b)
print("after swap function call: a:", arm, "b:", b)
