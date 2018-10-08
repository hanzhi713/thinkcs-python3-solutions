import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([800, 600])
screen.fill([0, 0, 0])


class Me:

    def __init__(self, x=0, y=0):
        self.image = pygame.transform.smoothscale(pygame.image.load("me.png"), (15, 15))
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (15, 15))
        screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self, x, y, rects, win, teleporters=None):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        self.x += x
        self.y += y
        if self.x > 785:
            self.x = 785
        if self.x < 0:
            self.x = 0
        if self.y > 585:
            self.y = 585
        if self.y < 0:
            self.y = 0
        self.rect = pygame.Rect((self.x, self.y), (15, 15))
        if teleporters is not None:
            for (teleporter, posn) in teleporters:
                if self.rect.colliderect(teleporter):
                    self.x = posn[0]
                    self.y = posn[1]
                    screen.blit(self.image, (self.x, self.y))
                    self.rect = pygame.Rect((self.x, self.y), (15, 15))
                    pygame.display.flip()
                    return
        for rect in rects:
            if self.rect.colliderect(rect):
                self.x -= x
                self.y -= y
                self.rect = pygame.Rect((self.x, self.y), (15, 15))
                return
        if self.rect.colliderect(win):
            print("You win!!!")
            screen.fill([0, 0, 0])
            pygame.display.flip()
            return True
        self.rect = pygame.Rect((self.x, self.y), (15, 15))
        screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def abs_movement(self, x, y):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)
        self.x = x
        self.y = y
        screen.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect((self.x, self.y, 15, 15))
        pygame.display.flip()


me = Me()


def wait_SPACE_key():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return


def main(level, rects, win, init_posn, time, teleporters=None):
    me.abs_movement(init_posn[0], init_posn[1])
    pygame.display.set_caption(level.name)
    pygame.display.flip()
    print("Press SPACE to start observe the maze. You have {0} seconds".format(time / 1000))
    wait_SPACE_key()
    level.walls_init(level.walls, screen, (255, 255, 255))
    pygame.time.delay(time)
    level.walls_init(level.walls, screen, (0, 0, 0))
    pygame.display.flip()
    x_movement = 0
    y_movement = 0
    while True:
        result = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    result = me.move(0, -1, rects, win, teleporters)
                    y_movement = -1
                elif event.key == pygame.K_a:
                    x_movement = -1
                elif event.key == pygame.K_s:
                    y_movement = 1
                elif event.key == pygame.K_d:
                    result = me.move(1, 0, rects, win, teleporters)
                    x_movement = 1
                pygame.time.delay(2)
            elif event.type == pygame.KEYUP:
                x_movement = 0
                y_movement = 0
        # result = me.move(x_movement, y_movement, rects, win, teleporters)
        if result:
            break


def next_level(level):
    print("Press SPACE to enter the next level")
    wait_SPACE_key()
    screen.fill([0, 0, 0])
    pygame.display.flip()
    win_rect = level.win(screen)
    walls_Rect = level.rects
    pygame.display.flip()
    teleporters = level.teleporters
    main(level, walls_Rect, win_rect, level.init_posn, level.time_to_observe, teleporters)


instructions = ['Invisible Maze:', 'Use WASD to move', 'You cannot go through walls in MOST OF THE CASES',
                'Reach the win block, which will be appeared on the screen, to win',
                'Walls may be invisible', 'Teleporters may exist in later levels', '']
for ins in instructions:
    print(ins)
import level1

next_level(level1)

import level2

next_level(level2)

import level3

next_level(level3)

# import level4
# next_level(level4)

print("Congratulations! This is the end of the game")
