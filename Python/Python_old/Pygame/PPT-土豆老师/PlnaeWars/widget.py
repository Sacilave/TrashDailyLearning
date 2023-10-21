import pygame


class Score(pygame.sprite.Sprite):
    """分数"""
    def __init__(self, score):
        super().__init__()
        self.size = 60
        self.color = (255, 255, 255)
        font = pygame.font.SysFont("font/font.ttf", self.size)
        self.image = font.render("SCORE:"+score, True, self.color)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.top = 10
        self.rect.left =10


class Score(pygame.sprite.Sprite):
    """生命值"""
    def __init__(self, life, position):
        super().__init__()
        self.size = 60
        self.color = (255, 255, 255)
        font = pygame.font.SysFont("font/font.ttf", self.size)
        self.image = font.render("SCORE:"+life, True, self.color)
        self.rect = self.image.get_rect()
    
    def update(self):
        self.rect.top = 10
        self.rect.left =10