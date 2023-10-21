import pygame


class Bullet01(pygame.sprite.Sprite):
    """上边的子弹"""
    def __init__(self,position):
        """初始化子弹"""
        super().__init__()  #初始化动画精灵
        self.image = pygame.image.load("images/bullet13.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获取位置
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = 2  #子弹的伤害值
        self.speed = 10  # 子弹的速度

        self.rect.center = [position[0],position[1]]  # 子弹的生成位置为飞机的顶端

    def update(self):
        """移动子弹，如果超过上边框，移除子弹"""
        self.rect.top -= self.speed  # 向上移动子弹
        if self.rect.bottom < 0:
            self.kill()


class Bullet02(pygame.sprite.Sprite):
    """左上边的子弹"""
    def __init__(self,position):
        """初始化子弹"""
        super().__init__()  #初始化动画精灵
        self.image = pygame.image.load("images/bullet8.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获取位置
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = 1  #子弹的伤害值
        self.speed = 10  # 子弹的速度

        self.rect.center = [position[0]-50,position[1]+50]  # 子弹的生成位置为飞机的顶端

    def update(self):
        """移动子弹，如果超过上边框，移除子弹"""
        self.rect.top -= self.speed * 0.5  # 向上移动子弹
        self.rect.left -= self.speed * 0.2  # 向左移动子弹
        if self.rect.bottom < 0:
            self.kill()



class Bullet03(pygame.sprite.Sprite):
    """右上边的子弹"""
    def __init__(self,position):
        """初始化子弹"""
        super().__init__()  #初始化动画精灵
        self.image = pygame.image.load("images/bullet8.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获取位置
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = 1  #子弹的伤害值
        self.speed = 10  # 子弹的速度

        self.rect.center = [position[0]+50,position[1]+50]  # 子弹的生成位置为飞机的顶端

    def update(self):
        """移动子弹，如果超过上边框，移除子弹"""
        self.rect.top -= self.speed * 0.5  # 向上移动子弹
        self.rect.right += self.speed * 0.2  # 向又移动子弹
        if self.rect.bottom < 0:
            self.kill()

class Bullet04(pygame.sprite.Sprite):
    """左边的子弹"""
    def __init__(self,position):
        """初始化子弹"""
        super().__init__()  #初始化动画精灵
        self.image = pygame.image.load("images/bullet19.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获取位置
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = 1  #子弹的伤害值
        self.speed = 10  # 子弹的速度

        self.rect.center = [position[0]-100,position[1]+50]  # 子弹的生成位置为飞机的顶端

    def update(self):
        """移动子弹，如果超过上边框，移除子弹"""
        self.rect.right -= self.speed * 2  # 向右移动子弹
        if self.rect.bottom < 0:
            self.kill()

class Bullet05(pygame.sprite.Sprite):
    """又边的子弹"""
    def __init__(self,position):
        """初始化子弹"""
        super().__init__()  #初始化动画精灵
        self.image = pygame.image.load("images/bullet20.png").convert_alpha()
        self.rect = self.image.get_rect()  # 获取位置
        self.mask = pygame.mask.from_surface(self.image)

        self.hp = 1  #子弹的伤害值
        self.speed = 10  # 子弹的速度

        self.rect.center = [position[0]+100,position[1]]  # 子弹的生成位置为飞机的顶端

    def update(self):
        """移动子弹，如果超过上边框，移除子弹"""
        self.rect.right += self.speed * 2  # 向右移动子弹
        if self.rect.bottom < 0:
            self.kill()

