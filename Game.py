# -*- coding: cp1251 -*-
import pygame #     I IIIII IIIII IIIII IIIII IIIII
pygame.init() #     I I I I IIIII I   I IIIII   I
import time   #     I I I I I     I   I I I     I
import browser#     I I I I I     IIIII I  I    I
import dataclasses




events = []


def setup_events():
    def on_down(e):
        # browser.console.dir(e)
        # print(e.keyCode)
        if not e.repeat:
            events.append(pygame.event.Event(pygame.KEYDOWN, key=e.keyCode))
    def on_up(e):
        events.append(pygame.event.Event(pygame.KEYUP, key=e.keyCode))
    browser.document.onkeydown = on_down
    browser.document.onkeyup = on_up

setup_events()


#Обьявления переменных
Window_Size = [950, 750]
IsWorking = True
hero1_c = [950-80, 750-80]
hero2_c = [0, 0]
shoot1_c = [-1, -1]
shoot2_c = [-1, -1]
shoot1_v = None
shoot2_v = None
hero_speed = 0.75
IsUp = [False, False]
IsDown = [False, False]
IsLeft = [False, False]
IsRight = [False, False]
IsBlueShooted = False
IsRedShooted = False


counter1 = 0

counter2 = 0

#Обьявления функций
#Hero1 = red
#Hero2 = blue
screen = pygame.display.set_mode(Window_Size)
pygame.display.set_caption("Tank's")
font = pygame.font.Font(pygame.font.get_default_font(), 10)
background = pygame.image.load("texture/pole.png").convert_alpha()
shoot_blue = pygame.image.load("texture/shoot blue.png").convert_alpha()
shoot_red = pygame.image.load("texture/shoot red.png").convert_alpha()
hero1_up = pygame.image.load("texture/tank red1.png").convert_alpha()
hero2_down = pygame.image.load("texture/tank blue3.png").convert_alpha()
hero1_down = pygame.image.load("texture/tank red3.png").convert_alpha()
hero2_up = pygame.image.load("texture/tank blue1.png").convert_alpha()
hero1_left = pygame.image.load("texture/tank red2.png").convert_alpha()
hero2_left = pygame.image.load("texture/tank blue4.png").convert_alpha()
hero1_right = pygame.image.load("texture/tank red4.png").convert_alpha()
hero2_right = pygame.image.load("texture/tank blue2.png").convert_alpha()

#Обьявления переменных
WhatDraw1 = hero1_up
WhatDraw2 = hero2_up

#Главный Цикл
def iteration():
    locals().update(globals())
    #Проверка выхода из игры
    for e in events:
        if e.type == pygame.QUIT:
            IsWorking = False
            
        #Перехват нажатий
        if e.type == pygame.KEYDOWN:
            print(e.key)
            if e.key == 38:
                IsUp[0] = True
                IsDown[0] = False
                IsLeft[0] = False
                IsRight[0] = False
            elif e.key == 40:
                IsDown[0] = True
                IsUp[0] = False
                IsLeft[0] = False
                IsRight[0] = False
            elif e.key == 37:
                IsLeft[0] = True
                IsUp[0] = False
                IsDown[0] = False
                IsRight[0] = False
            elif e.key == 39:
                IsRight[0] = True
                IsUp[0] = False
                IsDown[0] = False
                IsLeft[0] = False
                
            elif e.key == 87:
                IsUp[1] = True
                IsDown[1] = False
                IsLeft[1] = False
                IsRight[1] = False
            elif e.key == 83:
                IsDown[1] = True
                IsUp[1] = False
                IsLeft[1] = False
                IsRight[1] = False
            elif e.key == 65:
                IsUp[1] = False
                IsDown[1] = False
                IsRight[1] = False
                IsLeft[1] = True
            elif e.key == 68:
                IsRight[1] = True
                IsUp[1] = False
                IsDown[1] = False
                IsLeft[1] = False
            elif e.key == 81:
                if IsBlueShooted != True:
                    IsBlueShooted = True
                    shoot2_c = list(hero2_c)
                    shoot2_v = WhatDraw2

            elif e.key == 191:
                if IsRedShooted != True:
                    IsRedShooted = True
                    shoot1_c = list(hero1_c)
                    shoot1_v = WhatDraw1
                
                
        elif e.type == pygame.KEYUP:
            if e.key == 38:
                IsUp[0] = False
            elif e.key == 40:
                IsDown[0] = False
            elif e.key == 37:
                IsLeft[0] = False
            elif e.key == 39:
                IsRight[0] = False
                
            elif e.key == 87:
                IsUp[1] = False
            elif e.key == 83:
                IsDown[1] = False
            elif e.key == 65:
                IsLeft[1] = False
            elif e.key == 68:
                IsRight[1] = False
    events.clear()
    #Перемещение игроков           
    if IsUp[0] == True:
        hero1_c[1] = hero1_c[1] - hero_speed
    if IsDown[0] == True:
        hero1_c[1] = hero1_c[1] + hero_speed
    if IsLeft[0] == True:
        hero1_c[0] = hero1_c[0] - hero_speed
    if IsRight[0] == True:
        hero1_c[0] = hero1_c[0] + hero_speed
        
    if IsUp[1] == True:
        hero2_c[1] = hero2_c[1] - hero_speed
    if IsDown[1] == True:
        hero2_c[1] = hero2_c[1] + hero_speed
    if IsLeft[1] == True:
        hero2_c[0] = hero2_c[0] - hero_speed
    if IsRight[1] == True:
        hero2_c[0] = hero2_c[0] + hero_speed
        
    #Проверка выхода за поле
    if hero1_c[0] > 950-80:
        hero1_c[0] = hero1_c[0] - hero_speed
    if hero1_c[0] < 0:
        hero1_c[0] = hero1_c[0] + hero_speed
    if hero1_c[1] > 751-80:
        hero1_c[1] = hero1_c[1] - hero_speed
    if hero1_c[1] < 0:
        hero1_c[1] = hero1_c[1] + hero_speed
        
    if hero2_c[0] > 951-80:
        hero2_c[0] = hero2_c[0] - hero_speed
    if hero2_c[0] < 0:
        hero2_c[0] = hero2_c[0] + hero_speed
    if hero2_c[1] > 751-80:
        hero2_c[1] = hero2_c[1] - hero_speed
    if hero2_c[1] < 0:
        hero2_c[1] = hero2_c[1] + hero_speed

    #Проверка попаданий
    if shoot1_c[0] < hero2_c[0] and shoot1_c[0] > hero2_c[0] - 40:
        if shoot1_c[1] > hero2_c[1] and shoot1_c[1] < hero2_c[1] + 40:
            print('popal blen')
            counter1 = counter1 + 1
            hero2_c = [0, 0]
            shoot1_c = [-1, -1]

    if shoot1_c[1] < hero2_c[1] and shoot1_c[1] > hero2_c[1] - 40:
        if shoot1_c[0] > hero2_c[0] and shoot1_c[0] < hero2_c[0] + 40:
            print('popal blen')
            counter2 = counter2 + 1
            hero1_c = [950, 750]
            shoot1_c = [-1, -1]

    if shoot2_c[0] < hero1_c[0] and shoot2_c[0] > hero1_c[0] - 40:
        if shoot2_c[1] > hero1_c[1] and shoot2_c[1] < hero1_c[1] + 40:
            print('popal blen')
            counter1 = counter1 + 1
            hero2_c = [0, 0]
            shoot2_c = [-1, -1]

    if shoot2_c[1] < hero1_c[1] and shoot2_c[1] > hero1_c[1] - 40:
        if shoot2_c[0] > hero1_c[0] and shoot2_c[0] < hero1_c[0] + 40:
            print('popal blen')
            counter2 = counter2 + 1
            hero1_c = [950, 750]
            shoot2_c = [-1, -1]
        
    #Перезарядка
    if shoot1_c[0] > 950:
        shoot1_c = [-1, -1]
        shoot1_v = None
        IsRedShooted = False
    if shoot1_c[0] < 0:
        shoot1_c = [-1, -1]
        shoot1_v = None
        IsRedShooted = False
    if shoot1_c[1] > 751:
        shoot1_c = [-1, -1]
        shoot1_v = None
        IsRedShooted = False
    if shoot1_c[1] < 0:
        shoot1_c = [-1, -1]
        shoot1_v = None
        IsRedShooted = False

    if shoot2_c[0] > 950:
        shoot2_c = [-1, -1]
        shoot2_v = None
        IsBlueShooted = False
    if shoot2_c[0] < 0:
        shoot2_c = [-1, -1]
        shoot2_v = None
        IsBlueShooted = False
    if shoot2_c[1] > 751:
        shoot2_c = [-1, -1]
        shoot2_v = None
        IsBlueShooted = False
    if shoot2_c[1] < 0:
        shoot2_c = [-1, -1]
        shoot2_v = None
        IsBlueShooted = False
        
    #Просчет изображений
    if IsUp[0] == True:
        WhatDraw1 = hero1_up
    if IsDown[0] == True:
        WhatDraw1 = hero1_down
    if IsLeft[0] == True:
        WhatDraw1 = hero1_left
    if IsRight[0] == True:
        WhatDraw1 = hero1_right
        
    if IsUp[1] == True:
        WhatDraw2 = hero2_up
    if IsDown[1] == True:
        WhatDraw2 = hero2_down
    if IsLeft[1] == True:
        WhatDraw2 = hero2_left
    if IsRight[1] == True:
       WhatDraw2 = hero2_right

    # TODO: fix counter rendering
    text1 = font.render(str(counter1), 1, [0, 0, 255])
    text2 = font.render(str(counter2), 1, [255, 0, 0])

    screen.fill((255, 255, 255))
    screen.blit(background, [0, 0])
    screen.blit(text1, [150, 100])
    screen.blit(text2, [750, 100])
    screen.blit(WhatDraw1, [int(hero1_c[0]), int(hero1_c[1])])
    screen.blit(WhatDraw2, [int(hero2_c[0]), int(hero2_c[1])])
    
    #Проверка выстрела
    if shoot2_c[1] != -1:
        if shoot2_v == hero2_up:
            shoot2_c[1] = shoot2_c[1] - 5
            screen.blit(shoot_blue, [shoot2_c[0]+36, shoot2_c[1]])
        if shoot2_v == hero2_down:
            shoot2_c[1] = shoot2_c[1] + 5
            screen.blit(shoot_blue, [shoot2_c[0]+36, shoot2_c[1]])
        if shoot2_v == hero2_left:
            shoot2_c[0] = shoot2_c[0] - 5
            screen.blit(shoot_blue, [shoot2_c[0], shoot2_c[1]+36])
        if shoot2_v == hero2_right:
            shoot2_c[0] = shoot2_c[0] + 5
            screen.blit(shoot_blue, [shoot2_c[0], shoot2_c[1]+36])
            
    if shoot1_c[1] != -1:
        if shoot1_v == hero1_up:
            shoot1_c[1] = shoot1_c[1] - 5
            screen.blit(shoot_red, [shoot1_c[0]+36, shoot1_c[1]])
        if shoot1_v == hero1_down:
            shoot1_c[1] = shoot1_c[1] + 5
            screen.blit(shoot_red, [shoot1_c[0]+36, shoot1_c[1]])
        if shoot1_v == hero1_left:
            shoot1_c[0] = shoot1_c[0] - 5
            screen.blit(shoot_red, [shoot1_c[0], shoot1_c[1]+36])
        if shoot1_v == hero1_right:
            shoot1_c[0] = shoot1_c[0] + 5
            screen.blit(shoot_red, [shoot1_c[0], shoot1_c[1]+36])
    
    #Прорисовка на экран
    pygame.display.flip()

    #Ожидание для ФПС
    globals().update(locals())
    browser.timer.set_timeout(iteration, 0.03)

iteration()
# Выход из игры
# pygame.quit()
