import pygame
init_posn = (20,450)
time_to_observe = 1000
name = "level1"


def walls_init(walls, screen,color):
    for wall in walls:
        pygame.draw.rect(screen, color, wall,0)
    pygame.display.flip()


def wall_to_rect(walls):
    rects = []
    for wall in walls:
        rects.append(pygame.Rect(wall))
    return rects
walls= [(0, 362, 323, 52), (0, 499, 609, 34), (312, 66, 40, 338),
        (313, 17, 478, 49), (608, 175, 27, 355), (610, 143, 188, 35)]
rects = wall_to_rect(walls)
teleporters = None


def win(screen):
    win_rec = pygame.Rect((708, 86, 53, 37))
    pygame.draw.rect(screen, (0,123,123), win_rec,0)
    pygame.display.flip()
    return win_rec
