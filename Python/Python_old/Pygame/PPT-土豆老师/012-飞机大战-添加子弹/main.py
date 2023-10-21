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
    tick = 0  # 初始化计数器

    # 生成一个我方飞机
    hero_plane = plane.MyPlane(screen_size)
    # 敌方飞机的精灵组
    enemies_group = pygame.sprite.Group()
    # 存储被击毁的飞机，用来渲染击毁动画
    enemies_down = pygame.sprite.Group()

    while True:
        """游戏主界面循环"""
        for event in pygame.event.get():
            # 退出事件
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 获取按键
        keys = pygame.key.get_pressed()

        # 计数器计数，大于等于12000重置
        tick += 1
        if tick >= 12000:
            ticks = 0
        # 生成敌方飞机
        if tick % 60 == 0:
            # 每循环60次生成一个敌方小飞机
            small_enemy = plane.SmallEnemy(screen_size)
            enemies_group.add(small_enemy)
        if tick % 400 == 0:
            # 每循环400次生成一个敌方中飞机
            mid_enemy = plane.MidEnemy(screen_size)
            enemies_group.add(mid_enemy)
        if tick % 1400 == 0:
            # 每循环1400次生成一个敌方大飞机
            boss = plane.Boss(screen_size)
            enemies_group.add(boss)
        if tick % 2400 == 0:
            # 每循环2400次生成一个炸弹
            bomb = plane.Bomb(screen_size)
            enemies_group.add(bomb)
        if tick % 15 == 0:
            # 每循环15次发射一次子弹
            hero_plane.shoot()

        # 绘制背景
        screen.blit(bg, (0, 0))

        # 移动敌方飞机
        enemies_group.update()
        # 绘制敌方飞机
        enemies_group.draw(screen)
        # 移动子弹
        hero_plane.bullets.update()
        # 绘制子弹
        hero_plane.bullets.draw(screen)
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