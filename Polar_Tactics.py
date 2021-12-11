import pygame
import random
import math
from pygame import mixer

#Creates Screen
screenWidth = 1024
screenHeight = 1024
screen = pygame.display.set_mode((screenWidth, screenHeight))

#Background Sound
#mixer.music.load(NAME)
#mixer.music.play(-1)

#Title and Icon
pygame.display.set_caption("Ray Caster")
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

def pause_menu(initialState):
    
    menuPosition = initialState
    while True:

        if(menuPosition == 1):
            screen.fill(colorGrey)
            cont = font.render("Continue", True, colorLGreen)
            sett = font.render("Settings", True, colorDGreen)
            leave = font.render("Quit", True, colorDGreen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menuPosition = 1
                        escPressed = False
                        return True
        if(menuPosition == 2):
            screen.fill(colorGrey)
            cont = font.render("Continue", True, colorDGreen)
            sett = font.render("Settings", True, colorLGreen)
            leave = font.render("Quit", True, colorDGreen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        menuPosition = 1
                        escPressed = False
                        return True
        if(menuPosition == 3):
            screen.fill(colorGrey)
            cont = font.render("Continue", True, colorDGreen)
            sett = font.render("Settings", True, colorDGreen)
            leave = font.render("Quit", True, colorLGreen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.quit()
                        running = False
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if(menuPosition >= 3):
                        menuPosition = 1
                    else:
                        menuPosition += 1
                if event.key == pygame.K_UP:
                    if(menuPosition <= 1):
                        menuPosition = 3
                    else:
                        menuPosition -= 1
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        screen.blit(cont, ((screenWidth/2)-(textX*8), screenHeight/2 - screenHeight/4))
        screen.blit(sett, ((screenWidth/2)-(textX*8), screenHeight/2))
        screen.blit(leave, ((screenWidth/2)-(textX*4), screenHeight/2 + screenHeight/4))

#Game Loop
running = True
while running:

    #RGB of Background
    screen.fill(colorWhite)
    #pygame.draw.rect(screen, colorGrey, (0, 0, screenWidth, screenHeight))

    #Pause Menu
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pause_menu(1)

    #Checks Framerate
    dt = clock.tick(60)

    pygame.display.update()
