import pygame
from menu import *
from level import *

class Game():

    def __init__(self, mapArray):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.ESC_KEY = False
        self.DISPLAY_W, self.DISPLAY_H = 1024, 1024
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = "freesansbold.ttf"
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.GREY = (50,50,50)
        self.LGREEN, self.DGREEN = (0,255,0), (0,110,0)
        self.BLUE, self.LBLUE = (0,0,255), (53,81,94)
        self.RED = (255,0,0)
        self.YELLOW = (255,255,0)
        self.mapData = mapArray
        self.pause_menu = PauseMenu(self)
        self.curr_menu = self.pause_menu
        self.curr_level = Level(self, self.mapData)

    def gameLoop(self):
        while self.playing:
            self.checkEvents()
            if self.START_KEY:
                self.playing = False
            self.display.fill(self.BLACK)
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()

    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if event.key == pygame.K_ESCAPE:
                    self.ESC_KEY = True

    def resetKeys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
