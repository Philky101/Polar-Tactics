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
colorDGreen = (0, 255, 0)
colorLGreen = (0, 210, 0)
colorBlue = (0, 0, 255)
colorRed = (255, 0, 0)
colorWhite = (0, 0, 0)
colorBlack = (255, 255, 255)
colorGrey = (50, 50, 50)

#Clock
clock = pygame.time.Clock()
msPerUpdate = 16

#Game Loop
running = True
while running:

    #Keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
    
    #RGB of Background
    screen.fill(colorGrey)
    pygame.draw.rect(screen, colorGrey, (0, 0, screenWidth, screenHeight))

    #Checks Framerate
    dt = clock.tick(60)

    pygame.display.update()
