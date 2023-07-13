# DVD-Logo
DVD logo

import pygame
import os

window = pygame.display.set_mode((500,500))

x = 100
y = 0

running = True

while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
    x += 1

    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

    pygame.display.quit()

    window = pygame.display.set_mode((501,500))
    pygame.display.update()
pygame.quit()