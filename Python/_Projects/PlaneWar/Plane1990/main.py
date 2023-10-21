import sys
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()
#定义全屏开关
fullscreen = False
# 设置窗口大小
#FULLSCREEN 全屏模式   DOUBLEBUF 双缓冲模式
screen_size = width, height = 480, 650
screen = pygame.display.set_mode(screen_size)
#获取电脑支持的分辨率
mode_list = pygame.display.list_modes()
screen_full = mode_list[0]
# 设置标题
pygame.display.set_caption("飞机大战")
# 设置背景
bg_window = pygame.image.load("data/images/background.png").convert()
bg_full = pygame.transform.scale(bg_window, screen_full)
bg = bg_window

# 加载飞机图片
heroPlane = pygame.image.load("data/images/me1.png").convert_alpha()
# 获取飞机位置和大小
position = heroPlane.get_rect()
# 速度
speed = [0, 0]

# 建立时间对象
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # 退出事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-7,0]
            if event.key == K_RIGHT:
                speed = [7,0]
            if event.key == K_UP:
                speed = [0,-7]
            if event.key == K_DOWN:
                speed = [0,7]
            # 按ESC全屏
            if event.key == K_ESCAPE:
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode(screen_full,FULLSCREEN | HWSURFACE)
                    width, height = screen_full
                    bg = bg_full
                else:
                    screen = pygame.display.set_mode(screen_size)
                    width,height = screen_size
                    bg = bg_window
        else:
            speed = [0,0]
    #限制飞机飞行边界
    if position.top < 0:
        position.top = 0
    if position.bottom > height:
        position.bottom = height
    if position.left < 0:
        position.left = 0
    if position.right > width:
        position.right = width
    position = position.move(speed)
    # 设置背景 (fill纯色背景)
    screen.blit(bg,(0,0))
    # 放置飞机
    screen.blit(heroPlane, position)

    # 刷新屏幕
    pygame.display.flip()
    clock.tick(65)

