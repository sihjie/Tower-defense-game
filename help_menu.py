import pygame
import os
from help_menu2 import Help2


back_img = pygame.image.load(os.path.join("game_assets", "back.png")).convert_alpha()
next_img = pygame.image.load(os.path.join("game_assets", "next.png")).convert_alpha()

class Help:
    def __init__ (self, helpmenu):
        self.width = 1350
        self.height = 700
        self.helpmenu = helpmenu
        self.bg = pygame.image.load(os.path.join("game_assets", "helpbg2.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
       
        self.btn = (130, 290, back_img.get_width(), back_img.get_height())
        self.btn2 = (1090, 290, next_img.get_width(), next_img.get_height())

    def run(self):
        run = True
        while run:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:

                    x, y = pygame.mouse.get_pos()

                    # check if hit back btn
                    if self.btn[0] <= x <= self.btn[0] + self.btn[2]:
                        if self.btn[1] <= y <= self.btn[1] + self.btn[3]:
                            run = False

                    # check if hit next botton
                    if self.btn2[0] <= x <= self.btn2[0] + self.btn2[2]:
                        if self.btn2[1] <= y <= self.btn2[1] + self.btn2[3]:
                            Helpmenu2 = Help2(self.helpmenu)
                            Helpmenu2.run()
                            del Helpmenu2
                    
            self.draw()



    def draw(self):
        self.helpmenu.blit(self.bg, (0,0))
        self.helpmenu.blit(back_img, (self.btn[0], self.btn[1]))
        self.helpmenu.blit(next_img, (self.btn2[0], self.btn2[1]))
        pygame.display.update()