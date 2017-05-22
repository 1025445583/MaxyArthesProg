import Shared
import pygame

def CheckLevel():
    if Shared.score < 15:
        Shared.level = 1
    elif Shared.score >= 15 and Shared.score < 50:
        Shared.level = 2
        Shared.speedCharacterX = 0.3
        Shared.speedCharacterY = 0.3
    elif Shared.score >= 51 and Shared.score < 150:
        Shared.level = 3
        Shared.speedCharacterX = 0.4
        Shared.speedCharacterY = 0.4
    elif Shared.score >= 151 and Shared.score < 251:
        Shared.level = 4
        Shared.trafic = "left"
        Shared.speedCharacterX = 0.4
        Shared.speedCharacterY = 0.4
    else:
        Shared.level = 5
        Shared.speedCharacterX = 0.4
        Shared.speedCharacterY = 0.4


def SpeedLevel():
    if Shared.level == 1:
        Shared.tabSpeed = [0.1, 0.2, 0.3, 0.4, 0.5]
    elif Shared.level == 2:
        Shared.tabSpeed = [0.3, 0.4, 0.5, 0.5, 0.5]
    elif Shared.level == 3:
        Shared.tabSpeed = [0.4, 0.5, 0.6, 0.6, 0.6]
    else:
        Shared.tabSpeed = [0.6, 0.6, 0.7, 0.7, 0.7]

def SoundLevel():   #Play a little song when the player pass a level.
    if Shared.level == 2 and Shared.levelSound2:
        Shared.levelSound2 = False
        pygame.mixer.music.load(Shared.musicWin100)
        pygame.mixer.music.play()
    elif Shared.level == 3 and Shared.levelSound3:
        Shared.levelSound3 = False
        pygame.mixer.music.load(Shared.musicWin100)
        pygame.mixer.music.play()
    elif Shared.level == 4 and Shared.levelSound4:
        Shared.levelSound4 = False
        pygame.mixer.music.load(Shared.musicWin100)
        pygame.mixer.music.play()
    elif Shared.level == 5 and Shared.levelSound5:
        Shared.levelSound5 = False
        pygame.mixer.music.load(Shared.musicWin100)
        pygame.mixer.music.play()


if __name__ == '__main__':
    print("You must use the module Game.py as Main.")