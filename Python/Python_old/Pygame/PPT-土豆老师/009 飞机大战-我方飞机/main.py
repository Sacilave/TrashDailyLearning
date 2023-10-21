# 1.导入系统环境模块sys， 导入pygame， 导入pygame.locals

import sys
import pygame
from pygame.locals import *
import plane

# 初始化pygame
pygame.init()
# 设置窗口大小
screen_size = width, height = 1024, 600
screen = pygame.display.set_mode(screen_size)
# 设置标题
pygame.display.set_caption("飞机大战")
# 设置图标
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)
# 加载背景图片
bg = pygame.image.load("images/background.png").convert_alpha()


def main():
    """游戏主界面"""

    bgm = pygame.mixer.Sound("music/bgm_zhuxuanlv.ogg")  # 加载背景音乐
    bgm.set_volume(0.5)  # 设置音量
    bgm.play(-1)  # 播放背景音乐，循环播放

    clock = pygame.time.Clock()  # 设置时钟对象

    # 生成一个我方飞机
    hero_plane = plane.MyPlane(screen_size)

    while True:
        """游戏主界面循环"""
        for event in pygame.event.get():
            # 退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 获取按键
        keys = pygame.key.get_pressed()
        # 绘制背景
        screen.blit(bg, (0, 0))

        if hero_plane.is_alive:
            # 根据按键状态移动我方飞机
            hero_plane.move(keys)
            # 绘制我方飞机
            screen.blit(hero_plane.image, hero_plane.rect)

        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    # 开始运行程序
    main()