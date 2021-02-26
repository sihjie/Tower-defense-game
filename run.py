import pygame

if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((1350, 700))
    helpmenu = pygame.display.set_mode((1350, 700))
    helpmenu2 = pygame.display.set_mode((1350, 700))
    pygame.display.set_caption('沙漠保衛戰')
    from main_menu.main_menu import MainMenu
    mainMenu = MainMenu(win, helpmenu)
    mainMenu.run()