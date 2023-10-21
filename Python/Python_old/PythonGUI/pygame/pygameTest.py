import sys
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()
# 设置窗口大小
screen_size = width, height = 1024, 600
screen = pygame.display.set_mode(screen_size)
# 设置标题
pygame.display.set_caption("飞机大战")
# 设置图标
icon = pygame.image.load("CrazyMonkey.jpg").convert_alpha()
pygame.display.set_icon(icon)
# 加载背景图片 pygame.image.load("1.jpg").convert_alpha()
bg = (225, 225, 225)


def main():
    """游戏主界面"""
    # 获取系统字体，并设置文字大小
    font = pygame.font.SysFont("font/font.ttf", 60)
    # 设置文字内容
    score_text = font.render("SCORE:", True, (100, 100, 100))
    # 绘制文字
    screen.blit(score_text, (100, 50))



    clock = pygame.time.Clock()  # 设置时钟对象
    tick = 0  # 初始化计数器


    while True:
        """游戏主界面循环"""
        for event in pygame.event.get():
            # 退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 绘制背景:screen.blit(bg, (0, 0))
        screen.fill(bg)


        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    # 开始运行程序
    main()
