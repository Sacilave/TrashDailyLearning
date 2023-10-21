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
        self.mask = pygame.mask.from_surface(self.image)
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
def collide_check(group):
    for plane in group:
        plane.move()
    for plane in group:
        group.remove(plane)
        if pygame.sprite.spritecollide(plane, group, False, pygame.sprite.collide_mask):
            plane.speed[0] = -plane.speed[0]
            plane.speed[1] = -plane.speed[1]
            collide_voice = pygame.mixer.Sound("get_bomb.wav")
            collide_voice.set_volume(0.2)
            collide_voice.play()
        group.add(plane)
        screen.blit(plane.image, plane.rect)

pygame.init()
pygame.mixer.init()
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("AirplaneSprite")
background = pygame.image.load("background.png").convert()
pygame.mixer.music.load("game_music.ogg")
pygame.mixer.music.play(-1)
volumeNum = 1
imgs = ["me1.png", "enemy1.png", "enemy2.png"]
img_file = "me1.png"
group = pygame.sprite.Group()
speed = [2, 2]
for i in range(3):
    location_img = [i *120, 10]
    speed = [choice([-2, 2]), choice([-2, 2])]
    airplane = PlaneClass(imgs[i], location_img, speed)
    group.add(airplane)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP and volumeNum < 1:
                volumeNum += 0.1
            if event.key == K_DOWN and volumeNum > 0:
                volumeNum -= 0.1
            pygame.mixer.music.set_volume(volumeNum)
    screen.blit(background, (0, 0))
    collide_check(group)
    pygame.display.flip()
    clock.tick(30)
