class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at the origin """
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def set_cor(self, x=None, y=None):
        if x is None: x = self.x
        if y is None: y = self.y
        self.x = x
        self.y = y

    def get_distance(self, target=None):
        if target is None: target = Point(0, 0)
        return ((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5

    def print_coor(self):
        print("({0}, {1})".format(self.x, self.y))

    def mid_point(self, target):
        return Point(0.5 * (self.x + target.x), 0.5 * (self.y + target.y))

    def get_slope(self, target=None):
        if target is None: target = Point(0, 0)
        return (self.y - target.y) / (self.x - target.x)

    def reflect_x(self):
        return Point(self.x, -self.y)

    def get_line_to(self, point):
        slope = self.get_slope(point)
        print("y = {0}x + {1}".format(slope, point.y - slope * point.x))
        return (slope, point.y - slope * point.x)

    def get_perpendicular_bisector(self, point):
        slope = self.get_slope(point)
        midpoint = self.mid_point(point)
        print("y = {0}x + {1}".format(-1 / slope, midpoint.y + (1 / slope) * midpoint.x))
        return (-1 / slope, midpoint.y + (1 / slope) * midpoint.x)

    def get_center_of_circle(self, p1, p2):
        coeff1 = self.get_perpendicular_bisector(p1)
        coeff2 = self.get_perpendicular_bisector(p2)
        x_coor = (coeff2[1] - coeff1[1]) / (coeff1[0] - coeff2[0])
        return Point(x_coor, x_coor * coeff1[0] + coeff1[1])


print(Point(4, 11).get_line_to(Point(6, 15)))
print(Point(0, 1).get_center_of_circle(Point(1, 0), Point(-1, 0)))
