'''
游戏框架：
1.导入python程序运行所需的环境模块sys，pygame模块，以及pygame.locals模块提供常用的常量和函数。
2.定义窗口大小，并创建窗口，设置游戏标题，以及加载背景。
3.定义主函数main()，设置程序退出机制，绘制背景图像，flip()方法刷新所有待显示的图像（更新整个窗口），设置程序运行的帧率。
'''
import sys
import pygame
from pygame.locals import *

pygame.init()

screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("飞机大战")
background = pygame.image.load("images/background.png").convert()

#定义main()函数用来管理主程序
def main():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(background,(0,0))
        pygame.display.flip()
        clock.tick(60)
#避免main()函数被多次运行，即避免该python文件被其他python文件import时不被运行，
#即想要运行main()函数，只能直接运行该python文件（程序）
if __name__ == "__main__":
        main()


