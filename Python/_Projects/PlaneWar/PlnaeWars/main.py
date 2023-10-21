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
# 设置背景
bg = pygame.image.load("images/background.png").convert_alpha()
# 加载背景音乐
bgm = pygame.mixer.Sound("music/bgm_zhuxuanlv.ogg")
bgm.set_volume(0.1)

# 游戏分数
score = 10000000000  # 建立分数变量设为0
# 加载字体
font = pygame.font.Font("font/font.ttf", 60)  # 60 意思是设置字体大小
font2 = pygame.font.Font("font/font.ttf", 120)



def main():
    global score  # 把函数外变量变成全局函数
    score = 10000000000  # 初始化分数为0
    # 播放背景音乐
    bgm.play(-1)
    # 设置时钟对象
    clock = pygame.time.Clock()
    #创建计数器
    tick = 0
    # 生成我方飞机
    hero_plane = plane.MyPlane(screen_size)
    # 敌方飞机精灵组
    enemies_group = pygame.sprite.Group()
    # 被击毁的飞机
    enemies_down = pygame.sprite.Group()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 获取按键
        keys = pygame.key.get_pressed()
        # 计数器计数
        tick += 1
        if tick >= 12000:
            tick = 0
        if tick % 100 == 0:
            # 每循环100次生成一个小飞机
            small_enemy = plane.SmallEnemy(screen_size)
            enemies_group.add(small_enemy)
        if tick % 400 == 0:
            # 每循环400此，生成一个中飞机
            mid_enemy = plane.MidEnemy(screen_size)
            enemies_group.add(mid_enemy)
        if tick % 900 == 0:
            # 每循环900此生成一个大飞机
            big_enemy = plane.BigEnemy(screen_size)
            enemies_group.add(big_enemy)
        if tick % 1300 == 0:
            # 每循环1300此生成一个核弹
            bomb = plane.Bomb(screen_size)
            enemies_group.add(bomb)
        if tick % 300 == 0:
            #  每循环300此生成一个鬼畜
            guichu = plane.Guichu(screen_size)
            enemies_group.add(guichu)
        if tick % 8 ==0:
            # 每循环10次生成一个子弹
            hero_plane.shoot()

        # 加载背景
        screen.blit(bg, (0, 0))
        # 移动敌方所有飞机
        enemies_group.update()
        # 绘制敌方有飞机
        enemies_group.draw(screen)
        # 移动子弹
        hero_plane.bullets.update()
        #绘制子弹
        hero_plane.bullets.draw(screen)
        if hero_plane.is_alive:
            # 移动我方飞机
            hero_plane.move(keys)
            # 绘制我方飞机
            screen.blit(hero_plane.image, hero_plane.rect)


        """我方飞机和敌方飞机碰撞"""
        player_collide = pygame.sprite.spritecollide(hero_plane, enemies_group, True, pygame.sprite.collide_mask)
        if player_collide: #  如果发生碰撞
            # 将飞机调整为死亡状态
            # hero_plane.is_alive = False
            hero_plane.down_music.play()  # 播放爆炸音效
            # 敌方飞机爆炸
            for enemy in player_collide:
                enemies_down.add(enemy)
                enemy.down_music.play()  # 播放敌方飞机爆炸音效

        if not hero_plane.is_alive:
            #  如果我方飞机死亡
            if hero_plane.down_index < 6:
                screen.blit(hero_plane.down_images[hero_plane.down_index],hero_plane.rect)  # 取出元素
                if tick % 6 == 0:
                    hero_plane.down_index += 1
            else:
                hero_plane.reset()  # 复位我方飞机
                enemies_group.empty()  # 清空所有敌方飞机
                hero_plane.hp -= 1  # 生命值减一
                if hero_plane.hp <= 0:
                    return
        """子弹和敌方飞机碰撞检测"""
        for bullet in hero_plane.bullets:
            enemies_collide = pygame.sprite.spritecollide(bullet, enemies_group, False, pygame.sprite.collide_mask)
            if enemies_collide:
                # 如果发生碰
                bullet.kill()  # 移除子弹
                for enemy in enemies_collide:
                    enemy.hp -= bullet.hp  # 敌方飞机减去子弹攻击值+15
                    if enemy.hp <= 0:
                        enemy.kill()  # 如果地方飞机生命值小于0，移除飞机
                        enemies_down.add(enemy)
                        enemy.down_music.play()  # 播放敌方飞机爆炸音效
                        score += enemy.score  # 加分数


        """播放敌方飞机爆炸动画"""
        for enemy in enemies_down:
            if enemy.down_index < 6:
                screen.blit(enemy.down_images[enemy.down_index],enemy.rect)
                if tick % 5 == 0:
                    enemy.down_index += 1
            else:
                enemies_down.remove(enemy)

        """显示分数和生命值"""
        score_text = font.render("分数: " + str(score), True, (255, 255, 200))  # 括号中（"分数+分数，设置开启，设置颜色：白色"）
        screen.blit(score_text,(10,10))
        life_text = font.render("生命: " + "无限", True, (250, 250, 255))  # ("生命: " + str(hero_plane.hp), True, (255,255,255))
        screen.blit(life_text,(width-300, 10))

        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)

def gameover():
    """游戏结束画面"""
    global score
    screen.blit(bg, (0,0))  # 绘制背景

    # 显示分数
    score_text = font.render("你的分数："+ str(score), True, (0, 128, 255))
    score_rect = score_text.get_rect()
    screen.blit(score_text, ((width - score_rect.width)*0.5, height*0.2))

    # 显示gameover
    gameover_text = font2.render("GAME OVER !", True, (0,128,192))  # True 意思是抗锯齿开启
    gameover_rect = gameover_text.get_rect()
    screen.blit(gameover_text,((width-gameover_rect.width)*0.5, height*0.4))

    # 提示‘空格建继续’
    again_text = font.render("按空格键继续", True, (0, 255, 0))
    again_rect = again_text.get_rect()
    screen.blit(again_text,((width-again_rect.width)*0.5, height*0.8))

    # 刷新窗口
    pygame.display.flip()

    # gameover声音特效
    gameover_music = pygame.mixer.Sound("music/gameover.ogg")
    gameover_music.set_volume(1)  # 设置声音大小
    pygame.time.wait(500)  # 时间等待（500毫秒）
    gameover_music.play()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 获取按键
        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            return



if __name__ == '__main__':
    while True:
        main()
        gameover()
