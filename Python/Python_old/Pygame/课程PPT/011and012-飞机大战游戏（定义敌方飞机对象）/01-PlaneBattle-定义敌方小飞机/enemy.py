'''
定义敌方飞机的对象，并在对象中定义飞机图像的矩形、位置、速度等特性值，以及定义敌方飞机移动的方法
敌方飞机包含小型飞机、中型飞机、大型飞机
'''
import pygame
from random import *
#定义小型敌机的对象
class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = screen_size[0], screen_size[1]
        self.speed = 2  #可以通过修改速度来提高游戏的难度
        #小型敌机出现的位置是随机的
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-5*self.height,0)
    #定义小型敌机移动的方法
    def move(self):
        if self.rect.top < self.height - 60:
            self.rect.top +=  self.speed
        else:
            self.reset()   #当某一个小型敌机飞出窗口后，重新生成
    #定义重新生成小型敌机的方法，重新生成敌机的位置是随机的
    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-5*self.height,0)
