import pygame
import random
import time

pygame.init()

W, H = 1050, 800

win = pygame.display.set_mode((W, H))

walkRight = [pygame.image.load('Imagens\Walk_R\Angel_WR_1.png'), pygame.image.load('Imagens\Walk_R\Angel_WR_2.png'), pygame.image.load('Imagens\Walk_R\Angel_WR_3.png'), pygame.image.load(
    'Imagens\Walk_R\Angel_WR_4.png'), pygame.image.load('Imagens\Walk_R\Angel_WR_5.png'), pygame.image.load('Imagens\Walk_R\Angel_WR_6.png'), pygame.image.load('Imagens\Walk_R\Angel_WR_7.png')]

walkLeft = [pygame.image.load('Imagens\Walk_L\Angel_WL_1.png'), pygame.image.load('Imagens\Walk_L\Angel_WL_2.png'), pygame.image.load('Imagens\Walk_L\Angel_WL_3.png'), pygame.image.load(
    'Imagens\Walk_L\Angel_WL_4.png'), pygame.image.load('Imagens\Walk_L\Angel_WL_5.png'), pygame.image.load('Imagens\Walk_L\Angel_WL_6.png'), pygame.image.load('Imagens\Walk_L\Angel_WL_7.png')]

monster0 = [pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_1.png'), pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_2.png'), pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_3.png'),
           pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_4.png'), pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_5.png'), pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_6.png'),
           pygame.image.load('Imagens\Monsters\Gol_1\L\Golem_01_W_7.png')]

monster1 = [pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_1.png'), pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_2.png'), pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_3.png'),
           pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_4.png'), pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_5.png'), pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_6.png'),
           pygame.image.load('Imagens\Monsters\Gol_2\L\Golem_02_W_7.png')]

monster2 = [pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_1.png'), pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_2.png'), pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_3.png'),
           pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_4.png'), pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_5.png'), pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_6.png'),
           pygame.image.load('Imagens\Monsters\Gol_3\L\Golem_03_W_7.png')]

monster3 = [pygame.image.load('Imagens\Monsters\Gol_4\Bird_1.png'), pygame.image.load('Imagens\Monsters\Gol_4\Bird_2.png'), pygame.image.load('Imagens\Monsters\Gol_4\Bird_3.png'),
           pygame.image.load('Imagens\Monsters\Gol_4\Bird_4.png'), pygame.image.load('Imagens\Monsters\Gol_4\Bird_5.png'), pygame.image.load('Imagens\Monsters\Gol_4\Bird_6.png'),
           pygame.image.load('Imagens\Monsters\Gol_4\Bird_7.png')]

bg_pause = pygame.image.load('Imagens\game_background_4.png').convert()
bg = pygame.image.load('Imagens\game_background_1.png').convert()
playerStand = pygame.image.load('Imagens\Angel_1.png')

clock = pygame.time.Clock()

animCount = 0
animCountM = 0

def score_count(score, font_color = (0, 0, 0), font_type = 'Config\TextL\Guest.ttf', font_size = 70):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(f'Score: {score}', True, font_color)
    win.blit(text, (50, 20))
    
    pygame.display.update()

def print_m(mess, x, y, font_color, font_size, font_type = 'Config\TextL\Guest.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(mess, True, font_color)
    win.blit(text, (x, y))

def deth():
    win.fill((0, 0, 0))
    print_m('YOU DEAD', W // 4 - 50, H // 4 + 100, (170, 43, 43), 150)
    print_m('PRESS "ENTER" TO RESTART', W // 4 - 150, H // 4 + 300, (40, 80, 40), 70)
    
    pygame.display.update()
    
    clock.tick(15)
    pause = True

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            mainGame()
            pause = False
            

def pause():
    win.blit(bg_pause, (0, 0))
    print_m('PAUSED', W // 4 - 50, H // 4 + 100, (170, 43, 43), 150)
    print_m('PRESS "LSHIFT" TO RETURN', W // 4 - 150, H // 4 + 300, (40, 150, 40), 70)
    
    pygame.display.update()    
    
    clock.tick(10)
    pause = True
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LSHIFT]:
            pause = False
    
def mainGame():
    run = True
    x = 50
    y = H - 150
    width = 100
    height = 150
    speed = 5
    score = 0
    animCount = 0
    jump = 8.5
    isJump = False
    jumpCount = jump
    left = False
    right = False
    x_bg = 0
    berr_st_x = random.randrange(W, W + 300)
    berr_st_y = y + 25
    berr_speed = 10
    berr_width = 100
    berr_height = 150
    animCountM = 0
    berr_class = random.randrange(0, 4)
    
    
    def drawWin():
        global animCount
    
        if animCount + 1 >= 30:
            animCount = 0
        if left:
            win.blit(walkLeft[animCount // 5], (x, y))
            animCount += 1
        elif right:
            win.blit(walkRight[animCount // 5], (x, y))
            animCount += 1
        else:
            win.blit(playerStand, (x, y))
        
        score_count(score)
    
        pygame.display.update()
    
    def berr(berr_x, berr_y, berr_w, berr_h):
        global animCountM
        
        if animCountM + 1 >= 7:
            animCountM = 0
        if berr_class == 0:
            win.blit(monster0[animCountM], (berr_x, berr_y))
        elif berr_class == 1:
            win.blit(monster1[animCountM], (berr_x, berr_y))
        elif berr_class == 2:
            win.blit(monster2[animCountM], (berr_x, berr_y))    
        else:
            win.blit(monster3[animCountM], (berr_x, berr_y + 10))
        animCountM += 1    
    
    while run:
        clock.tick(60)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_work = False       
        
        win.blit(bg, (0, 0))
        
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and x > speed:
            x -= speed
            left = True
            right = False
        elif key[pygame.K_RIGHT] and x < W - width - speed:
            x += speed
            left = False
            right = True
        elif key[pygame.K_ESCAPE]:
            pause()
        else:
            left = False
            right = False
            animCount = 0
        if not(isJump):
            if key[pygame.K_SPACE]:
                isJump = True
        else:
            if jumpCount >= -jump:
                if jumpCount < 0:
                    y += (jumpCount ** 2) / 4
                else:
                    y -= (jumpCount ** 2) / 4
                jumpCount -= 0.5
            else:
                isJump = False
                jumpCount = jump
        
        berr(berr_st_x, berr_st_y, berr_width, berr_height)
        berr_st_x -= berr_speed
        
        if berr_st_x < 0:
            score += 1
            berr_speed += 0.1
            animCountM = 0
            berr_st_x = 0 - berr_width
            berr_class = random.randrange(0, 4)
            berr_st_x = random.randrange(W, W + 300)
        
        if (berr_st_x < x + 50 and berr_st_x + berr_width > x + 50) and (y + height - 40 > berr_st_y):
            run = False
            deth()
        
        drawWin()

mainGame()

pygame.quit()
