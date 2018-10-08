import math

help(math)

# (a)
# 44

# (b)
# math.ceil(x)
''' Return the ceiling of x as an Integral
This is the smallest integer >= x.'''

# math.floor(x)
'''Return the floor of x as an Integral
This is the largest integer <=x '''

# (c) By using Newton's algorithm
'''def sqrt(n):
    approx = n/2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better'''

# (d)
math.pi
math.e
