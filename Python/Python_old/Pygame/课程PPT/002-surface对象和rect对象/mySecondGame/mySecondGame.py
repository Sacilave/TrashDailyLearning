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
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    position = position.move(speed)
    if position.left < 0 or position.right > width:
        heroPlane = pygame.transform.flip(heroPlane, True, False)
        speed[0] = -speed[0]
    if position.top <0 or position.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(heroPlane, position)
    pygame.display.flip()
    clock.tick(40)
