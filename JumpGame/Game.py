from sys import exit
from Player import *
from Vehicle import *
from GameOver import *
from Level import *
import pygame


pygame.init()
font = pygame.font.SysFont("calibri", 40)
key = pygame.key.get_pressed()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("JumpGame")

back = pygame.Surface((640,480))
background = back.convert()
background.fill(Shared.WHITE)
backgroundImage = pygame.image.load(os.path.join('Images', 'backgroundImage.png')).convert_alpha()
clock = pygame.time.Clock()

while Shared.inGame:
    Shared.dt = clock.tick(60)
    scoreText = font.render("Score : ", True, (Shared.GREEN)) #Display of the score.
    scoreTextLevel = font.render("Level : ", True, (Shared.GREEN))  # Display of the score.
    score1 = font.render(str(Shared.score), True, (Shared.GREEN)) #Display of the score.
    score2 = font.render(str(Shared.level), True, (Shared.GREEN))  # Display of the score.

    screen.blit(backgroundImage, (0, 0))
    screen.blit(scoreText, (5, 5))
    screen.blit(scoreTextLevel, (5, 50))
    screen.blit(score2, (130, 50))
    screen.blit(score1, (130, 8))
    screen.blit(Shared.car, (Shared.positionCarX, 351))
    screen.blit(Shared.character, (Shared.positionCharacterX, Shared.positionCharacterY))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if Shared.positionCharacterY >= 350 and Shared.positionCharacterY < 359:
                    CheckLevel()
                    Shared.character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
                    Shared.moveCharacterY = Shared.speedCharacterY
            if event.key == K_LEFT:
                Shared.moveCharacterX = Shared.speedCharacterX
            if event.key == K_RIGHT:
                Shared.moveCharacterX = -Shared.speedCharacterX
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                Shared.moveCharacterX = 0
            if event.key == K_RIGHT:
                Shared.moveCharacterX = 0

    BlockWall()
    Jump()
    AvoidPositionXBug()
    MoveCharacter()
    MoveCar()
    CheckUpCrash()
    SpeedLevel()
    SoundLevel()

    if Shared.trafic == "right":
        ModelCarRight()
    else:
        ModelCarLeft()

    pygame.display.update()


if __name__ != '__main__':
    print("You must start me as the main module.")