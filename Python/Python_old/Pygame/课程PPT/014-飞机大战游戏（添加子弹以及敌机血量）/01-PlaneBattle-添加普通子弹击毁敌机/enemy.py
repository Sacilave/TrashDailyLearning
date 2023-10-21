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
        #加载小型敌机坠毁动画图片，并保存到列表中，动画即几幅图片的顺序切换
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy1_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy1_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = screen_size[0], screen_size[1]
        self.speed = 2  #可以通过修改速度来提高游戏的难度
        self.active = True  #敌机的状态标记
        #小型敌机出现的位置是随机的
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-5*self.height,0)
        self.mask = pygame.mask.from_surface(self.image)   #将图像非透明部分保存为mask，实现完美碰撞

    #定义小型敌机移动的方法
    def move(self):
        if self.rect.top < self.height - 60:
            self.rect.top +=  self.speed
        else:
            self.reset()   #当某一个小型敌机飞出窗口后，重新生成
    #定义重新生成小型敌机的方法，重新生成敌机的位置是随机的
    def reset(self):
        self.active = True   #敌机重生时，状态标记重置为True
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-5*self.height,0)

#定义中型敌机
class MidEnemy(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy2.png").convert_alpha()
        #加载中型敌机坠毁动画图片，并保存到列表中
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy2_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy2_down4.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height = screen_size[0], screen_size[1]
        self.speed = 1
        self.active = True   #定义敌机状态标记
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-10*self.height, -self.height)
        self.mask = pygame.mask.from_surface(self.image)   #将图像非透明部分保存为mask，实现完美碰撞

    def move(self):
        if self.rect.top < self.height - 60:
            self.rect.top +=  self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True #重置敌机状态标记
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-10*self.height,0)

#定义大型敌机
class BigEnemy(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/enemy3_n1.png").convert_alpha()
        self.image2 = pygame.image.load("images/enemy3_n2.png").convert_alpha()
        #加载小型敌机坠毁动画图片，并保存到列表中
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load("images/enemy3_down1.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down2.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down3.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down4.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down5.png").convert_alpha(),\
            pygame.image.load("images/enemy3_down6.png").convert_alpha()])
        self.rect = self.image.get_rect()
        self.width, self.height  = screen_size[0], screen_size[1]
        self.speed = 1
        self.active = True  #定义敌机状态标记
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-15*self.height, -5*self.height)
        self.mask = pygame.mask.from_surface(self.image)   #将图像非透明部分保存为mask，实现完美碰撞

    def move(self):
        if self.rect.top < self.height - 60:
            self.rect.top +=  self.speed
        else:
            self.reset()

    def reset(self):
        self.active = True #重置敌机状态标记
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width),\
                                        randint(-15*self.height, -5*self.height)
