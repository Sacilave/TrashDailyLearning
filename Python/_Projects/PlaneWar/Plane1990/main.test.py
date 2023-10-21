import sys
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口大小
screen_size = width, height = 480,650    # 原先大小 480,650——1280,700 全屏
screen = pygame.display.set_mode(screen_size)
# 设置图标
icon = pygame.image.load("data/images/timg2.png").convert_alpha()
pygame.display.set_icon(icon)
# 设置标题
pygame.display.set_caption("获取字符指令")
# 设置背景
bg = (0, 0, 0)
#字体
font = pygame.font.Font(None,20)
font_height_line = font.get_linesize()
font_height = 0


# 建立时间对象
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        # 退出事件
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        font_surface = font.render(str(event),True,(0,255,0))
        screen.blit(font_surface,(0,font_height))
        font_height += font_height_line
        if font_height > height:
            font_height = 0
            screen.fill(bg)


    # 刷新屏幕
    pygame.display.flip()
    clock.tick(60)

