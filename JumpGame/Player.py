import Shared
import pygame
import os

def BlockWall():
    if Shared.positionCharacterX > 570:
        Shared.positionCharacterX = 570
    elif Shared.positionCharacterX < -14:
        Shared.positionCharacterX = -14

def Jump():
    if Shared.positionCharacterY < Shared.heightJump and Shared.moveCharacterY == Shared.speedCharacterY: #Avoid double jump.
        Shared.moveCharacterY = -Shared.speedCharacterY
        Shared.character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
    elif Shared.positionCharacterY > 351 and Shared.moveCharacterY == -Shared.speedCharacterY: #Make the character going down after the jump.
        Shared.moveCharacterY = 0
        Shared.character = pygame.image.load(os.path.join('Images', 'characterStand.png'))

def MoveCharacter():
    Shared.positionCharacterX -= Shared.moveCharacterX * Shared.dt#Make the character move left and right.
    Shared.positionCharacterY -= Shared.moveCharacterY * Shared.dt #Make the character jump.

def AvoidPositionXBug():
    if Shared.positionCharacterY > 351:
        Shared.moveCharacterY = 0
        Shared.character = pygame.image.load(os.path.join('Images', 'characterStand.png'))
        Shared.positionCharacterY = 351

if __name__ == '__main__':
    print("You must use the module Game.py as Main.")