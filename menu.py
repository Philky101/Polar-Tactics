import pygame

class Menu():
    
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0,0,20,20)
        self.offset = -100

    def drawCursor(self):
        self.game.drawText("*", 35, self.cursor_rect.x - 100, self.cursor_rect.y + 10)

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.resetKeys()

class PauseMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Continue"
        self.contx, self.conty = self.mid_w, (self.mid_h - self.mid_h / 4)
        self.settx, self.setty = self.mid_w, self.mid_h
        self.exitx, self.exity = self.mid_w, (self.mid_h + self.mid_h / 4)
        self.cursor_rect.midtop = (self.contx, self.conty)

    def displayMenu(self):
        self.run_display = True
        while self.run_display:
            self.game.checkEvents()
            self.checkInput()
            self.game.display.fill(self.game.BLACK)
            self.game.drawText("Continue", 40, self.contx, self.conty)
            self.game.drawText("Settings", 40, self.settx, self.setty)
            self.game.drawText("Quit", 40, self.exitx, self.exity)
            self.drawCursor()
            self.blitScreen()

    def moveCursor(self):
        if self.game.DOWN_KEY:
            if self.state == "Continue":
                self.cursor_rect.midtop = (self.settx, self.setty)
                self.state = "Settings"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.exitx, self.exity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.contx, self.conty)
                self.state = "Continue"
        elif self.game.UP_KEY:
            if self.state == "Continue":
                self.cursor_rect.midtop = (self.exitx, self.exity)
                self.state = "Quit"
            elif self.state == "Quit":
                self.cursor_rect.midtop = (self.settx, self.setty)
                self.state = "Settings"
            elif self.state == "Settings":
                self.cursor_rect.midtop = (self.contx, self.conty)
                self.state = "Continue"

    def checkInput(self):
        self.moveCursor()
        if self.game.START_KEY:
            if self.state == "Continue":
                self.game.playing = True
            elif self.state == "Settings":
                self.game.playing = True
            elif self.state == "Quit":
                self.game.playing = False
            self.run_display = False
