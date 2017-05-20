import pygame
from pygame.locals import *
screen = pygame.display.set_mode((640,480),0,32)

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