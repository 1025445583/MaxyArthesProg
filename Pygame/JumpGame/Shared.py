import pygame
import os
'''''Character'''''
positionCharacterX = 280 #Starting position X of the character.
positionCharacterY = 351 #Starting position Y of the character.
moveCharacterY = 0
moveCharacterX = 0
speedCharacterX = 0.2 #Speed when moving left or right.
speedCharacterY = 0.2 #Speed when jumping.
heightJump = 150 #Height that the character gonna jump.
'''''Car'''''
positionCarX = 700 #Starting position of the car.
SpeedMoveCar = 0 #Movement speed of the car.
tabSpeed = [0.1, 0.2, 0.3, 0.4, 0.5] #Different speeding for the car.
model = 1 #Speeding the car must use in tabSpeed.
'''''Color'''''
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
'''''Sounds'''''
musicCrash = os.path.join('Musics', 'carCrash.mp3')
musicWin100 = os.path.join('Musics', 'win100.mp3')
'''''Images'''''
character = pygame.image.load(os.path.join('Images', 'characterStand.png'))
car = pygame.image.load(os.path.join('Images', 'car.png'))
explosion = pygame.image.load(os.path.join('Images', 'explosion.png'))
'''''Score'''''
score = 0 #Score ingame.
level = 1
'''''Boolean'''''
inGame = True


if __name__ == '__main__':
    print("You must use the module Game.py as Main.")