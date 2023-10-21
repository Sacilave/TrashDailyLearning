import pygame
from pygame.locals import *
import random


class MyPlane(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        self.image = pygame.image.load("images/plane_adventure_01.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.mask = pygame.sprite.from_surface(self.image)
        # 生命值
        self.life = 3
        self.speed = 5
        # 初始化飞机位置
        self.reset()
        self.bullets = pygame.sprite.Group()

    def move(self, key):
        if key[K_w] and self.rect.top > 0:
            self.rect.top -= self.speed
        if key[K_s] and self.rect.bottom < self.height:
            self.rect.bottom += self.speed
        if key[K_a] and self.rect.left > 0:
            self.rect.left -= self.speed
        if key[K_d] and self.rect.right < self.width:
            self.rect.right += self.speed

    def reset(self):
        self.rect.midbottom = [self.width/2, self.height-60]

    def shoot(self, bullet_image):
        bullet = Bullet(bullet_image, self.rect.midtop)
        self.bullets.add(bullet)


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        super().__init__()
        image_file = "images/enemy" + str(random.randint(1, 10)) + ".png"
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.mask = pygame.sprite.from_surface(self.image)
        self.hit = 5
        self.speed = 1
        self.reset()
        # 添加飞机坠毁图片
        self.down_index = 0

    def update(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.kill()

    def reset(self):
        self.rect.bottom = 0
        self.rect.left = random.randint(0, self.width-self.rect.width)



class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image, position):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(bullet_image).convert_alpha()
        self.rect = self.image.get_rect()

        self.speed = 15
        self.active = True
        self.mask = pygame.sprite.from_surface(self.image)
        # position应该为我方飞机中央机头位置
        self.rect.center = [position[0], position[1]]
        self.boom_img = pygame.image.load("images/bomb1s.png").convert_alpha()

    def update(self):
        self.rect.top -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class EnemyBomb(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = pygame.image.load("images/bomb_img.png").convert_alpha()
        self.columns = 6
        self.image = None
        self.rect = position
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 150
        self.frame_height = 150
        self.all_frame = 5
        self.last_time = 0

    def update(self, current_time, rate=600):
        if self.frame != self.old_frame:
            x = self.frame * self.frame_width
            y = 0
            rect = (x, y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.all_frame:
                self.frame = 0
            self.last_time = current_time


