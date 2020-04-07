import pygame
import random

pygame.init()

win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Dimcun")

run = True

blue = (0, 0, 255)
red = (255, 0, 0)

x1 = 300
y1 = 300
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_a:
                y1_change = 0
                x1_change = -10
            elif event.key == pygame.K_d:
                y1_change = 0
                x1_change = 10
            elif event.key == pygame.K_s:
                y1_change = 10
                x1_change = 0
    x1 += x1_change
    y1 += y1_change
    win.fill((0,0,0))
    pygame.draw.rect(win, (55,55,55), [0, 0, 0, 800],10)
    pygame.draw.rect(win, (55, 55, 55), [0, 600, 800, 600], 10)
    pygame.draw.rect(win, blue, [x1, y1, 10, 10])
    pygame.display.update()

    clock.tick(15)
pygame.quit()
quit()
