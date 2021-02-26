import pygame
from .tower import Tower
import os
import math
import time



damage_imgs = [pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "10.png")).convert_alpha(), (90,90)),
              pygame.transform.scale(pygame.image.load(os.path.join("game_assets/support_towers", "9.png")).convert_alpha(), (90,90))]

money=0
class DamageTower(Tower):
    """
    add damage to surrounding towers
    """
    def __init__(self, x, y):
        super().__init__(x,y)
        self.range = 100
        self.tower_imgs = damage_imgs[:]
        self.archer_imgs = damage_imgs[:]
        self.effect = [0.5, 1]
        self.name = "damage"
        self.price = [2000]

    def support(self):
        """
        will modify towers according to ability
        :param towers: list
        :return: None
        """
        
        


        '''effected = []
        for tower in towers:
            x = tower.x
            y = tower.y

            dis = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)

            if dis <= self.range + tower.width/2:
                effected.append(tower)

        for tower in effected:
            tower.damage = tower.original_damage + round(tower.original_damage * self.effect[self.level -1])'''
        
