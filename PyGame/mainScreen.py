import pygame, sys
from pygame.locals import *
from random import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT= 300


pygame.init()
pygame.display.set_caption('Main_Screen')
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
#프레임마다 몇 밀리세컨 걸렸는지 계산하는 시계
clock = pygame.time.Clock()

class Player(object):
    def __init__(self):
        self.x = 150
        self.y = 150
        self.image = pygame.image.load("image/plane.png").convert_alpha()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Ball(object):
    def __init__(bullet):
        bullet.x = randint(0, 150)
        bullet.y = randint(0, 150)
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

def main():
    player = Player()
    numBall=5
    ballList = []
    for i in range(numBall):
        ballList.append(Ball())
    saveKey = [False, False, False, False]
    score = 0

 # main game loop
    while True:
        elapsed = clock.tick(30)
        #score += elapsed
        #print(ballList[1].x, ballList[1].y)
        #키가 눌려있는지 아닌지 확인
        for event in pygame.event.get():
            if(event.type == KEYDOWN):
                if event.key == K_a:
                    saveKey[0] = True
                if event.key == K_d:
                    saveKey[1] = True
                if event.key == K_w:
                    saveKey[2] = True
                if event.key == K_s:
                    saveKey[3] = True
            elif(event.type == KEYUP):
                if event.key == K_a:
                    saveKey[0] = False
                if event.key == K_d:
                    saveKey[1] = False
                if event.key == K_w:
                    saveKey[2] = False
                if event.key == K_s:
                    saveKey[3] = False
            #키 눌려있을 경우 누르는 자판 저장

        #눌린 키에 따라 비행기 이동
        # true IF condition ELSE false
        if (saveKey[0]) :
            player.x = player.x - 5 if player.x - 5 > 0 else player.x
        elif (saveKey[1]) :
            player.x = player.x + 5 if player.x + 5 < SCREEN_WIDTH else player.x
        if (saveKey[2]) :
            player.y = player.y - 5 if player.y - 5 > 0 else player.y
        elif (saveKey[3]) :
            player.y = player.y + 5 if player.y + 5 < SCREEN_HEIGHT else player.y;

        #게임종료
        if event.type == pygame.QUIT:
            sys.exit()

        #화면 초기화
        screen.fill((0,0,0))
        player.draw()
        for i in range(numBall):
            ballList[i].draw()
        #text = str(score)
        #label = pygame.font.Font(None, 64).render(text, 1, (0, 0, 250))
        #screen.blit(label, (100, 100))
        pygame.display.update()

if __name__ == "__main__":
    main()
