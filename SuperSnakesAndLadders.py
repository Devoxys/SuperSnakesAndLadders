import random
import pygame
from pygame.locals import *

WIDTH = 960
HEIGHT = 720
BOARD_WIDTH = 600
BOARD_HEIGHT = 600
FPS = 60
BOARD_RED = (255, 77, 77)
BOARD_WHITE = (255, 255, 255)
BOARD_YELLOW = (255, 255, 77)
BOARD_GREEN = (77, 255, 77)
BOARD_CYAN = (77, 255, 255)
BOARD_BLUE = (77, 77, 255)
BOARD_BLACK = (20, 20, 20)
COUNTER = 3


def find_center(n):
    """Finds Center of tile n"""
    tens = (n-1)//10**1 % 10
    ones = (n-1)//10**0 % 10
    if tens % 2 == 0:
        cy = 90 + 60*(9-tens)
        cx = 90 + 60*ones
    else:
        cy = 90 + 60*(9-tens)
        cx = 90 + 60*(9-ones)
    return cx, cy


def identify_square(pos):
    x = pos[0]
    y = pos[1]
    if x < 60 or y < 60 or x > 660 or y > 660:
        return -1
    ones = 10 - x // 60
    tens = 10 - y // 60
    if tens % 2 == 1:
        print('a', tens*10 + ones + 1)
        return tens*10 + ones + 1
    else:
        print('b', tens*10 + (10 - ones))
        return tens*10 + (10 - ones)


def draw_ladder(screen, start=-1, end=-1):
    if start == -1 and end == -1:
        start = random.randint(1, 56)
        end = start + random.randint(1, 30)
    name = [start, end]
    startx, starty = find_center(start)
    endx, endy = find_center(end)
    pygame.draw.line(screen, BOARD_YELLOW, (startx, starty), (endx, endy), 8)
    return name


def draw_snake(screen, start=-1, end=-1):
    if start == -1 and end == -1:
        start = random.randint(2, 99)
        end = random.randint(1, start-1)
    name = [start, end]
    startx, starty = find_center(start)
    endx, endy = find_center(end)
    pygame.draw.line(screen, BOARD_GREEN, (startx, starty), (endx, endy), 8)
    return sorted(name)


def generator(screen, num_snake, num_ladder, num_card):
    snakelist = []
    for i in range(num_snake):
        snakelist.append(draw_snake(screen))
    ladderlist = []
    for i in range(num_ladder):
        ladderlist.append(draw_ladder(screen))
    cardlist = random.sample(range(1, 99), num_card)
    return snakelist, ladderlist, cardlist


# Text generator would go here if I bother to refactor this


def draw_board(screen, counter, snakelist, ladderlist, cardlist):
    for i in range(11):  # Borders
        pygame.draw.line(screen, (255, 77, 77), (60, 60+i * 60), (660, 60 + i * 60), 3)
        pygame.draw.line(screen, (255, 77, 77), (60 + i * 60, 60), (60 + i * 60, 660), 3)

    for i in range(10):  # Squares and Numbers
        if i % 2 == 0:
            for j in range(5):
                left = 60 + 2 * j * 60
                top = 60 + i * 60
                tn = 100 - (10*i + 2*j)
                pygame.draw.rect(screen, (255, 77, 77), [left, top, 60, 60], 0)
                tnfont = pygame.font.SysFont('georgiattf', 20)
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
                tn = 100 - (10*i + (9-(2*j+1)))
                pygame.draw.rect(screen, (255, 77, 77), [left, top, 60, 60], 0)
                tnfont = pygame.font.SysFont('georgiattf', 20)
                tntext1 = tnfont.render(str(tn), 1, BOARD_WHITE)
                tntext1pos = tntext1.get_rect()
                tntext1pos.left = left + 5
                tntext1pos.top = top + 5
                tntext2 = tnfont.render(str(tn - 1), 1, BOARD_RED)
                tntext2pos = tntext2.get_rect()
                tntext2pos.left = left - 55
                tntext2pos.top = top + 5
                screen.blit(tntext2, tntext2pos)
                screen.blit(tntext1, tntext1pos)

    cladderfont = pygame.font.SysFont('georgiattf', 30)
    claddertext = cladderfont.render("Configure Ladders", 1, BOARD_BLACK)
    claddertextpos = claddertext.get_rect()
    claddertextpos.right = screen.get_rect().right - 30
    claddertextpos.top = screen.get_rect().top + 120
    cladderrect = Rect(claddertextpos.left - 10, claddertextpos.top - 10,
                       claddertextpos.width + 20, claddertextpos.height + 20)
    pygame.draw.rect(screen, BOARD_YELLOW, cladderrect, 0)
    screen.blit(claddertext, claddertextpos)

    csnakefont = pygame.font.SysFont('georgiattf', 30)
    csnaketext = csnakefont.render("Configure Snakes", 1, BOARD_BLACK)
    csnaketextpos = csnaketext.get_rect()
    csnaketextpos.left = claddertextpos.left
    csnaketextpos.top = claddertextpos.bottom + 40
    csnakerect = Rect(claddertextpos.left - 10, csnaketextpos.top - 10,
                      claddertextpos.width + 20, csnaketextpos.height + 20)
    pygame.draw.rect(screen, BOARD_GREEN, csnakerect, 0)
    screen.blit(csnaketext, csnaketextpos)

    confirmfont = pygame.font.SysFont('georgiattf', 30)
    confirmtext = confirmfont.render("Save Changes", 1, BOARD_BLACK)
    confirmtextpos = confirmtext.get_rect()
    confirmtextpos.left = claddertextpos.left
    confirmtextpos.top = csnaketextpos.bottom + 40
    confirmrect = Rect(claddertextpos.left - 10, confirmtextpos.top - 10,
                       claddertextpos.width + 20, confirmtextpos.height + 20)
    pygame.draw.rect(screen, BOARD_CYAN, confirmrect, 0)
    screen.blit(confirmtext, confirmtextpos)

    endturnfont = pygame.font.SysFont('georgiattf', 30)
    endturntext = endturnfont.render("End Turn", 1, BOARD_BLACK)
    endturntextpos = endturntext.get_rect()
    endturntextpos.left = claddertextpos.left
    endturntextpos.top = confirmtextpos.bottom + 40
    endturnrect = Rect(claddertextpos.left - 10, endturntextpos.top - 10,
                       claddertextpos.width + 20, endturntextpos.height + 20)
    pygame.draw.rect(screen, BOARD_RED, endturnrect, 0)
    screen.blit(endturntext, endturntextpos)

    counterfont = pygame.font.SysFont('georgiattf', 30)
    countertext = counterfont.render("Counter: " + str(counter), 1, BOARD_BLACK)
    countertextpos = countertext.get_rect()
    countertextpos.right = screen.get_rect().right
    countertextpos.bottom = screen.get_rect().bottom
    screen.blit(countertext, countertextpos)

    titlefont = pygame.font.SysFont('georgiattf', 35)
    titletext = titlefont.render("Welcome To Super Duper Snakes and Ladders DX!", 1, BOARD_BLACK)
    titletextpos = titletext.get_rect()
    titletextpos.top = screen.get_rect().top
    titletextpos.centerx = screen.get_rect().centerx
    screen.blit(titletext, titletextpos)

    for s in snakelist:
        draw_snake(screen, s[0], s[1])
    for l in ladderlist:
        draw_ladder(screen, l[0], l[1])
    for c in cardlist:
        cx, cy = find_center(c)
        cfont = pygame.font.SysFont('impactttf', 20)
        ctext = cfont.render("C", 1, (248, 82, 248))
        ctextpos = ctext.get_rect()
        ctextpos.centerx = cx
        ctextpos.centery = cy
        screen.blit(ctext, ctextpos)

    return cladderrect, csnakerect, confirmrect, endturnrect


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

    counter = 0
    snakes, ladders, cardspots = generator(screen, random.randint(4, 8), random.randint(4, 8), random.randint(30, 70))

    mode = "normal"
    edit_mode = 1
    edit_info = []

    screen.blit(background, (0, 0))
    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes, ladders, cardspots)
    cladderrect = Rect(cladderrect)
    csnakerect = Rect(csnakerect)
    confirmrect = Rect(confirmrect)
    endturnrect = Rect(endturnrect)
    pygame.display.flip()

    while startflag:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 0
            if event.type == MOUSEBUTTONDOWN:
                print(snakes)
                print(ladders)
                print(cardspots)
                print(identify_square(event.pos))
                if mode == "normal":
                    if endturnrect.collidepoint(event.pos):
                        counter -= 1
                        if counter <= 0:
                            counter = COUNTER
                            snakes, ladders, cardspots = generator(screen, random.randint(4, 12),
                                                                   random.randint(4, 12), random.randint(30, 70))
                        screen.blit(background, (0, 0))
                        cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                       snakes, ladders, cardspots)
                        pygame.display.flip()
                    if cladderrect.collidepoint(event.pos):
                        mode = 'ladder'
                        helpfont = pygame.font.SysFont('georgiattf', 24)
                        helptext = helpfont.render("Click on an end of {0} to remove".format(mode), 1, BOARD_BLACK)
                        helptextpos = helptext.get_rect()
                        helptextpos.bottom = screen.get_rect().bottom
                        screen.blit(background, (0, 0))
                        cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes,
                                                                                       ladders, cardspots)
                        screen.blit(helptext, helptextpos)
                        pygame.display.flip()
                    if csnakerect.collidepoint(event.pos):
                        mode = 'snake'
                        helpfont = pygame.font.SysFont('georgiattf', 24)
                        helptext = helpfont.render("Click on an end of {0} to remove".format(mode), 1, BOARD_BLACK)
                        helptextpos = helptext.get_rect()
                        helptextpos.bottom = screen.get_rect().bottom
                        screen.blit(background, (0, 0))
                        cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes,
                                                                                       ladders, cardspots)
                        screen.blit(helptext, helptextpos)
                        pygame.display.flip()
                    print(mode)
                else:
                    if confirmrect.collidepoint(event.pos):
                        edit_mode = 1
                        edit_info = []
                        mode = 'normal'
                        helpfont = pygame.font.SysFont('georgiattf', 24)
                        helptext = helpfont.render("Changes Saved.", 1, BOARD_BLACK)
                        helptextpos = helptext.get_rect()
                        helptextpos.bottom = screen.get_rect().bottom
                        screen.blit(background, (0, 0))
                        cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes, ladders,
                                                                                       cardspots)
                        screen.blit(helptext, helptextpos)
                        pygame.display.flip()
                    else:
                        if edit_mode == 1:
                            edit_info.append(identify_square(event.pos))
                            helpfont = pygame.font.SysFont('georgiattf', 24)
                            helptext = helpfont.render("Click on other end of {0} to remove".format(mode), 1,
                                                       BOARD_BLACK)
                            helptextpos = helptext.get_rect()
                            helptextpos.bottom = screen.get_rect().bottom
                            screen.blit(background, (0, 0))
                            cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes,
                                                                                           ladders, cardspots)
                            screen.blit(helptext, helptextpos)
                            pygame.display.flip()
                            edit_mode += 1
                        elif edit_mode == 2:
                            edit_info.append(identify_square(event.pos))
                            if mode == 'snake':
                                if -1 in edit_info:
                                    edit_info = []
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on an end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                                elif sorted(edit_info) not in snakes:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Not found, try again".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode = 1
                                else:
                                    snakes.remove(sorted(edit_info))
                                    edit_info = []
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on an end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                            elif mode == 'ladder':
                                if -1 in edit_info:
                                    edit_info = []
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on an end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                                elif sorted(edit_info) not in ladders:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Not found, try again".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode = 1
                                else:
                                    ladders.remove(sorted(edit_info))
                                    edit_info = []
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on an end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                        elif edit_mode == 3:
                            start = identify_square(event.pos)
                            if mode == 'snake':
                                if (start < 2 or start > 99) and start != -1:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Invalid. Try again.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                else:
                                    edit_info.append(start)
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on other end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes,
                                                                                                   ladders, cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                            elif mode == 'ladder':
                                if (start < 2 or start > 85) and start != -1:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Invalid. Try again.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes,
                                                                                                   ladders, cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                else:
                                    edit_info.append(start)
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Click on other end of new {0}".format(mode), 1,
                                                               BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                    edit_mode += 1
                        elif edit_mode == 4:
                            end = identify_square(event.pos)
                            if -1 in edit_info or end == -1:
                                edit_info = []
                                edit_mode = 1
                                mode = 'normal'
                                helpfont = pygame.font.SysFont('georgiattf', 24)
                                helptext = helpfont.render("Done.", 1, BOARD_BLACK)
                                helptextpos = helptext.get_rect()
                                helptextpos.bottom = screen.get_rect().bottom
                                screen.blit(background, (0, 0))
                                cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                               snakes, ladders,
                                                                                               cardspots)
                                screen.blit(helptext, helptextpos)
                                pygame.display.flip()
                            elif mode == "snake":
                                if ((end < 2 or end > 99) and end != -1) or end == edit_info[0]:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Invalid. Try again.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                else:
                                    edit_info.append(end)
                                    snakes.append(sorted(edit_info))
                                    edit_info = []
                                    edit_mode = 1
                                    mode = 'normal'
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Created Snake.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                            elif mode == "ladder":
                                if ((end < 2 or end > 85 or abs(edit_info[0] - end) > 30)
                                        and end != -1) or end == edit_info[0]:
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Invalid. Try again.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
                                else:
                                    edit_info.append(end)
                                    ladders.append(sorted(edit_info))
                                    edit_info = []
                                    edit_mode = 1
                                    mode = 'normal'
                                    helpfont = pygame.font.SysFont('georgiattf', 24)
                                    helptext = helpfont.render("Created Ladder.", 1, BOARD_BLACK)
                                    helptextpos = helptext.get_rect()
                                    helptextpos.bottom = screen.get_rect().bottom
                                    screen.blit(background, (0, 0))
                                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter,
                                                                                                   snakes, ladders,
                                                                                                   cardspots)
                                    screen.blit(helptext, helptextpos)
                                    pygame.display.flip()
            if event.type == KEYDOWN:
                if event.key == K_s:
                    screen.blit(background, (0, 0))
                    snakes = []
                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes, ladders,
                                                                                   cardspots)
                    pygame.display.flip()
                    pygame.display.flip()
                if event.key == K_l:
                    screen.blit(background, (0, 0))
                    ladders = []
                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes, ladders,
                                                                                   cardspots)
                    pygame.display.flip()

                if event.key == K_f:
                    screen.blit(background, (0, 0))
                    snakes, ladders = ladders, snakes
                    cladderrect, csnakerect, confirmrect, endturnrect = draw_board(screen, counter, snakes, ladders,
                                                                                   cardspots)
                    pygame.display.flip()


if __name__ == '__main__':
    main()