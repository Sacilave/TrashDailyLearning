import sys
import pygame
from pygame.locals import *

pygame.init()
screen_size = width, height = 480, 700
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("RecordEvent")

f = open("record.txt", 'w')

while True:
    for event in pygame.event.get():
        f.write(str(event) + '\n')
        if event.type == QUIT:
            f.close()
            pygame.quit()
            sys.exit()
    pygame.display.flip()
