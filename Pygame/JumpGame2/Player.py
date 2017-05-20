import pygame
import os


class Player:
    positionCharacterX = 280  # Starting position X of the character.
    positionCharacterY = 351  # Starting position Y of the character.
    speedCharacter = 250  # Movement speed of the character.
    moveCharacterY = 0  # Speed when jumping.
    moveCharacterX = 0  # Speed when moving left or right.
    heightJump = 150  # Height that the character gonna jump.
    character = pygame.image.load(os.path.join('Images', 'characterStand.png'))
    screen = pygame.display.set_mode((640, 480), 0, 32)

    def _init_(self, name):
        self.name = name
        self.screen.blit(self.character, (self.positionCharacterX, self.positionCharacterY))

    def JumpCharacter(self):
        if self.positionCharacterY < self.heightJump and self.moveCharacterY == 0.20:  # Avoid double jump.
            self.moveCharacterY = -0.20
            self.character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
        elif self.positionCharacterY > 351 and self.moveCharacterY == -0.20:  # Make the character going down after the jump.
            self.moveCharacterY = 0
            self.character = pygame.image.load(os.path.join('Images', 'characterStand.png'))

    def AvoidCharacterOutScreen(self):
        if self.positionCharacterX > 570:
            self.positionCharacterX = 570
        elif self.positionCharacterX < -14:
            self.positionCharacterX = -14

    def CharacterMoveLeftRight(self):
        self.positionCharacterX -= self.moveCharacterX  # Make the character move left and right.
        self.positionCharacterY -= self.moveCharacterY  # Make the character jump.