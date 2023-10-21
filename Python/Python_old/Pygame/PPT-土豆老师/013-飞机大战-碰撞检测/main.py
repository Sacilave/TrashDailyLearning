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

        """飞机与敌机碰撞检测"""
        player_collide = pygame.sprite.spritecollide(hero_plane, enemies_group, True, pygame.sprite.collide_mask)
        if player_collide:
            # 如果检测到碰撞
            hero_plane.is_alive = False  # 将我方飞机的状态调整为死亡，注释掉飞机将变为无敌
        if not hero_plane.is_alive:
            # 如果我方飞机死亡
            hero_plane.reset()  # 重置自己的飞机
            enemies_group.empty()  # 清空当前所有敌方飞机，相当于重新开始
            hero_plane.hp -= 1  # 飞机生命值减1
            if hero_plane.hp <= 0:
                # 如果我方飞机生命值小于0，游戏结束
                bgm.stop()  # 停止播放背景音乐
                return  # 此处将退出main函数

        """子弹与敌机碰撞检测"""
        for bullet in hero_plane.bullets:
            enemies_collides = pygame.sprite.spritecollide(bullet, enemies_group, False, pygame.sprite.collide_mask)
            if enemies_collides:
                bullet.kill()  # 将碰撞的子弹清除
                for enemy in enemies_collides:
                    enemy.hp -= bullet.hp  # 飞机的生命值减去子弹的伤害值
                    if enemy.hp <= 0:
                        # 如果敌方飞机的生命值小于等于0
                        enemy.kill()  # 将敌方飞机从精灵组清除

        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    # 开始运行程序
    main()