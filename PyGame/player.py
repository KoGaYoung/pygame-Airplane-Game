import pygame, sys
from pygame.locals import *
from random import *


class Player(object):
    def __init__(self):
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("image/plane.png").convert_alpha()

    def draw(self,screen):
        screen.blit(self.image, (self.x, self.y))
