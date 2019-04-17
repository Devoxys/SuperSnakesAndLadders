import sys
import random
import math
import os
import pygame
from pygame.locals import *

WIDTH = 720
HEIGHT = 720
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
FPS = 60
BOARD_RED = (255, 77, 77)
BOARD_WHITE = (255, 255, 255)


def find_center(n):
    """Finds Center of tile n"""
    tens = n//10**1 % 10
    ones = n//10**0 % 10


def draw_board(screen):
    for i in range(11): # Borders
        pygame.draw.line(screen, (255, 77, 77), (60, 60+i * 60), (660, 60 + i * 60), 3)
        pygame.draw.line(screen, (255, 77, 77), (60 + i * 60, 60), (60 + i * 60, 660), 3)

    for i in range(10): # Squares and Numbers
        if i % 2 == 0:
            for j in range(5):
                left = 60 + 2 * j * 60
                top = 60 + i * 60
                tn = 100 - (10*i + 2*j)
                pygame.draw.rect(screen, (255, 77, 77), [left, top, 60, 60], 0)
                tnfont = pygame.font.Font(None, 24)
                tntext1 = tnfont.render(str(tn), 1, BOARD_WHITE)
                tntext1pos = tntext1.get_rect()
                tntext1pos.left = left + 5
                tntext1pos.top = top + 5
                tntext2 = tnfont.render(str(tn-1), 1, BOARD_RED)
                tntext2pos = tntext2.get_rect()
                tntext2pos.left = left + 65
                tntext2pos.top = top + 5
                screen.blit(tntext2, tntext2pos)
                screen.blit(tntext1, tntext1pos)
        else:
            for j in range(5):
                left = 120 + 2 * j * 60
                top = 60 + i * 60
                tn = 100 - (10*i + 2*j+1)
                pygame.draw.rect(screen, (255, 77, 77), [left, top, 60, 60], 0)
                tnfont = pygame.font.Font(None, 24)
                tntext1 = tnfont.render(str(tn), 1, BOARD_WHITE)
                tntext1pos = tntext1.get_rect()
                tntext1pos.left = left + 5
                tntext1pos.top = top + 5
                tntext2 = tnfont.render(str(tn + 1), 1, BOARD_RED)
                tntext2pos = tntext2.get_rect()
                tntext2pos.left = left - 55
                tntext2pos.top = top + 5
                screen.blit(tntext2, tntext2pos)
                screen.blit(tntext1, tntext1pos)




def main():
    """Main Game Code"""
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Super Duper Snakes and Ladders Deluxe 345/2 Days X3 Ultra')
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BOARD_WHITE)
    clock = pygame.time.Clock()
    startflag = True
    while startflag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
        screen.blit(background, (0, 0))
        draw_board(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()