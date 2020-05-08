import pygame
import random
import sys
import time

pygame.init()

WIDTH = 500
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Dodge it!')
GAME_OVER = False
CLOCK = pygame.time.Clock()
SPEED = 1

ew_list = []

previousscore = 0
curscore = 0
player_pos = [168, 470]

#colours
BLACK = (0,0,0)
WHITE = (255, 255, 255)
DARKBLUE = (0, 0, 200)
DARKRED = (200, 0, 0)
DARKGREEN = (68, 179, 85)
LIGHTBLUE = (0, 0, 255)
PINK = (255, 0, 0)
LIGHTGREEN = (128, 208, 171)

#images
bg = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\background.jpg')
garbage= pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\garbage.png')
garbage = pygame.transform.scale(garbage, (90, 96)).convert_alpha()
mosquito = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\mosquito.png')
mosquito = pygame.transform.scale(mosquito, (91, 80)).convert_alpha()
toilet = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\toilet.png')
toilet = pygame.transform.scale(toilet, (90, 105)).convert_alpha()
glassshards = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\glassshards.png')
glassshards = pygame.transform.scale(glassshards, (120, 80)).convert_alpha()
bananapeel = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\bananapeel.png')
bananapeel = pygame.transform.scale(bananapeel, (110, 80)).convert_alpha()
doge = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\doge.png')
doge = pygame.transform.scale(doge, (100, 100)).convert_alpha()
poo = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\poo.png')
poo = pygame.transform.scale(poo, (90, 90)).convert_alpha()
player = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\player.png')
player = pygame.transform.scale(player, (165, 130)).convert_alpha()
lettuce = pygame.image.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\lettuce.png')
lettuce = pygame.transform.scale(lettuce, (150, 150)).convert_alpha()

def more_ew(ew_l):
    delay = random.random()
    ewpicker = random.randint(0,6)
    if len(ew_l) <= 5 and delay < 0.005:
        ew_pos = [random.randint(0,WIDTH-80), 0]
        ew_list.append([ewpicker, ew_pos])

def draw_ew(ew_l):
    for ew in ew_l:
        ewpicker = ew[0]
        if ewpicker == 0:
            screen.blit(garbage, tuple(ew[1]))
        elif ewpicker == 1:
            screen.blit(mosquito, tuple(ew[1]))
        elif ewpicker == 2:
            screen.blit(glassshards, tuple(ew[1]))
        elif ewpicker == 3:
            screen.blit(bananapeel, tuple(ew[1]))
        elif ewpicker == 4:
            screen.blit(doge, tuple(ew[1]))
        elif ewpicker == 5:
            screen.blit(poo, tuple(ew[1]))
        else:
            screen.blit(toilet, tuple(ew[1]))

def update_pos(ew_l):
    for idx, ew in enumerate(ew_l):
        global previousscore
        global curscore
        global SPEED
        ew_pos = ew[1]
        if ew_pos[1] >= 0 and ew_pos[1] < HEIGHT:
            if curscore%10 == 0 and previousscore != curscore:
                SPEED += 1
                previousscore = curscore
            ew_pos[1] += SPEED
        else:
            ew_l.pop(idx)
            curscore += 1

def didyoudodgeit(player_posi, ew):
    p_x = player_posi[0]
    p_y = player_posi[1]
    f_x = ew[1][0]
    f_y = ew[1][1]
    if (f_y >= p_y and f_y < (p_y + 80)) or (p_y >= f_y and p_y < (f_y + 75)):
        if (f_x >= p_x and f_x <= (p_x + 165)) or (p_x >= f_x and p_x <= (f_x + 90)):
            return True
    return False

def score(ew_l, player_posi):
    for ew in ew_l:
        if didyoudodgeit(player_posi, ew):
            return True
    return False


def message_to_screen(msg, x, y, size):
    fontObj = pygame.font.Font("freesansbold.ttf", size)
    textSurface = fontObj.render(msg, True, BLACK)
    textRect = textSurface.get_rect()
    textRect.center = (x, y)
    screen.blit(textSurface, textRect)


def button(msg, x, y, width, height, inactive_color, active_color, action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x+width > mouse[0] > x and y+height > mouse[1] > y):
        pygame.draw.rect(screen, active_color, (x, y, width, height))
        if (click[0] == 1 and action != None):
            if (action == "play"):
                main()
            elif (action == "quit"):
                pygame.quit()
                sys.exit()
            elif (action == "help"):
                help_page()
            elif (action == "back"):
                game_intro()
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, width, height))
    message_to_screen(msg, (x + (width/2)), (y + (height/2)), 20)

def help_page():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(WHITE)
        message_to_screen("How to Play", 250, 160, 50)
        message_to_screen("Use left and right arrow keys to move.", 250, 240, 20)
        message_to_screen("Dodge as many nasties as you can!,", 250, 270, 20)
        message_to_screen("Lettuce play!", 250, 350, 20)
        screen.blit(lettuce, (300,400))
        button("Back", 50, 450, 100, 50, LIGHTBLUE, LIGHTBLUE, "back")
        pygame.display.update()
        CLOCK.tick(15)


def game_intro():
    pygame.mixer.music.load(r'C:\Users\Ann Gie\Desktop\python\Dodge It\images\flamingo.mp3')
    pygame.mixer.music.play(-1,11.0)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.blit(bg, (0,0))
        message_to_screen("DODGE IT!", WIDTH/2, HEIGHT/2 - 80, 60)
        button("Start", 60, 360, 100, 50, DARKGREEN, LIGHTGREEN, "play")
        button("Help", 200, 360, 100, 50, DARKBLUE, LIGHTBLUE, "help")
        button("Quit", 340, 360, 100, 50, DARKRED, PINK, "quit")
        pygame.display.update()
        CLOCK.tick(15)


def main():
    while not GAME_OVER:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                x = player_pos[0]
                if event.key == pygame.K_LEFT:
                    x -= 40
                elif event.key == pygame.K_RIGHT:
                    x += 40
                player_pos[0] = x
        
        screen.blit(bg, (0, 0))
        screen.blit(player, (player_pos[0], player_pos[1]))

        more_ew(ew_list)
        update_pos(ew_list)
        if score(ew_list, player_pos):
            message_to_screen("Score: " + str(curscore), WIDTH/2, HEIGHT/2, 40)
            pygame.display.update()
            time.sleep(5)
            break
        draw_ew(ew_list)
        pygame.display.update()
        CLOCK.tick(60)
    pygame.quit()
    sys.exit()


game_intro()