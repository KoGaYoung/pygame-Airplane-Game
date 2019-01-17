import pygame, sys
from tkinter import *
import os
from pygame.locals import *
from random import *

SCREEN_WIDTH = 600
SCREEN_HEIGHT= 600

root = tkinter.TK()
embed = tkinter.Frame(root,width=200, height=100)
embed.pack()
text = tkinter.Button(root, text='blah')
text.pack()

pygame.init()
pygame.display.set_caption('Main_Screen')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#프레임마다 몇 밀리세컨 걸렸는지 계산하는 시계
clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.x = 300
        self.y = 300
        self.image = pygame.image.load("image/plane.png").convert_alpha()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Ball(object):
    def __init__(bullet):
        bullet.x = randint(0, 600)
        bullet.y = randint(0, 600)
        bullet.image = pygame.image.load("image/ball.gif").convert_alpha()
        bullet.speedX = uniform(-3.0, 3.0)
        bullet.speedY = uniform(-3.0, 3.0)

    def draw(bullet):
        bullet.x = bullet.x + bullet.speedX
        bullet.y = bullet.y + bullet.speedY
        if(bullet.x >SCREEN_WIDTH or bullet.x <0.0) :
            bullet.speedX = bullet.speedX * -1
        if(bullet.y >SCREEN_HEIGHT or bullet.y<0.0) :
            bullet.speedY = bullet.speedY * -1
        screen.blit(bullet.image, (bullet.x,bullet.y))

def text_objects(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pause = False

def main():
    player = Player()
    numBall=5
    ballList = []
    for i in range(numBall):
        ballList.append(Ball())
    isDown = False
    saveKey =''
    score = 0

 # main game loop
    while True:
        elapsed = clock.tick(30)
        score += elapsed

        #키가 눌려있는지 아닌지 확인
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                isDown = True
                if event.key == K_a:
                    saveKey = 'a'
                elif event.key == K_d:
                    saveKey = 'd'
                elif event.key == K_w:
                    saveKey = 'w'
                elif event.key == K_s:
                    saveKey ='s'
            elif(event.type == KEYUP):
                isDown = False
            #키 눌려있을 경우 누르는 자판 저장


        if isDown == True:
            if (saveKey == 'a') :
                player.x = player.x - 5
            elif (saveKey == 'd') :
                player.x = player.x + 5
            elif (saveKey =='w') :
                player.y = player.y - 5
            elif (saveKey =='s') :
                player.y = player.y + 5;

            #게임종료
        if event.type == pygame.QUIT:
            sys.exit()

        button("Continue",150,450,100,50,(0,255,0),(0,255,0),unpause)
        button("Quit",550,450,100,50,(200,0,0),(225,0,0),quitgame)

        #화면 초기화
        screen.fill((0,0,0))
        player.draw()
        for i in range(numBall):
            ballList[i].draw()
        text = str(score)
        label = pygame.font.Font(None, 64).render(text, 1, (0, 0, 250))
        screen.blit(label, (100, 100))
        pygame.display.update()

if __name__ == "__main__":
    main()
