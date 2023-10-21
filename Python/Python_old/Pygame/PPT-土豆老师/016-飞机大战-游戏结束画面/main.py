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

# 游戏分数
score = 0


def main():
    """游戏主界面"""
    global score  # 将分数设为全局变量
    score = 0  # 初始化分数

    bgm = pygame.mixer.Sound("music/bgm_zhuxuanlv.ogg")  # 加载背景音乐
    bgm.set_volume(0.5)  # 设置音量
    bgm.play(-1)  # 播放背景音乐，循环播放

    clock = pygame.time.Clock()  # 设置时钟对象
    tick = 0  # 初始化计数器

    # 生成一个我方飞机
    hero_plane = plane.MyPlane(screen_size)
    # 敌方飞机的精灵组
    enemies_group = pygame.sprite.Group()
    # 击毁组，存储被击毁的飞机，用来渲染击毁动画
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

        """飞机与敌机碰撞检测"""
        player_collide = pygame.sprite.spritecollide(hero_plane, enemies_group, True, pygame.sprite.collide_mask)
        if player_collide:
            # 如果检测到碰撞
            hero_plane.is_alive = False  # 将我方飞机的状态调整为死亡，注释掉飞机将变为无敌
            hero_plane.down_music.play()  # 播放我方飞机爆炸音效
            for each in player_collide:
                enemies_down.add(each)  # 将碰撞的敌方飞机添加到击毁组，准备播放爆炸动画
                each.down_music.play()  # 播放敌方飞机爆炸的音效
        if not hero_plane.is_alive:
            # 如果我方飞机死亡
            if hero_plane.down_index < len(hero_plane.down_img):
                # 播放死亡爆炸动画，每循环6次切换一次特效图片
                screen.blit(hero_plane.down_img[hero_plane.down_index], hero_plane.rect)
                if tick % 6 == 0:
                    hero_plane.down_index += 1 
            else:
                hero_plane.reset()  # 重置自己的飞机
                enemies_group.empty()  # 清空当前所有敌方飞机，相当于重新开始
                hero_plane.hp -= 1  # 飞机生命值减1
                if hero_plane.hp <= 0:
                    # 如果我方飞机生命值小于0，游戏结束
                    bgm.stop()  # 停止播放背景音乐
                    return  # 此处将退出main函数

        """子弹与敌机碰撞检测"""
        for bullet in hero_plane.bullets:
            enemies_collide = pygame.sprite.spritecollide(bullet, enemies_group, False, pygame.sprite.collide_mask)
            if enemies_collide:
                bullet.kill()  # 将碰撞的子弹清除
                for enemy in enemies_collide:
                    enemy.hp -= bullet.hp  # 飞机的生命值减去子弹的伤害值
                    if enemy.hp <= 0:
                        # 如果敌方飞机的生命值小于等于0
                        enemy.kill()  # 将敌方飞机从精灵组清除
                        enemies_down.add(enemy)  # 将碰撞的敌方飞机添加到击毁组，准备播放爆炸动画
                        enemy.down_music.play()  # 播放爆炸音效
                        score += enemy.score  # 获得敌方飞机对应的分数
                        

        """飞机爆炸动画和音效"""
        if enemies_down:
            for enemy in enemies_down:
                if enemy.down_index < len(enemy.down_img):
                    # 播放死亡爆炸动画，每循环6次切换一次特效图片
                    screen.blit(enemy.down_img[enemy.down_index], enemy.rect)
                    if tick % 6 == 0:
                        enemy.down_index += 1
                else:
                    enemies_down.remove(enemy)  # 爆炸特效结束后，移出击毁组

        # 显示分数
        show_score(str(score))
        # 显示生命值
        show_life(hero_plane.hp)
        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)


def show_score(text):
    """显示分数"""
    # 获取系统字体，并设置文字大小
    font = pygame.font.SysFont("font/font.ttf", 60)
    # 设置文字内容
    score_text = font.render("SCORE:"+text, True, (255, 255, 255))
    # 绘制文字
    screen.blit(score_text, (10, 10))


def show_life(hp):
    """显示飞机生命值"""
    # 获取系统字体，并设置文字大小
    font = pygame.font.SysFont("font/font.ttf", 60)
    # 设置文字内容
    score_text = font.render("LIFE:"+str(hp), True, (255, 255, 255))
    # 绘制文字
    screen.blit(score_text, (width-150, 10))


def gameover():
    """结束画面"""
    global score  # 将分数设为全局变量
    
    # 游戏结束音效
    gameover_music = pygame.mixer.Sound("music/gameover.ogg")
    gameover_music.set_volume(1)
    # 绘制背景
    screen.blit(bg, (0, 0))

    # 显示最终得分，字体大小60
    font1 = pygame.font.SysFont("font/font.ttf", 60)
    score_text = font1.render("YOUR SCORRE:"+str(score), True, (0, 200, 0))
    score_rect = score_text.get_rect()
    screen.blit(score_text, ((width-score_rect.width)*0.5, height*0.2))
    # 显示 game over，字体大小120
    font2 = pygame.font.SysFont("font/font.ttf", 120)
    gameover_text = font2.render("GAME OVER!", 1, (0, 200, 0))
    gameover_rect = gameover_text.get_rect()
    screen.blit(gameover_text, ((width-gameover_rect.width)*0.5, (height-gameover_rect.height)*0.5))
    # 显示按空格继续游戏，字体大小40
    font3 = pygame.font.SysFont("font/font.ttf", 40)
    again_text = font3.render("Press SPACE to continue", 1, (0, 200, 0))
    again_rect = again_text.get_rect()
    screen.blit(again_text, ((width-again_rect.width)*0.5, height*0.8))

    # 更新屏幕显示
    pygame.display.update()
    # 等待0.5秒后播放gameover音效
    pygame.time.wait(500)
    gameover_music.play()

    while True:
        # 设置时钟对象
        clock = pygame.time.Clock()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            # 如果按下空格键，就退出该函数
            return


if __name__ == '__main__':
    # 开始运行程序,程序在主界面和结束界面循环
    while True:
        main()
        gameover()
