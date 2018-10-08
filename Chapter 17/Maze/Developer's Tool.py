# -*- coding: utf-8 -*-
import pygame
import sys

pygame.init()
screen = pygame.display.set_mode([800, 600])
font = pygame.font.SysFont("Calibri", 20)
lc = []
index = -1
rect_result = []
Instructions = ['Instructions:', 'You can draw a rectangle by clicking on two distinct points',
                'Press the key E to undo the last drawing', 'Press C to clear the screen',
                'Press Q to generate the rectangle coordinate lists of the rectangles that have already drawn', '']
for instru in Instructions:
    print(instru)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(pygame.Rect((172, 312, 320, -129)).colliderect((348, 463, 252, -232)))
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            lc.append(pygame.mouse.get_pos())
            index += 1
            pygame.draw.circle(screen, (0, 255, 0), lc[index], 5, 0)
            pygame.display.flip()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, (0, 0, 0), (100, 500, 130, 40))
            text_surface = font.render("x:{0}, y:{1}".format(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]),
                                       True, (0, 0, 255))
            screen.blit(text_surface, (100, 500))
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rect_result = []
                for i in range(0, len(lc), 2):
                    width = lc[i][0] - lc[i + 1][0]
                    height = lc[i][1] - lc[i + 1][1]
                    if width > 0:
                        if height > 0:
                            rect_result.append((lc[i + 1][0], lc[i + 1][1], width, height))
                        else:
                            rect_result.append((lc[i + 1][0], lc[i + 1][1] + height, width, -height))
                    if width < 0:
                        if height > 0:
                            rect_result.append((lc[i][0], lc[i][1] - height, -width, height))
                        else:
                            rect_result.append((lc[i][0], lc[i][1], -width, -height))
                print(rect_result)
            elif event.key == pygame.K_e:
                if len(lc) >= 2:
                    width = lc[index - 1][0] - lc[index][0]
                    height = lc[index - 1][1] - lc[index][1]
                    pygame.draw.rect(screen, (0, 0, 0), (lc[index - 1][0], lc[index - 1][1], -width, -height), 0)
                    lc = lc[:len(lc) - 2]
                    index -= 2
                    pygame.display.flip()
            elif event.key == pygame.K_c:
                screen.fill([0, 0, 0])
                index = -1
                lc = []
                pygame.display.flip()
        if len(lc) % 2 == 0 and len(lc) > 0:
            width = lc[index - 1][0] - lc[index][0]
            height = lc[index - 1][1] - lc[index][1]
            pygame.draw.rect(screen, (255, 255, 255), (lc[index - 1][0], lc[index - 1][1], -width, -height))
            pygame.display.flip()
