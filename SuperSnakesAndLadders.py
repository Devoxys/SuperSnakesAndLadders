import sys
import random
import math
import os
import pygame
from pygame.locals import *

WIDTH = 720
HEIGHT = 720
FPS = 60






def main():
    """Main Game Code"""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Super Duper Snakes and Ladders Deluxe 345/2 Days X3 Ultra')
    screen = pygame.display.get_surface()
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((13, 10, 51))
    clock = pygame.time.Clock()
    startflag = True
    while startflag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()