'''
游戏框架：
1.导入python程序运行所需的环境模块sys，pygame模块，以及pygame.locals模块提供常用的常量和函数。
2.定义窗口大小，并创建窗口，设置游戏标题，以及加载背景。
3.定义主函数main()，设置程序退出机制，绘制背景图像，flip()方法刷新所有待显示的图像（更新整个窗口），设置程序运行的帧率。
'''
import sys
import pygame
from pygame.locals import *
import myplane  #导入我方飞机模块
import enemy #导入敌方飞机模块
import bullet #导入子弹模块

pygame.init()

screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("飞机大战")
background = pygame.image.load("images/background.png").convert()

#加载背景音乐
pygame.mixer.music.load("sound/game_music.ogg")  #加载背景音乐文件
pygame.mixer.music.set_volume(0.1)  #设置音量
#加载大型飞机飞行声音
enemy3_fly_sound = pygame.mixer.Sound("sound/enemy3_flying.wav")
enemy3_fly_sound.set_volume(0.2)
#加载敌机坠毁的声音
small_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
small_down_sound.set_volume(0.3)
mid_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
mid_down_sound.set_volume(0.3)
big_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
big_down_sound.set_volume(0.6)

#定义将敌方小飞机添加到组的函数
def add_small_enemies(group1, group2, num):
    for small_enemy_num in range(num):
        each_small_enemy = enemy.SmallEnemy(screen_size)
        group1.add(each_small_enemy)
        group2.add(each_small_enemy)

#定义将敌方中型飞机添加到组的函数
def add_mid_enemies(group1, group2, num):
    for mid_enemy_num in range(num):
        each_mid_enemy = enemy.MidEnemy(screen_size)
        group1.add(each_mid_enemy)
        group2.add(each_mid_enemy)

#定义将敌方大型飞机添加到组的函数
def add_big_enemies(group1, group2, num):
    for big_enemy_num in range(num):
        each_big_enemy = enemy.BigEnemy(screen_size)
        group1.add(each_big_enemy)
        group2.add(each_big_enemy)

#定义main()函数用来管理主程序
def main():
    pygame.mixer.music.play(-1)    #一直循环播放背景音乐
    clock = pygame.time.Clock()

    #生成我方飞机
    heroPlane = myplane.myPlane(screen_size)
    #创建敌方飞机组（动画精灵组）
    enemies = pygame.sprite.Group()
    #生成小敌方飞机
    small_enemies = pygame.sprite.Group()  #创建敌方小飞机组（动画精灵组）
    add_small_enemies(small_enemies, enemies, 15)   #将生成的多个小飞机添加到敌方小飞机组以及敌方飞机组
    #生成中型敌方飞机
    mid_enemies = pygame.sprite.Group()  #创建敌方小飞机组（动画精灵组）
    add_mid_enemies(mid_enemies, enemies, 4)   #将生成的多个中型飞机添加到敌方中型飞机组以及敌方飞机组
    #生成大型敌方飞机
    big_enemies = pygame.sprite.Group()  #创建敌方大型飞机组（动画精灵组）
    add_big_enemies(big_enemies, enemies, 2)   #将生成的多个大型飞机添加到敌方大型飞机组以及敌方飞机组
    #用于切换飞机特效图像
    switch_image = True
    #碰撞后，敌机坠毁动画图片索引标志定义
    small_destroy_index = 0
    mid_destroy_index = 0
    big_destroy_index = 0

    #生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4    #子弹数量为4时，按照循环10次发射一发，差不多占满窗口的高度
    #生成4发子弹并放入bullet1列表
    for i in range(BULLET1_NUM):
        bullet1.append(bullet.Bullet1(heroPlane.rect.midtop))

    #用于切换特效的延迟
    delay = 100
    #统计得分
    score = 0
    score_font = pygame.font.Font("font/font.ttf", 36)   #创建一个Font对象
    WhiteFont = (255, 255, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #检测用户的键盘操作,并让我方飞机向上、向下、向左、向右移动
        key_pressed = pygame.key.get_pressed()
        if key_pressed[ K_w ] or key_pressed[ K_UP ]:
            heroPlane.moveUp()
        if key_pressed[ K_s ] or key_pressed[ K_DOWN ]:
            heroPlane.moveDown()
        if key_pressed[ K_a ] or key_pressed[ K_LEFT ]:
            heroPlane.moveLeft()
        if key_pressed[ K_d ] or key_pressed[ K_RIGHT ]:
            heroPlane.moveRight()

        screen.blit(background,(0,0))

        #绘制小型敌机,添加敌机坠毁动画
        for each in small_enemies:
            if each.active == True:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                #动画图片的切换稍作延时，主循环三次切换一幅图
                if not(delay % 3):
                    #播放坠毁声音
                    if small_destroy_index == 0:
                        small_down_sound.play()
                    #切换坠毁动画图像
                    screen.blit(each.destroy_images[small_destroy_index], each.rect)  #绘制动画图像
                    small_destroy_index = (small_destroy_index + 1) % 4   #动画图像切换索引递变
                    #重新生成敌机
                    if small_destroy_index == 0:
                        score += 100    #击中一架小型敌机得分加100
                        each.reset()
        #绘制中型敌机
        for each in mid_enemies:
            if each.active == True:
                each.move()
                screen.blit(each.image, each.rect)
            else:
                #动画图片的切换稍作延时，主循环三次切换一幅图
                if not(delay % 3):
                    if mid_destroy_index == 0:
                        mid_down_sound.play()
                    screen.blit(each.destroy_images[mid_destroy_index], each.rect)  #绘制动画图像
                    mid_destroy_index = (mid_destroy_index + 1) % 4   #动画图像切换索引递变
                    if mid_destroy_index == 0:
                        score += 300    #击中一架中型敌机得分加300
                        each.reset()
        #绘制大型飞机
        for each in big_enemies:
            if each.active == True:
                each.move()
                if switch_image:
                    screen.blit(each.image, each.rect)
                else:
                    screen.blit(each.image2, each.rect)
                #在大型敌机出现在窗口之前，开始有飞行声音
                if each.rect.bottom == -50:
                    enemy3_fly_sound.play()
            else:
                #动画图片的切换稍作延时，主循环三次切换一幅图
                if not(delay % 3):
                    if big_destroy_index == 0:
                        big_down_sound.play()
                    screen.blit(each.destroy_images[big_destroy_index], each.rect)  #绘制动画图像
                    big_destroy_index = (big_destroy_index + 1) % 6   #大型敌机的动画是6张图
                    if big_destroy_index == 0:
                        enemy3_fly_sound.stop()   #当坠毁时，飞行的声音停止
                        score += 500    #击中一架大型敌机得分加500
                        each.reset()
        #绘制我方飞机，切换特效图像
        if switch_image:
            screen.blit(heroPlane.image,heroPlane.rect)
        else:
            screen.blit(heroPlane.image2,heroPlane.rect)
        #每循环5次切换一次特效图像
        if not(delay % 5):
            switch_image = not switch_image
        delay -= 1
        if delay == 0:
            delsy = 100

        #发射子弹,没循环10次，发射一枚子弹
        if not(delay % 10):
            bullet1[bullet1_index].reset(heroPlane.rect.midtop)
            bullet1_index = (bullet1_index + 1) % BULLET1_NUM

        #检测子弹击中敌机
        for each in bullet1:
            #如果子弹状态标记为True，则子弹移动
            if each.active == True:
                each.move()   #子弹移动
                screen.blit(each.image,each.rect)   #绘制子弹
                enemies_hit = pygame.sprite.spritecollide(each,enemies,False,pygame.sprite.collide_mask) #检测子弹与敌机碰撞
                #如果有敌机被击中，则子弹状态标记改为False，被击中的敌机的状态标记也改为False
                if enemies_hit:
                    each.active = False
                    for e in enemies_hit:
                        #如果被击中的敌机是中型或大型敌机，则每击中一次血量减1，当血量变为0时，敌机状态标记改为False
                        if e in mid_enemies or e in big_enemies:
                            e.energy -= 1
                            if e.energy == 0:
                                e.active = False
                        #如果是小型敌机，一发子弹搞定
                        else:
                            e.active = False
            #如果子弹状态标记为False，则重新生成子弹（原来子弹消失）
            else:
                each.reset(heroPlane.rect.midtop)
        '''
        #将下面的代码删除，现在不需要检测我方飞机与敌机的碰撞
        #添加碰撞检测，检测我方飞机与敌机发生碰撞
        #将发生碰撞的敌机（动画精灵）保存到enemies_collided列表
        enemies_collided = pygame.sprite.spritecollide(heroPlane,enemies,False,pygame.sprite.collide_mask)
        #将发生碰撞的敌机复位（消失并重新绘制）
        if enemies_collided:
            for each in enemies_collided:
                #each.reset()        #添加敌机状态标记后，应删除该行，重新生成敌机在坠毁动画后操作
                each.active = False  #碰撞后，将敌机状态设置为False
        '''
        #显示得分
        score_surface = score_font.render("Score : %s" % str(score), True, WhiteFont)
        screen.blit(score_surface, (10,5))  #在左上角（10,5）的位置显示

        pygame.display.flip()
        clock.tick(60)

#避免main()函数被多次运行，即避免该python文件被其他python文件import时不被运行，
#即想要运行main()函数，只能直接运行该python文件（程序）
if __name__ == "__main__":
        main()


