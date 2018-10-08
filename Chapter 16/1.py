from unit_tester import test


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def flip(self):
        (self.height, self.width) = (self.width, self.height)

    def contains(self, point):
        if 0 <= point.x - self.corner.x < self.width and 0 <= point.y - self.corner.y < self.height:
            return True
        else:
            return False

    def if_collision(self, rect2):
        flag = abs(self.corner.x - rect2.corner.x) < max(self.width, rect2.width) and \
               abs(self.corner.y - rect2.corner.y) < max(self.height, rect2.height)
        return flag


# These tests have passed
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.area() == 50)
# test(r.perimeter() == 30)
# r = Rectangle(Point(100, 50), 10, 5)
# test(r.width == 10 and r.height == 5)
# r.flip()
# test(r.width == 5 and r.height == 10)
# r = Rectangle(Point(0, 0), 10, 5)
# test(r.contains(Point(0, 0)))
# test(r.contains(Point(3, 3)))
# test(not r.contains(Point(3, 7)))
# test(not r.contains(Point(3, 5)))
# test(r.contains(Point(3, 4.99999)))
# test(not r.contains(Point(10,5)))
# test(not r.contains(Point(-3, -3)))
#
# g = Rectangle(Point(8.9, -3.9), 9, 4)
# test(g.if_collision(r))
r = Rectangle(1, 1, 1)
r.move(1, 1)
