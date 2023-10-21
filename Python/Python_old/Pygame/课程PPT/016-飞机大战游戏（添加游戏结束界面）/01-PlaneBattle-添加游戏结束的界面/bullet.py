'''
定义我方飞机发射子弹的对象
'''
import pygame

class Bullet1(pygame.sprite.Sprite):
    def __init__(self,position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("images/bullet1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position    #position应该为我方飞机中央机头位置
        self.speed = 12
        self.active = True
        self.mask = pygame.sprite.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.active = False

    def reset(self,position):
        self.rect.left, self.rect.top = position    #从新生成子弹时，需要根据我方飞机最新的位置来生成
        self.active = True
