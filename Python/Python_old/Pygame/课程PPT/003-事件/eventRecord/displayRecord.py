import sys
import pygame
from pygame.locals import *

pygame.init()
bg = (0, 0, 0)

screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("displayRecord")
screen.fill(bg)

font = pygame.font.Font(None, 20)
height_per_line = font.get_linesize()
lineHeight = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        font_surface = font.render(str(event), True, (0, 255, 0))
        screen.blit(font_surface, (0, lineHeight))
        lineHeight += height_per_line
        if lineHeight > height:
            lineHeight = 0
            screen.fill(bg)

    pygame.display.flip()
