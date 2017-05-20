import pygame
from sys import exit
from pygame.locals import *
import os
import random


GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

positionCharacterX = 280 #Starting position X of the character.
positionCharacterY = 351 #Starting position Y of the character.
speedCharacter = 250 #Movement speed of the character.
moveCharacterY = 0 #Speed when jumping.
moveCharacterX = 0 #Speed when moving left or right.
heightJump = 150 #Height that the character gonna jump.
positionCarX = 700 #Starting position of the car.
SpeedMoveCar = 0 #Movement speed of the car.
score = 0 #Score ingame.
tabSpeed = [0.1, 0.2, 0.3, 0.4, 0.5] #Different speeding for the car.
model = 1 #Speeding the car must use in tabSpeed.
musicCrash = os.path.join('Musics', 'carCrash.mp3')
musicWin100 = os.path.join('Musics', 'win100.mp3')

pygame.init()
font = pygame.font.SysFont("calibri", 40)
key = pygame.key.get_pressed()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("JumpGame")

back = pygame.Surface((640,480))
background = back.convert()
background.fill(WHITE)
character = pygame.image.load(os.path.join('Images', 'characterStand.png'))
car = pygame.image.load(os.path.join('Images', 'car.png'))
explosion = pygame.image.load(os.path.join('Images', 'explosion.png'))
backgroundImage = pygame.image.load(os.path.join('Images', 'backgroundImage.png')).convert_alpha()
inGame = True
scoreSound = True

def GameOver(positionCharacterX,positionCharacterY, explosion, backgroundImage, scoreText, score1):
    '''''If the player hit the car, this will change the image for a explosion and stop the game.'''''
    GameOverCheckUp = True
    while GameOverCheckUp:
        screen.blit(backgroundImage, (0, 0))
        screen.blit(scoreText, (5, 5))
        screen.blit(score1, (130, 8))
        screen.blit(explosion, (positionCharacterX, positionCharacterY))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

while inGame:
    scoreText = font.render("Score : ", True, (GREEN)) #Display of the score.
    score1 = font.render(str(score), True, (GREEN)) #Display of the score.
    distance = positionCharacterX - positionCarX #Count the distance between the car and the character.
    if distance > -60 and distance < 117: #Check if the character got the same X as the car.
        if positionCharacterY > 300: #Check if the character was also at the same Y of the car.
            inGame = False #Stop the game.
            pygame.mixer.music.load(musicCrash)
            pygame.mixer.music.play()
            GameOver(positionCharacterX,positionCharacterY, explosion, backgroundImage, scoreText, score1)

    screen.blit(backgroundImage, (0, 0))
    screen.blit(scoreText, (5, 5))
    screen.blit(score1, (130, 8))
    screen.blit(car, (positionCarX, 351))
    screen.blit(character, (positionCharacterX, positionCharacterY))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if positionCharacterY == 351 or positionCharacterY == 351.2:
                    character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
                    moveCharacterY = 0.20
            if event.key == K_LEFT:
                    moveCharacterX = 0.2
            if event.key == K_RIGHT:
                    moveCharacterX = -0.2
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                moveCharacterX = 0
            if event.key == K_RIGHT:
                moveCharacterX = 0

    if positionCharacterX > 570:
        positionCharacterX = 570
    elif positionCharacterX < -14:
        positionCharacterX = -14

    if positionCharacterY < heightJump and moveCharacterY == 0.20: #Avoid double jump.
        moveCharacterY = -0.20
        character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
    elif positionCharacterY > 351 and moveCharacterY == -0.20: #Make the character going down after the jump.
        moveCharacterY = 0
        character = pygame.image.load(os.path.join('Images', 'characterStand.png'))

    positionCharacterX -= moveCharacterX #Make the character move left and right.
    positionCharacterY -= moveCharacterY #Make the character jump.
    positionCarX -= SpeedMoveCar #Make the char move left.

    if model == 1:
        if positionCarX == 700:
            SpeedMoveCar = tabSpeed[0]
        if positionCarX < -200:
            SpeedMoveCar = 0
            positionCarX = 700
            score = score + 1
            model = random.randint(1, 5)
    elif model == 2:
        if positionCarX == 700:
            SpeedMoveCar = tabSpeed[1]
        if positionCarX < -200:
            SpeedMoveCar = 0
            positionCarX = 700
            score = score + 2
            model = random.randint(1, 5)
    elif model == 3:
        if positionCarX == 700:
            SpeedMoveCar = tabSpeed[2]
        if positionCarX < -200:
            SpeedMoveCar = 0
            positionCarX = 700
            score = score + 3
            model = random.randint(1, 5)
    elif model == 4:
        if positionCarX == 700:
            SpeedMoveCar = tabSpeed[3]
        if positionCarX < -200:
            SpeedMoveCar = 0
            positionCarX = 700
            score = score + 4
            model = random.randint(1, 5)
    elif model == 5:
        if positionCarX == 700:
            SpeedMoveCar = tabSpeed[4]
        if positionCarX < -200:
            SpeedMoveCar = 0
            positionCarX = 700
            score = score + 5
            model = random.randint(1, 5)

    if scoreSound and score >= 100: #Play a little song when the player hit the 100 scores.
        scoreSound = False
        pygame.mixer.music.load(musicWin100)
        pygame.mixer.music.play()

    pygame.display.update()