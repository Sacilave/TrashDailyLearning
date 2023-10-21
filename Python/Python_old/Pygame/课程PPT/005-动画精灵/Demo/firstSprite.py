import sys
import pygame
from pygame.locals import *

class PlaneClass(pygame.sprite.Sprite):
    def __init__(self, img_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

pygame.init()
screen_size = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("AirplaneSprite")
background = pygame.image.load("background.png").convert()
screen.blit(background, (0, 0))
img_airplane = "me1.png"
airplanes = []
for i in range(3):
    location_img = [i *100, 10]
    airplane = PlaneClass(img_airplane, location_img)
    airplanes.append(airplane)
for each in airplanes:
    screen.blit(each.image, each.rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()

