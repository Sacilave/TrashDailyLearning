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

pygame.init()

screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("飞机大战")
background = pygame.image.load("images/background.png").convert()

#加载背景音乐
pygame.mixer.music.load("sound/game_music.ogg")  #加载背景音乐文件
pygame.mixer.music.set_volume(0.2)  #设置音量
#定义将敌方小飞机添加到组的函数
def add_small_enemies(group1, group2, num):
    for small_enemy_num in range(15):
        each_small_enemy = enemy.SmallEnemy(screen_size)
        group1.add(each_small_enemy)
        group2.add(each_small_enemy)
#定义main()函数用来管理主程序
def main():
    pygame.mixer.music.play(-1)    #一直循环播放背景音乐
    clock = pygame.time.Clock()
    #生成我方飞机
    heroPlane = myplane.myPlane(screen_size)
    #创建敌方飞机组（动画精灵组）
    enemies = pygame.sprite.Group()
    #生成敌方飞机
    small_enemies = pygame.sprite.Group()  #创建敌方小飞机组（动画精灵组）
    add_small_enemies(small_enemies, enemies, 15)   #将生成的多个小飞机添加到敌方小飞机组以及敌方飞机组
    #用于切换飞机特效图像
    switch_image = True
    #用于切换特效的延迟
    delay = 100

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
        #绘制小型敌机
        for each in small_enemies:
            each.move()
            screen.blit(each.image, each.rect)
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

        pygame.display.flip()
        clock.tick(60)
#避免main()函数被多次运行，即避免该python文件被其他python文件import时不被运行，
#即想要运行main()函数，只能直接运行该python文件（程序）
if __name__ == "__main__":
        main()


