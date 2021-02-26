from game import Game
from help_menu import Help
import pygame
import os

start_btn = pygame.image.load(os.path.join("game_assets", "start1.png")).convert_alpha()
help_btn = pygame.image.load(os.path.join("game_assets", "question.png")).convert_alpha()
logo = pygame.transform.scale(pygame.image.load(os.path.join("game_assets", "logo_2.png")).convert_alpha(), (900, 300))

class MainMenu:
    def __init__(self, win, helpmenu):
        self.width = 1350
        self.height = 700
        self.bg = pygame.image.load(os.path.join("game_assets", "main_bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.win = win
        self.helpmenu = helpmenu
        self.btn = (self.width/2 - start_btn.get_width()/2 - 100, 400, start_btn.get_width(), start_btn.get_height())
        self.btn2 = (self.width/2 - help_btn.get_width()/2 + 100, 400, help_btn.get_width(), help_btn.get_height())
    def run(self):
        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    
                    x, y = pygame.mouse.get_pos()

                    # check if hit start btn
                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            game = Game(self.win)
                            game.run()
                            del game

                    # check if hit question btn
                    if self.btn2[0] <= x <= self.btn2[0] + self.btn2[2]:
                        if self.btn2[1] <= y <= self.btn2[1] + self.btn2[3]:
                            Helpmenu = Help(self.helpmenu)
                            Helpmenu.run()
                            del Helpmenu
            self.draw()

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0,0))
        self.win.blit(logo, (self.width/2 - logo.get_width()/2, 0))
        self.win.blit(start_btn, (self.btn[0], self.btn[1]))
        self.win.blit(help_btn, (self.btn2[0], self.btn2[1]))#############################
        pygame.display.update()


