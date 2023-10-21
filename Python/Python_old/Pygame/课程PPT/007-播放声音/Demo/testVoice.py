import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
screen_size = width, height = 320, 480
pygame.display.set_mode(screen_size)
pygame.display.set_caption("testVoice")

voice = pygame.mixer.Sound("get_bomb.wav")
voice.play()
#pygame.mixer.music.load("game_music.ogg")
#pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            pygame.quit()
    pygame.display.flip()
