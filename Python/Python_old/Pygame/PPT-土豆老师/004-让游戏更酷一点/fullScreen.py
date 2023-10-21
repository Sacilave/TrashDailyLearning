import sys
import pygame
from pygame.locals import *

pygame.init()
bg = (0, 255, 0)
speed = [0, 0]
modesList = pygame.display.list_modes()
fullscreen = False
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("controlAirplane")
screen.fill(bg)

airPlane = pygame.image.load("me1.png")
position = airPlane.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
        if event.type ==  KEYDOWN:
            if event.key == K_LEFT:
                speed = [-1, 0]
            if event.key == K_RIGHT:
                speed = [1, 0]
            if event.key == K_UP:
                speed = [0, -1]
            if event.key == K_DOWN:
                speed = [0, 1]
            if event.key == K_F11:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(modesList[0], FULLSCREEN | HWSURFACE)
                else:
                    screen = pygame.display.set_mode(screen_size)
        else:
            speed = [0, 0]
    if position.left < 0:
        position.left = 0
    if fullscreen == True and position.right > modesList[0][0]:
        position.right = modesList[0][0]
    elif fullscreen == False and position.right > width:
        position.right = width
    if position.top <0:
        position.top = 0
    if fullscreen == True and position.bottom > modesList[0][1]:
        position.bottom = modesList[0][1]
    elif fullscreen == False and position.bottom > height:
        position.bottom = height
    position = position.move(speed)
    screen.fill(bg)
    screen.blit(airPlane,position)
    pygame.display.flip()
