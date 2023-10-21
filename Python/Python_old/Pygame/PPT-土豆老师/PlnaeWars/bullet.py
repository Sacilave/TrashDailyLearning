import pygame


class Bullet01(pygame.sprite.Sprite):
    """中间的子弹"""
    def __init__(self, position):
        """position为飞机的rect.midtop"""
        super().__init__()
        self.image = pygame.image.load("images/bullet10.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.sprite.from_surface(self.image)
        self.hp = 3  # 子弹的伤害值
        self.speed = 10  # 子弹的飞行速度

        # 调整子弹出发点的位置，在飞机中前部
        self.rect.center = [position[0], position[1]]

    def update(self):
        """更新子弹位置，向前发射，超过边界移除"""
        self.rect.top -= self.speed
        if self.rect.bottom < 0:
            self.kill()


class Bullet02(pygame.sprite.Sprite):
    """左边的子弹"""
    def __init__(self, position):
        """position为rect.midtop"""
        super().__init__()
        self.image = pygame.image.load("images/bullet8.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.sprite.from_surface(self.image)
        self.hp = 1  # 子弹的伤害值
        self.speed = 10  # 子弹的飞行速度

        # 调整子弹出发点的位置,在飞机左边
        self.rect.center = [position[0]-50, position[1]+50]

    def update(self):
        """更新子弹位置，向左前发射，超过边界移除"""
        self.rect.top -= self.speed*0.5
        self.rect.left -= self.speed*0.2
        if self.rect.bottom < 0:
            self.kill()


class Bullet03(pygame.sprite.Sprite):
    """右边的子弹"""
    def __init__(self, position):
        """position为rect.midtop"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet8.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.sprite.from_surface(self.image)
        self.hp = 1  # 子弹的伤害值
        self.speed = 10  # 子弹的飞行速度

        # 调整子弹出发点的位置,在飞机右边
        self.rect.center = [position[0]+50, position[1]+50]

    def update(self):
        """更新子弹位置，向右前发射，超过边界移除"""
        self.rect.top -= self.speed*0.5
        self.rect.right += self.speed*0.2
        if self.rect.bottom < 0:
            self.kill()
