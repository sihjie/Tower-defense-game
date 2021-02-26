import pygame
import os

back_img = pygame.image.load(os.path.join("game_assets", "back.png")).convert_alpha()

class Help2:
    def __init__ (self, helpmenu):
        self.width = 1350
        self.height = 700
        self.helpmenu = helpmenu
        self.bg = pygame.image.load(os.path.join("game_assets", "helpbg3.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
       
        self.btn = (130, 290, back_img.get_width(), back_img.get_height())

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

                    
            self.draw()



    def draw(self):
        self.helpmenu.blit(self.bg, (0,0))
        self.helpmenu.blit(back_img, (self.btn[0], self.btn[1]))
        pygame.display.update()