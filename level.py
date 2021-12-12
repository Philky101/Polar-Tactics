import pygame
import math

class Level():

    def __init__(self, game, mapArray):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.mapData = mapArray

    def displayLevel(self):
        self.run_display = True
        while True:
            self.game.checkEvents()
            self.checkInput()
            self.drawMap()
            self.blitScreen()     

    def drawMap(self):
        tileX = 0
        tileY = 0
        mapXOffset = 0
        mapYOffset = 0
        mapNum = self.mapData
        mapX = int(math.sqrt(int(len(mapNum))))
        mapY = mapX
        border = ((self.game.DISPLAY_H+self.game.DISPLAY_W)/2)/16
        tileSize = 63
        xGreaterThanY = True
        self.game.window.fill(self.game.LBLUE)
        if self.game.DISPLAY_W >= self.game.DISPLAY_H:
            xGreaterThanY = True
            mapXOffset = (self.game.DISPLAY_W-self.game.DISPLAY_H-(2*border))/2
            tileSize = ((self.game.DISPLAY_H-(2*border))/mapY)
        else:
            xGreaterThanY = False
            mapYOffset = (self.game.DISPLAY_H-self.game.DISPLAY_W-(2*border))/2
            tileSize = ((self.game.DISPLAY_W-(2*border))/mapX)
        for i in range(mapY):
            for j in range(mapX):
                if(mapNum[i*mapX+j]==1):
                    if xGreaterThanY:
                        tileX = (j*((self.game.DISPLAY_H-2*border)/mapY))+border
                        tileY = (i*((self.game.DISPLAY_H-2*border)/mapY))+border
                    else:
                        tileX = (j*((self.game.DISPLAY_W-2*border)/mapX))+border
                        tileY = (i*((self.game.DISPLAY_W-2*border)/mapX))+border
                    pygame.draw.rect(self.game.window, self.game.YELLOW, (tileX, tileY, tileSize, tileSize))
                elif(mapNum[i*mapX+j]==0):
                    if xGreaterThanY:
                        tileX = (j*((self.game.DISPLAY_H-2*border)/mapY))+border
                        tileY = (i*((self.game.DISPLAY_H-2*border)/mapY))+border
                    else:
                        tileX = (j*((self.game.DISPLAY_W-2*border)/mapX))+border
                        tileY = (i*((self.game.DISPLAY_W-2*border)/mapX))+border
                    pygame.draw.rect(self.game.window, self.game.WHITE, (tileX, tileY, tileSize, tileSize))
                elif(mapNum[i*mapX+j]==2):
                    if xGreaterThanY:
                        tileX = (j*((self.game.DISPLAY_H-2*border)/mapY))+border
                        tileY = (i*((self.game.DISPLAY_H-2*border)/mapY))+border
                    else:
                        tileX = (j*((self.game.DISPLAY_W-2*border)/mapX))+border
                        tileY = (i*((self.game.DISPLAY_W-2*border)/mapX))+border
                    pygame.draw.rect(self.game.window, self.game.BLUE, (tileX, tileY, tileSize, tileSize))
                elif(mapNum[i*mapX+j]==3):
                    if xGreaterThanY:
                        tileX = (j*((self.game.DISPLAY_H-2*border)/mapY))+border
                        tileY = (i*((self.game.DISPLAY_H-2*border)/mapY))+border
                    else:
                        tileX = (j*((self.game.DISPLAY_W-2*border)/mapX))+border
                        tileY = (i*((self.game.DISPLAY_W-2*border)/mapX))+border
                    pygame.draw.rect(self.game.window, self.game.LBLUE, (tileX, tileY, tileSize, tileSize))
                elif(mapNum[i*mapX+j]==4):
                    if xGreaterThanY:
                        tileX = (j*((self.game.DISPLAY_H-2*border)/mapY))+border
                        tileY = (i*((self.game.DISPLAY_H-2*border)/mapY))+border
                    else:
                        tileX = (j*((self.game.DISPLAY_W-2*border)/mapX))+border
                        tileY = (i*((self.game.DISPLAY_W-2*border)/mapX))+border
                    pygame.draw.rect(self.game.window, self.game.BLACK, (tileX, tileY, tileSize, tileSize))

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.resetKeys()

    def checkInput(self):
        if self.game.ESC_KEY:
            self.game.playing = False
        self.run_display = False
