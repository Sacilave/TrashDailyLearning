"""
1. 导入环境变量模块 sys， 游戏模块 pygame ， pygame常用常量模块 pygame.locals
2. 初始化pygame， 设置窗口， 标题， 背景， 图标
3. 进入游戏主循环, 退出事件， 加载背景， 刷新屏幕
"""

import sys
import pygame
from pygame.locals import *
import plane


# 初始化pygame
pygame.init()

# 设置窗口
screen_size = width, height = 1024, 600

# 加载背景音乐
bgm = pygame.mixer.Sound("music/bgm_zhuxuanlv.ogg")
# 发射子弹声音
bullet_sound = pygame.mixer.Sound("music/effcet_sfx_beiji.ogg")
# 击毁声音
enemy_dead_sound = pygame.mixer.Sound("music/effcet_sfx_siwang.ogg")
# 角色死亡声音
player_dead_sound = pygame.mixer.Sound("music/effcet_sfx_polan.ogg")

down_img = pygame.image.load("images/bomb_img.png")
enemy_down_img = []
for i in range(6):
    enemy_down_img.append(down_img.subsurface(pygame.Rect(i*150, 0, 150, 150)))

# 统计得分
score = 0

def show_start_info(screen, bg):
    font1 = pygame.font.Font("font/xinwei.ttf", 80)
    tip1 = font1.render(u"飞机大战", True, (65, 105, 225))
    tip1_rect = tip1.get_rect()

    font2 = pygame.font.Font("font/xinwei.ttf", 40)
    tip2 = font2.render(u'按任意键开始游戏~~~', True, (65, 105, 225))
    tip2_rect = tip2.get_rect()

    screen.blit(bg, (0, 0))
    screen.blit(tip1, ((width-tip1_rect.width)/2, 300))
    screen.blit(tip2, ((width-tip2_rect.width)/2, 400))
    pygame.display.update()


# 定义一个函数来管理主程序
def running_game(screen, bg, clock):
    # 计数速率
    ticks = 0

    # 播放背景音乐
    bgm.set_volume(0.5)
    bgm.play(-1)

    # 生成我方飞机对象
    player_plane = plane.MyPlane(screen_size)

    # 敌方飞机的精灵组
    enemy_group = pygame.sprite.Group()

    # 游戏主循环
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            bgm.stop()
        # 计数器
        ticks += 1
        if ticks >= 120:
            ticks = 0
        # 生成敌方飞机
        if ticks % 110 == 0:
            enemy = plane.SmallEnemy(screen_size)
            enemy_group.add(enemy)
        # 生成子弹
        if keys[K_j]:
            if ticks % 20 == 0:
                player_plane.shoot("images/bullet8s.png")
                bullet_sound.play()

        # 绘制背景
        screen.blit(bg, (0, 0))
        # 移动我方飞机
        player_plane.move(keys)
        # 移动敌方飞机
        enemy_group.update()
        # 移动子弹
        player_plane.bullets.update()

        # 飞机与敌机碰撞检测
        if plane_collide_check(player_plane, enemy_group):
            player_plane.life -= 1
            if player_plane.life <= 0:
                # 生命之小于0，游戏结束
                return

        # 子弹与敌机碰撞检测
        bullet_collide_check(screen, player_plane.bullets, enemy_group)

        # 绘制子弹
        player_plane.bullets.draw(screen)
        # 绘制我方飞机
        screen.blit(player_plane.image, player_plane.rect)
        # 绘制敌方飞机
        enemy_group.draw(screen)

        # 显示分数
        show_text(screen, (5, 5), "SCORE:"+str(score), (0, 0, 0))
        pygame.display.flip()


# 飞机与敌机碰撞检测
def plane_collide_check(player_plane, enemy_group):
    player_hit = pygame.sprite.spritecollide(player_plane, enemy_group, True, pygame.sprite.collide_mask)
    if player_hit:
        player_dead_sound.play()
        player_plane.reset()
        return True


# 子弹与敌机碰撞检测
def bullet_collide_check(screen, bullets, enemy_group):
    enemy_hit = pygame.sprite.groupcollide(enemy_group, bullets, True, True, pygame.sprite.collide_mask)




def show_text(window, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # 获取系统字体，并设置文字大小
    cur_font = pygame.font.SysFont("font/xinwei.ttf", font_size)
    # 设置是否加粗属性
    cur_font.set_bold(font_bold)
    # 设置是否斜体属性
    cur_font.set_italic(font_italic)
    # 设置文字内容
    text_fmt = cur_font.render(text, 1, color)
    # 绘制文字
    window.blit(text_fmt, pos)


def gameover(screen, bg, clock):
    screen.blit(bg, (0, 0))
    show_text(screen, (width/2, height/2), "GAMEOVER！", (255, 0, 0))
    pygame.display.update()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_SPACE]:
            break


# 程序终止
def terminate():
    pygame.quit()
    sys.exit()


# 主函数
def main():
    # 生成窗口
    screen = pygame.display.set_mode(screen_size)
    # 设置背景图片
    bg = pygame.image.load("images/background.png").convert_alpha()
    # 设置窗口标题
    pygame.display.set_caption("飞机大战")
    # 设置窗口图标
    icon = pygame.image.load("images/icon.png").convert_alpha()
    pygame.display.set_icon(icon)
    # 设置时钟对象
    clock = pygame.time.Clock()
    while True:
        running_game(screen, bg, clock)
        gameover(screen, bg, clock)


if __name__ == "__main__":
    main()
