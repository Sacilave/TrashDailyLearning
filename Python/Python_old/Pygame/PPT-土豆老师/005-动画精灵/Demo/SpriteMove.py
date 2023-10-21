import sys
import pygame
from pygame.locals import *
from random import *

class PlaneClass(pygame.sprite.Sprite):
    def __init__(self, img_file, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

pygame.init()
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("AirplaneSprite")
background = pygame.image.load("background.png").convert()

imgs = ["me1.png", "enemy1.png", "enemy2.png", "enemy3_n1.png"]
airplanes = []
speed = [2, 2]
for i in range(4):
    location_img = [i *100, 10]
    speed = [choice([-2, 2]), choice([-2, 2])]
    airplane = PlaneClass(imgs[i], location_img, speed)
    airplanes.append(airplane)

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.time.delay(10)
    screen.blit(background, (0, 0))
    for each in airplanes:
        each.move()
        screen.blit(each.image, each.rect)
    pygame.display.flip()



