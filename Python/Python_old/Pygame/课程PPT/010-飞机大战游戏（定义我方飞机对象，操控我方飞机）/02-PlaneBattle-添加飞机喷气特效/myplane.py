'''
定义我方飞机的对象，并在对象中定义飞机图像的矩形、位置、速度等特性值，以及定义我方飞机移动的方法
'''
import pygame

class myPlane(pygame.sprite.Sprite):
    def __init__(self,screen_size):
        pygame.sprite.Sprite.__init__(self)   #动画精灵初始化

        self.image = pygame.image.load("images/me1.png").convert_alpha()   #加载我方飞机的图像
        self.image2 = pygame.image.load("images/me2.png").convert_alpha()  #加载喷气特效图像
        self.rect = self.image.get_rect()  #获取我方飞机的rect对象
        self.width,self.height = screen_size[0], screen_size[1]    #定义窗口大小的内部参数
        #设置我方飞机最初的位置
        self.rect.left, self.rect.bottom = (self.width- self.rect.width)//2, self.height - 60

        self.speed = 10
    #定义我方飞机移动的方法
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.bottom += self.speed
        else:
            self.rect.bottom = self.height - 60

    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.right += self.speed
        else:
            self.rect.right = self.width


