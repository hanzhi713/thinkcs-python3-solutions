# This is a template of a maze level
# For your convenience, developer's tool is available for graphically design the level
# You can acquire the coordinate list directly from this tool and copy it here


import pygame


# Some important constants:
# init_posn = (50,570)
# spawn position
# time_to_observe = 3000
# time in milliseconds for player to observe the walls before they disappear
# name = "level4"
# level name

# let wall to be draw on the screen
def walls_init(walls, screen, color):
    for wall in walls:
        pygame.draw.rect(screen, color, wall, 0)
    pygame.display.flip()


# generate the collide box of the walls
def wall_to_rect(walls):
    rects = []
    for i in range(len(walls)):
        # if i == -- or --:
        #   continue
        # if specific walls are penetrable, add indices here to remove it from the collide box
        # penetrable walls will appear on the screen, but they don't have the collide box
        rects.append(pygame.Rect(walls[i]))
    return rects


walls = []  # coordinate list of the walls and teleporters. DO NOT ADD WIN BLOCK HERE!
rects = wall_to_rect(walls)  # walls collide box
teleporters = None  # if the player meets the teleporter, he will be immediately teleported to another position


# teleporters = [(wall_to_rect([(136, 33, 59, 47)])[0],(535,24))]
# a template of how to create a teleporter
# teleporters = [(wall_to_rect([(YOUR_TELEPORTER_RECT)])[0], (Destination_POS_X, Destination_POS_Y)), ……]
# remember to add your teleporters to the wall list


# draw the win block and generate its collide box
def win(screen):
    win_rec = pygame.Rect((637, 458, 51, 47))  # set the win block here
    pygame.draw.rect(screen, (0, 123, 123), win_rec, 0)  # set the color here (R, G, B)
    pygame.display.flip()
    return win_rec
