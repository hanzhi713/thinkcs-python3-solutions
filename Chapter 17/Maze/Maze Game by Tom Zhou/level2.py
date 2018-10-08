import pygame
init_posn = (20,250)
time_to_observe = 2000
name = "level2"


def walls_init(walls, screen,color):
    for wall in walls:
        pygame.draw.rect(screen, color, wall,0)
    pygame.display.flip()


def wall_to_rect(walls):
    rects = []
    for wall in walls:
        rects.append(pygame.Rect(wall))
    return rects
walls= [(0, 218, 277, 21), (2, 308, 269, 9), (241, 238, 4, 28), (259, 317, 12, 153), (261, 465, 198, 21),
        (354, 392, 358, 17), (275, 61, 23, 174), (297, 98, 288, 25), (382, 120, 25, 148), (337, 318, 164, 13),
        (481, 203, 238, 4), (604, 208, 17, 115), (758, 26, 23, 535), (653, 96, 40, 109), (562, 67, 93, 15),
        (536, 256, 22, 99), (563, 406, 8, 132), (144, 533, 414, 4), (145, 361, 19, 176), (129, 17, 29, 166)]
rects = wall_to_rect(walls)
teleporters = None


def win(screen):
    win_rec = pygame.Rect((40, 74, 53, 56))
    pygame.draw.rect(screen, (0,123,123), win_rec,0)
    pygame.display.flip()
    return win_rec
