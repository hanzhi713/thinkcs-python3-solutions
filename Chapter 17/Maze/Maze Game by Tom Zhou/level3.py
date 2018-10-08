import pygame
init_posn = (50,570)
time_to_observe = 1000
name = "level3"


def walls_init(walls, screen,color):
    for wall in walls:
        pygame.draw.rect(screen, color, wall,0)
    pygame.display.flip()


def wall_to_rect(walls):
    rects = []
    for wall in walls:
        rects.append(pygame.Rect(wall))
    return rects
walls= [(0, 517, 272, 16), (341, 372, 15, 225), (180, 441, 92, 13), (77, 360, 23, 169),
        (108, 281, 248, 2), (270, 284, 26, 130), (427, 161, 11, 202), (352, 448, 164, 18),
        (435, 274, 133, 3), (562, 277, 3, 322), (265, 196, 164, 1), (250, 192, 18, 90),
        (0, 189, 123, 8), (72, 109, 324, 4), (68, 17, 9, 95), (501, 4, 7, 265), (136, 33, 59, 47),
        (506, 93, 177, 7), (724, 0, 18, 214), (622, 211, 115, 1), (566, 340, 134, 7), (622, 275, 2, 59),
        (709, 415, 3, 115), (611, 420, 97, 1), (608, 421, 1, 107), (746, 464, 51, 5)]
rects = wall_to_rect(walls)
teleporters = [(wall_to_rect([(136, 33, 59, 47)])[0], (535, 24))]


def win(screen):
    win_rec = pygame.Rect((637, 458, 51, 47))
    pygame.draw.rect(screen, (0,123,123), win_rec,0)
    pygame.display.flip()
    return win_rec
