import pygame
from pygame.locals import *
import random


class MyPlane(pygame.sprite.Sprite):
    """我方飞机的类"""
    def __init__(self, screen_size):
        super().__init__()  # 初始化动画精灵
        self.image = pygame.image.load("images/plane_j20.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.sprite.from_surface(self.image)
        # 游戏窗口的宽和高
        self.width = screen_size[0]
        self.height = screen_size[1]

        self.is_alive = True  # 我方飞机状态，True表示生存
        self.speed = 5  # 我方飞机速度
        self.hp = 3  # 我方飞机生命值

        # 调用复位飞机的方法
        self.reset()

    def move(self, keys):
        """移动我方飞机"""
        if keys[K_w] and self.rect.top > 0:
            self.rect.top -= self.speed
        if keys[K_s] and self.rect.bottom < self.height:
            self.rect.bottom += self.speed
        if keys[K_a] and self.rect.left > 0:
            self.rect.left -= self.speed
        if keys[K_d] and self.rect.right < self.width:
            self.rect.right += self.speed

    def reset(self):
        """复位我方飞机"""
        self.rect.midbottom = [self.width/2, self.height-10]
        self.is_alive = True  # 将飞机设置为生存状态


class SmallEnemy(pygame.sprite.Sprite):
    """敌方小飞机的类"""
    def __init__(self, screen_size):
        super().__init__()
        image_file = "images/enemy" + str(random.randint(1, 10)) + ".png"
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.sprite.from_surface(self.image)
        # 游戏窗口的宽和高
        self.width = screen_size[0]
        self.height = screen_size[1]

        self.hp = 10  # 飞机生命值
        self.speed = 3  # 飞机速度
        self.score = 100  # 击杀分数

        self.reset()  # 调用复位飞机的方法

    def update(self):
        """"更新飞机位置"""
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.kill()

    def reset(self):
        """复位敌方小飞机"""
        self.rect.bottom = -self.height
        self.rect.left = random.randint(0, self.width-self.rect.width)
