# 导入系统环境模块sys(退出模块)   导入pygame  导入pygame.Locals
import sys
import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()
# 设置窗口大小
screen_size = width, height = 1024,600
screen = pygame.display.set_mode(screen_size)
#设置标题
pygame.display.set_caption("飞机大战")
# 设置图标
icon = pygame.image.load("images/icon.png").convert_alpha()
pygame.display.set_icon(icon)
# 设置背景
bg = pygame.image.load("images/background.png").convert_alpha()
# 加载背景音乐
bgm = pygame.mixer.Sound("music/bgm_zhuxuanlv.ogg")
# 设置音量
bgm.set_volume(0.1)

# 定义函数
def main():
    # 播放背景音乐
    bgm.play(-1)
    # 设置时钟对象
    clock = pygame.time.Clock()

    running = True  # 运行 = 正确
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # 加载背景
        screen.blit(bg,(0,0))





        # 刷新屏幕窗口
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__' :
    main()


