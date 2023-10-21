import sys
import pygame
from pygame.locals import *

pygame.init()
screen_size = width, height = 480, 700
bg = (0, 255, 0)
speed = [1, 1]

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("myFirstGame")
heroPlane = pygame.image.load("me1.png")
position = heroPlane.get_rect()
print(position)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    position = position.move(speed)
    screen.fill(bg)
    screen.blit(heroPlane, position)
    pygame.display.flip()

