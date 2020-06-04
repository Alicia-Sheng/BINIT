# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 11:50:21 2019
"""

import pygame,sys, time, random

class draggables(pygame.sprite.Sprite):
    def _init_(self, xpos,ypos,id):
        super(draggables,self)._init_()
        self.image = pygame.image.load("bottle.png").convert()
        self.clicked = False
        self.rect = self.image.get_rect()
        self.rect.y = ypos
        self.rect.x = xpos
        self.id = id

icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)

Score = 0
Spawn_Key = random.randint(1,3)
Basket_Key = random.randint(1,3)
item_number = random.randint(1,3)

Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)
pygame.init()

display_width = 1280
display_height = 720

window = pygame.display.set_mode((display_width,display_height),pygame.FULLSCREEN)

pygame.display.set_caption("BIN IT!")

clock = pygame.time.Clock()
pygame.font.init
font = pygame.font.SysFont('Cocogoose Pro-trial.ttf', 32)

basket_h = 100
basket_w =100
basket_y_pos = 600

def restart_spawn():
    global Score
    global Spawn_Key
    global item_number
    Spawn_Key = random.randint(1,3)
    item_number = random.randint(1,3)
    print(Score)

def spawn(x,y,w,h):
    global window
    global Spawn_Key
    global item_number

    if Spawn_Key == 1:
        if item_number == 1:
            img = pygame.image.load("recyclable1.jpg")
            window.blit(img,(x,y))
        elif item_number == 2:
            img = pygame.image.load("recyclable2.jpg")
            window.blit(img,(x,y))
        elif item_number == 3:
            img = pygame.image.load("recyclable3.jpg")
            window.blit(img,(x,y))
        #pygame.draw.rect(window,Black,[x,y,w,h])
    if Spawn_Key == 2:
        if item_number == 1:
            img = pygame.image.load("compost1.jpg")
            window.blit(img,(x,y))
        elif item_number == 2:
            img = pygame.image.load("compost2.jpg")
            window.blit(img,(x,y))
        elif item_number == 3:
            img = pygame.image.load("compost3.jpg")
            window.blit(img,(x,y))
        #pygame.draw.rect(window,Red,[x,y,w,h])
    if Spawn_Key == 3:
        if item_number == 1:
            img = pygame.image.load("hazardous1.jpg")
            window.blit(img,(x,y))
        elif item_number == 2:
            img = pygame.image.load("hazardous2.jpg")
            window.blit(img,(x,y))
        elif item_number == 3:
            img = pygame.image.load("hazardous3.jpg")
            window.blit(img,(x,y))
        #pygame.draw.rect(window,Blue,[x,y,w,h])

def basket(x):
    global window
    global Basket_Key

    if Basket_Key == 1:
        img = pygame.image.load("recyclableCan.jpg")
        window.blit(img,(x-50,basket_y_pos))
        #pygame.draw.rect(window,Black,[x-50,basket_y_pos,basket_h,basket_w])
    if Basket_Key == 2:
        img = pygame.image.load("compostCan.jpg")
        window.blit(img,(x-50,basket_y_pos))
        #pygame.draw.rect(window,Red,[x-50,basket_y_pos,basket_h,basket_w])
    if Basket_Key == 3:
        img = pygame.image.load("hazardousCan.jpg")
        window.blit(img,(x-50,basket_y_pos))
        #pygame.draw.rect(window,Blue,[x-50,basket_y_pos,basket_h,basket_w])


def game_loop():
    global Score

    g_startx = random.randrange(0,display_width)
    g_starty = -100
    g_speed = 5
    g_width = 100
    g_height = 100

    run = True
    in_game = True

    while run:
        while in_game:
            pos = pygame.mouse.get_pos()
            mouse_x = pos[0]


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    run = False
    #            if event.type == pygame.MOUSEBUTTONDOWN:
    #                pos = pygame.mouse.get_pos()
    #                x = pos[0]
    #                y = pos[1]
    #                if event.button == 1:
    #                    #draggables_list.add(draggables(x,y,len(draggables_list)+1))
    #                    print('hi')
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        in_game = False
                        run = False

            if Score == 5:
                in_game = False

            if Score == 2 and g_speed == 5:
                g_speed = 6
            if Score == 4 and g_speed == 6:
                g_speed = 8


            window.fill(White)
            spawn(g_startx,g_starty,g_width,g_height)
            basket(mouse_x)
            g_starty += g_speed

            text = font.render('Score: ' + str(Score), True, Black)
            textRect = text.get_rect()
            window.blit(text, textRect)

            if g_starty > display_height:
                g_starty = -100
                restart_spawn()
                g_startx = random.randrange(0,display_width)


            g_boundaries = [(int(g_startx), int(g_startx + g_width)), (int(g_starty - g_height/2),int(g_starty + g_height/2))]
            basket_boundaries = [(int(mouse_x - basket_w/2), int(mouse_x + basket_w/2)), (int(basket_y_pos - basket_h/2),int(basket_y_pos + basket_h/2))]

            if g_boundaries[1][0] in range(basket_y_pos-basket_h, basket_y_pos+basket_h) or g_boundaries[1][1] in range(basket_y_pos-basket_h, basket_y_pos+basket_h):
                if g_boundaries[0][0] <= basket_boundaries[0][1] and g_boundaries[0][1] >= basket_boundaries[0][1]:
                    g_starty = -100
                    g_startx = random.randrange(0,display_width)
                    if Spawn_Key == Basket_Key:
                        Score+=1
                    else:
                        Score-=1
                    restart_spawn()
                elif g_boundaries[0][1] >= basket_boundaries[0][0] and g_boundaries[0][0] <= basket_boundaries[0][1]:
                    g_starty = -100
                    g_startx = random.randrange(0,display_width)
                    if Spawn_Key == Basket_Key:
                        Score+=1
                    else:
                        Score-=1
                    restart_spawn()



            pygame.display.update()
            clock.tick(60)

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

        #text = font.render("You've Won!", True, Black)
        #textRect = text.get_rect()

        #window.blit(text, (640,360))
        imgEnd = pygame.image.load("Picture1.png")
        window.blit(imgEnd,(100,100))
        pygame.display.update()

game_loop()

pygame.quit()
