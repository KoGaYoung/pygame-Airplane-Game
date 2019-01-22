import pygame

class Player(object):
    def __init__(self):
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("image/plane.png").convert_alpha()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))
