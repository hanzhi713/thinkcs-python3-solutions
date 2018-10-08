import time


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # CXalc the absolute x distance
    return dx == dy  # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):  # Look at all columns to the left of c
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False  # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def reflection_x(s1):
    s1_reflected = []
    for i in s1:
        s1_reflected.append(len(s1) - 1 - i)
    return s1_reflected


def reflection_y(s1):
    s1_reflected = list(range(len(s1)))
    for (x, y) in enumerate(s1):
        s1_reflected[len(s1) - 1 - x] = y
    return s1_reflected


def rotation_90(s1):
    s1_rotated = list(range(len(s1)))
    for (x, y) in enumerate(s1):
        s1_rotated[y] = len(s1) - 1 - x
    return s1_rotated


def rotation_180(s1):
    return rotation_90(rotation_90(s1))


def rotation_270(s1):
    return rotation_180(rotation_90(s1))


def rotation_reflection_family(s1):
    family = [s1[:], rotation_90(s1), rotation_180(s1), rotation_270(s1), reflection_x(s1), reflection_y(s1),
              reflection_x(rotation_90(s1)), reflection_y(rotation_90(s1))]
    return family


def solutions_generator(board_size):
    import random
    rng = random.Random()  # Instantiate a generator
    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    passed_solutions = []
    unique_solutions = []
    while True:
        t = time.clock()
        rng.shuffle(bd)
        tries += 1
        if tries > 100000:
            break
        if bd not in passed_solutions:
            if not has_clashes(bd):
                passed_solutions.extend(rotation_reflection_family(bd)[:])
                unique_solutions.append(bd[:])
                print("Found solution {0} in {1} tries.".format(bd, tries))
                tries = 0
                num_found += 1


solutions_generator(15)
