import Shared
import pygame
from pygame.locals import *
import os

pygame.init()
font = pygame.font.SysFont("calibri", 40)
screen = pygame.display.set_mode((640,480),0,32)
font = pygame.font.SysFont("calibri", 40)
backgroundImage = pygame.image.load(os.path.join('Images', 'backgroundImage.png')).convert_alpha()
scoreText = font.render("Score : ", True, (Shared.GREEN))  # Display of the score.
scoreTextLevel = font.render("Level : ", True, (Shared.GREEN))  # Display of the score.

def CheckUpCrash():
    distance = Shared.positionCharacterX - Shared.positionCarX #Count the distance between the car and the character.
    if distance > -60 and distance < 117: #Check if the character got the same X as the car.
        if Shared.positionCharacterY > 300: #Check if the character was also at the same Y of the car.
            Shared.inGame = False #Stop the game.
            pygame.mixer.music.load(Shared.musicCrash)
            pygame.mixer.music.play()
            GameOver()

def GameOver():
    '''''If the player hit the car, this will change the image for a explosion and stop the game.'''''
    GameOverCheckUp = True
    score1 = font.render(str(Shared.score), True, (Shared.GREEN))  # Display of the score.
    score2 = font.render(str(Shared.level), True, (Shared.GREEN))  # Display of the score.
    while GameOverCheckUp:
        screen.blit(backgroundImage, (0, 0))
        screen.blit(scoreText, (5, 5))
        screen.blit(scoreTextLevel, (5, 50))
        screen.blit(score1, (130, 8))
        screen.blit(score2, (130, 50))
        screen.blit(Shared.explosion, (Shared.positionCharacterX, Shared.positionCharacterY))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

if __name__ == '__main__':
    print("You must use the module Game.py as Main.")