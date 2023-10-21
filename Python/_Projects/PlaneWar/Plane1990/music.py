import sys
import pygame
from pygame.locals import *
import random

class Plane(pygame.sprite.Sprite):
    def __init__(self,img_file,location,speed):
        # 初始化动画精灵
        super().__init__()
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left = location[0]
        self.rect.top = location[1]
        self.speed = speed
    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0]= -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]
def collide_check(group):
    for each in group:
        each.move()
    for each in group:
        group.remove(each)
        if pygame.sprite.spritecollide(each,group,False,pygame.sprite.collide_mask):
            sound.play()
            each.speed[0] = -each.speed[0]
            each.speed[1] = -each.speed[1]
        group.add(each)
        screen.blit(each.image,each.rect)


pygame.init()
# 设置窗口大小
# FULLSCREEN 全屏模式   DOUBLEBUF 双缓冲模式
screen_size = width, height = 480, 650
screen = pygame.display.set_mode(screen_size)
# 设置标题
pygame.display.set_caption("飞机大战")
# 建立时间对象
clock = pygame.time.Clock()
# 设置背景ert()
bg = pygame.image.load("data/images/background.png").convert()
plane_list = []
# 初始化音乐
pygame.mixer.init()
# 背景音乐
pygame.mixer.music.load("data/sound/game_music.ogg")
pygame.mixer.music.play()
# 音效
sound = pygame.mixer.Sound("data/sound/get_bomb.wav")


for i in range(2):
    plane = Plane("data/images/me1.png",[100,100*i],[2*(i+1),1*(i+1)])
    plane_list.append(plane)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))

    for each in plane_list:
        each.move()
        screen.blit(each.image,each.rect)
    collide_check()
    pygame.display.flip()
    clock.tick(60)
