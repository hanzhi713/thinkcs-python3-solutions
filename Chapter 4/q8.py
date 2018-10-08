import math


def area_of_circle(r):
    return r ** 2 * math.pi


while 1:
    try:
        r = float(input("Please enter the radius."))
        break
    except:
        None
print(area_of_circle(r))
