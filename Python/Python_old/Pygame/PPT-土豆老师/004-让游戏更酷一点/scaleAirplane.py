import sys
import pygame
from pygame.locals import *

pygame.init()
speed = [0, 0]
modesList = pygame.display.list_modes()
fullscreen = False
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("controlAirplane")

obg = pygame.image.load("background.png")
background = obg

ratio = 1.0
airPlane = pygame.image.load("me1.png")
newAirplane = airPlane
airPlane_rect = airPlane.get_rect()
position = newAirplane_rect = airPlane_rect

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
                    background = pygame.transform.scale(obg, modesList[0])
                else:
                    screen = pygame.display.set_mode(screen_size)
                    background = pygame.transform.scale(obg, screen_size)
            if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
                if event.key == K_EQUALS and ratio < 2.0:
                    ratio += 0.1
                if event.key == K_MINUS and ratio >0.5:
                    ratio -= 0.1
                if event.key == K_SPACE:
                    ratio = 1.0
                newAirplane = pygame.transform.smoothscale(airPlane, \
                                             (int(airPlane_rect.width * ratio), \
                                              int(airPlane_rect.height * ratio)))
                newAirplane_rect = newAirplane.get_rect()
                position.width, position.height = newAirplane_rect.width, newAirplane_rect.height
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
    screen.blit(background, (0, 0))
    screen.blit(newAirplane,position)
    pygame.display.flip()
