import pygame, sys
from pygame.locals import *
from random import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT= 300

class Ball(object):
    def __init__(bullet):
        bullet.x = randint(0, 150)
        bullet.y = randint(0, 150)
        bullet.image = pygame.image.load("image/ball.gif").convert_alpha()
        bullet.speedX = uniform(-3.0, 3.0)
        bullet.speedY = uniform(-3.0, 3.0)

    def draw(bullet,screen):
        bullet.x = bullet.x + bullet.speedX
        bullet.y = bullet.y + bullet.speedY
        if(bullet.x >SCREEN_WIDTH or bullet.x <0.0) :
            bullet.speedX = bullet.speedX * -1
        if(bullet.y >SCREEN_HEIGHT or bullet.y<0.0) :
            bullet.speedY = bullet.speedY * -1
        screen.blit(bullet.image, (bullet.x,bullet.y))
