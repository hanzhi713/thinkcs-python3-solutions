import pygame


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)  # Calc the absolute y distance
    dx = abs(x1 - x0)  # Calc the absolute x distance
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


def reflection_x(s1):  # return the symmetric solution about the x-axis
    s1_reflected = []
    for i in s1:
        s1_reflected.append(len(s1) - 1 - i)
    return s1_reflected


def reflection_y(s1):  # return the symmetric solution about the y-axis
    s1_reflected = list(range(len(s1)))
    for (x, y) in enumerate(s1):
        s1_reflected[len(s1) - 1 - x] = y
    return s1_reflected


def rotation_90(s1):  # return the 90 degrees rotated solution about the y-axis
    s1_rotated = list(range(len(s1)))
    for (x, y) in enumerate(s1):
        s1_rotated[y] = len(s1) - 1 - x
    return s1_rotated


def rotation_180(s1):  # return the 180 degrees rotated solution about the y-axis
    return rotation_90(rotation_90(s1))


def rotation_270(s1):  # return the 270 degrees rotated solution about the y-axis
    return rotation_180(rotation_90(s1))


def rotation_reflection_family(s1):  # return the group of all symmetric solutions
    family = [s1[:], rotation_90(s1), rotation_180(s1), rotation_270(s1), reflection_x(s1),
              reflection_y(s1), reflection_x(rotation_90(s1)), reflection_y(rotation_90(s1))]
    return family


def solutions_generator(board_size):
    import random
    rng = random.Random()  # Instantiate a generator
    bd = list(range(board_size))  # Generate the initial permutation
    num_found = 0
    tries = 0
    passed_solutions = []
    unique_solutions = []
    while num_found < 10:  # only generate the first 10 solutions
        rng.shuffle(bd)
        tries += 1
        if tries > 0.5 * board_size ** 6:  # breaks when too many trials,
            # which means all fundamental solutions have been found
            break
        if bd not in passed_solutions:
            if not has_clashes(bd):
                passed_solutions.extend(rotation_reflection_family(bd)[:])  # add all symmetric solutions to the list
                unique_solutions.append(bd[:])
                print("Found solution {0}：{1} in {2} tries.".format(num_found + 1, bd, tries))
                tries = 0
                num_found += 1
    return unique_solutions


pygame.init()


def draw_board(size, size_per_block, solutions, solution_index):
    pygame.display.set_caption('Solution {0}/{1} of {2} Queen Puzzle'  # set the title
                               .format(solution_index, len(solutions) + solution_index - 1, size))
    screen = pygame.display.set_mode([size_per_block * size, size_per_block * size])
    screen.fill([255, 255, 255])
    for y in range(0, size_per_block * size, size_per_block):  # draw the empty board
        for x in range(int((y / size_per_block) % 2) * size_per_block, size_per_block * size +
                                                                       int((y / size_per_block) % 2) * size_per_block,
                       size_per_block * 2):
            pygame.draw.rect(screen, [0, 0, 0], [x, y, size_per_block, size_per_block], 0)
    pygame.display.flip()
    queen = pygame.transform.smoothscale(pygame.image.load("Queen.png"), (size_per_block, size_per_block))
    for (x, y) in enumerate(solutions[0]):  # draw the queens on the board
        screen.blit(queen, [x * size_per_block, y * size_per_block])
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if len(solutions[1:]) == 0:
                    return
                return draw_board(size, size_per_block, solutions[1:], solution_index + 1)
                # draw the next solution when clicking the exit button


board_size = int(input("Please enter the board size (8 for example, stands for 8*8)"))
size_per_block = int(input("Please enter the size length per block (in pixels)"))
print("Only the first ten solutions will be shown.")
print("These solutions are unique, which means all rotations and reflections have been removed.")
print("Note: Close the current solution to see the next solution")
draw_board(board_size, size_per_block, solutions_generator(board_size), 1)
