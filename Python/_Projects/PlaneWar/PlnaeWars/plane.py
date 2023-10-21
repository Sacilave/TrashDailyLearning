import pygame
from pygame.locals import *
import random
import bullet


class MyPlane(pygame.sprite.Sprite):
    """我方飞机的类"""
    def __init__(self, screen_size):
        super().__init__()  # 初始化动画精灵
        self.image = pygame.image.load("images/plane_j20.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 5
        self.hp = 1  # 设置我方飞机血量
        self.is_alive = True  # 飞机生存状态

        self.reset()  # 调用复位飞机的方法

        self.bullets = pygame.sprite.Group()  # 子弹的精灵组

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  #调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_siwang.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量


    def move(self, keys):
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
        self.is_alive = True
        self.down_index = 0

    def shoot(self):
        """发射子弹"""
        bullet1 = bullet.Bullet01(self.rect.midtop)  # 中间的子弹
        self.bullets.add(bullet1)
        bullet2 = bullet.Bullet02(self.rect.midtop)  # 左边的子弹
        self.bullets.add(bullet2)
        bullet3 = bullet.Bullet03(self.rect.midtop)  # 左边的子弹
        self.bullets.add(bullet3)
        bullet4 = bullet.Bullet04(self.rect.midtop)  # 左边的子弹
        self.bullets.add(bullet4)
        bullet5 = bullet.Bullet05(self.rect.midtop)  # 左边的子弹
        self.bullets.add(bullet5)

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_100.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*100, 0, 100, 100)))

class SmallEnemy(pygame.sprite.Sprite):
    """敌方小飞机"""
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load("images/enemy"+str(random.randint(1,10))+".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 2  # 飞机速度
        self.hp = 20  # 设置飞机血量  hit piont = hp 打击点数
        self.score = 5000  # 击杀飞机得分


        self.reset() # 初始化敌方小飞机

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  #调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_xiaobaozha.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量



    def update(self):
        """更新敌方小飞机的位置"""
        self.rect.top += self.speed
        if self.rect.top > self.height:
            # 如果小飞机超出边界，杀掉小飞机
            self.kill()

    def reset(self):
        """复位敌方小飞机"""
        self.rect.left = random.randint(0,self.width-self.rect.width)
        self.rect.bottom = -self.height

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_100.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*100, 0, 100, 100)))



class MidEnemy(pygame.sprite.Sprite):
    """敌方中飞机"""
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load("images/mid_enemy"+str(random.randint(1,3))+".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 1.5  # 飞机速度
        self.hp = 30  # 设置飞机血量  hit piont = hp 打击点数
        self.score = 7000  # 击杀飞机得分


        self.reset()  # 初始化敌方中飞机

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  #调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_zhongbaozha.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量



    def update(self):
        """更新敌方中飞机的位置"""
        self.rect.top += self.speed
        if self.rect.top > self.height:
            # 如果中飞机超出边界，杀掉中飞机
            self.kill()

    def reset(self):
        """复位敌方中飞机"""
        self.rect.left = random.randint(0,self.width-self.rect.width)
        self.rect.bottom = -self.height

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_200.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*200, 0, 200, 200)))


class BigEnemy(pygame.sprite.Sprite):
    """敌方大飞机"""
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load("images/boss"+str(random.randint(1,3))+".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 1  # 速度
        self.hp = 40  # 设置血量  hit piont = hp 打击点数
        self.score = 9000  # 击杀得分


        self.reset()  # 初始化

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  #调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_siwang.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量



    def update(self):
        """更新的位置"""
        self.rect.top += self.speed
        if self.rect.top > self.height:
            # 如果超出边界，杀掉
            self.kill()

    def reset(self):
        """复位"""
        self.rect.left = random.randint(0,self.width-self.rect.width)
        self.rect.bottom = -self.height

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_300.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*300, 0, 300, 300)))


class Bomb(pygame.sprite.Sprite):
    """核弹"""
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load("images/bomb.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 1  # 速度
        self.hp = 50  # 设置血量  hit piont = hp 打击点数
        self.score = 11000  # 击杀得分


        self.reset()  # 初始化

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  #调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_dabaozha.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量


    def update(self):
        """更新敌方的位置"""
        self.rect.top += self.speed
        if self.rect.top > self.height:
            # 如果超出边界，杀掉
            self.kill()

    def reset(self):
        """复位"""
        self.rect.left = random.randint(0,self.width-self.rect.width)
        self.rect.bottom = -self.height

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_200.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*200, 0, 200, 200)))


class Guichu(pygame.sprite.Sprite):
    """鬼畜"""
    def __init__(self,screen_size):
        super().__init__()
        self.image = pygame.image.load("images/guichu"+str(random.randint(1, 20))+".png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.width = screen_size[0]
        self.height = screen_size[1]
        self.speed = 1  # 速度
        self.hp = 70  # 设置血量  hit piont = hp 打击点数
        self.score = 15000  # 击杀得分


        self.reset()  # 初始化

        # 飞机爆炸图片
        self.down_images = []  # 存储飞机的爆炸的图片(列表)
        self.down_index = 0  # 爆炸图片的序号
        self.add_down_image()  # 调用加载飞机爆炸图片
        # 飞机爆炸音效
        self.down_music = pygame.mixer.Sound("music/effect_dabaozha.ogg")
        self.down_music.set_volume(0.8)  # 设置爆炸音效音量


    def update(self):
        """更新敌方鬼畜的位置"""
        self.rect.top += self.speed
        if self.rect.top > self.height:
            # 如果超出边界，杀掉
            self.kill()

    def reset(self):
        """复位"""
        self.rect.left = random.randint(0,self.width-self.rect.width)
        self.rect.bottom = -self.height

    def add_down_image(self):
        """添加爆炸图片的方法"""
        down_image = pygame.image.load("images/bomb_300.png").convert_alpha()
        for i in range(6):
            self.down_images.append(down_image.subsurface(pygame.Rect(i*300, 0, 300, 300)))

