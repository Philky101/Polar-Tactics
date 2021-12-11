import pygame
import random
import math
from pygame import mixer

#Creates Screen
screenWidth = 1024
screenHeight = 1024
screen = pygame.display.set_mode((screenWidth, screenHeight))
border = ((screenHeight+screenWidth)/2)/16

#Background Sound
#mixer.music.load(NAME)
#mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Arctic Antics")
#icon = pygame.image.load(NAME)
#pygame.display.set_icon(icon)

#Font
pygame.font.init()
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#Colors
colorLGreen = (0, 255, 0)
colorDGreen = (0, 110, 0)
colorBlue = (0, 0, 255)
colorRed = (255, 0, 0)
colorBlack = (0, 0, 0)
colorWhite = (255, 255, 255)
colorGrey = (50, 50, 50)

#Clock
clock = pygame.time.Clock()
msPerUpdate = 16

#Keypresses
global escPressed
escPressed = False

def pause_menu():
    
    menuPosition = 1
    pressed = 0
    while True:

        screen.fill(colorGrey)
        
        if(menuPosition == 1):
            cont = font.render("Continue", True, colorLGreen)
            sett = font.render("Settings", True, colorDGreen)
            leave = font.render("Quit", True, colorDGreen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        escPressed = False
                        return True
        if(menuPosition == 2):
            cont = font.render("Continue", True, colorDGreen)
            sett = font.render("Settings", True, colorLGreen)
            leave = font.render("Quit", True, colorDGreen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        escPressed = False
                        return True
        if(menuPosition == 3):
            cont = font.render("Continue", True, colorDGreen)
            sett = font.render("Settings", True, colorDGreen)
            leave = font.render("Quit", True, colorLGreen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        running = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and pressed == 0:
                    if(menuPosition >= 3):
                        menuPosition = 1
                    else:
                        menuPosition += 1
                    pressed += 1
                if event.key == pygame.K_UP and pressed == 0:
                    if(menuPosition <= 1):
                        menuPosition = 3
                    else:
                        menuPosition -= 1
                    pressed += 1
            if event.type == pygame.KEYUP:
                pressed = 0
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        screen.blit(cont, ((screenWidth/2)-(textX*8), screenHeight/2 - screenHeight/4))
        screen.blit(sett, ((screenWidth/2)-(textX*8), screenHeight/2))
        screen.blit(leave, ((screenWidth/2)-(textX*4), screenHeight/2 + screenHeight/4))
        #debug = font.render(str(pressed), True, colorRed)
        #screen.blit(debug, ((screenWidth/2)-(textX*4), screenHeight/2 + screenHeight/6))
        pygame.display.update()

def drawGameMap(mapX, mapY, mapNum):
    tileX = 0
    tileY = 0
    mapXOffset = 0
    mapYOffset = 0
    tileSize = 63
    xGreaterThanY = True
    if screenWidth >= screenHeight:
        xGreaterThanY = True
        mapXOffset = (screenWidth-screenHeight)/2
        tileSize = (screenHeight/mapY)-2
    else:
        xGreaterThanY = False
        mapYOffset = (screenHeight-screenWidth)/2
        tileSize = (screenWidth/mapX)-2
    for i in range(mapY):
        for j in range(mapX):
            if(mapNum[i*mapX+j]==1):
                if xGreaterThanY:
                    tileX = (j*(screenHeight/mapY))+1+mapXOffset
                    tileY = (i*(screenHeight/mapY))+1
                else:
                    tileX = (j*(screenWidth/mapX))+1
                    tileY = (i*(screenWidth/mapX))+1+mapYOffset
                pygame.draw.rect(screen, colorBlack, (tileX, tileY, tileSize, tileSize))
            elif(mapNum[i*mapX+j]==0):
                if xGreaterThanY:
                    tileX = (j*(screenHeight/mapY))+1+mapXOffset
                    tileY = (i*(screenHeight/mapY))+1
                else:
                    tileX = (j*(screenWidth/mapX))+1
                    tileY = (i*(screenWidth/mapX))+1+mapYOffset
                pygame.draw.rect(screen, colorWhite, (tileX, tileY, tileSize, tileSize))

#Game Loop
running = True
while running:

    #RGB of Background
    screen.fill(colorWhite)
    #pygame.draw.rect(screen, colorGrey, (border, border, screenWidth-2*border, screenHeight-2*border))

    #Pause Menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_menu()

    #Checks Framerate
    dt = clock.tick(60)

    pygame.display.update()
