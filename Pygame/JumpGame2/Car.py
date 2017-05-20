import pygame
import os
import random

class Car:
    positionCarX = 700  # Starting position of the car.
    SpeedMoveCar = 0  # Movement speed of the car.
    tabSpeed = [0.1, 0.2, 0.3, 0.4, 0.5]  # Different speeding for the car.
    model = 1  # Speeding the car must use in tabSpeed.
    car = pygame.image.load(os.path.join('Images', 'car.png'))

    def _init_(self, name):
        self.name = name

    def RandomSpeedCar(self):
        if self.model == 1:
            if self.positionCarX == 700:
                self.SpeedMoveCar = self.tabSpeed[0]
            if self.positionCarX < -200:
                self.SpeedMoveCar = 0
                self.positionCarX = 700
                self.score = self.score + 1
                self.model = random.randint(1, 5)
        elif self.model == 2:
            if self.positionCarX == 700:
                self.SpeedMoveCar = self.tabSpeed[1]
            if self.positionCarX < -200:
                self.SpeedMoveCar = 0
                self.positionCarX = 700
                self.score = self.score + 2
                self.model = random.randint(1, 5)
        elif self.model == 3:
            if self.positionCarX == 700:
                self.SpeedMoveCar = self.tabSpeed[2]
            if self.positionCarX < -200:
                self.SpeedMoveCar = 0
                self.positionCarX = 700
                self.score = self.score + 3
                self.model = random.randint(1, 5)
        elif self.model == 4:
            if self.positionCarX == 700:
                self.SpeedMoveCar = self.tabSpeed[3]
            if self.positionCarX < -200:
                self.SpeedMoveCar = 0
                self.positionCarX = 700
                self.score = self.score + 4
                self.model = random.randint(1, 5)
        elif self.model == 5:
            if self.positionCarX == 700:
                self.SpeedMoveCar = self.tabSpeed[4]
            if self.positionCarX < -200:
                self.SpeedMoveCar = 0
                self.positionCarX = 700
                self.score = self.score + 5
                self.model = random.randint(1, 5)

    def CarMove(self):
        self.positionCarX -= self.SpeedMoveCar  # Make the car move left.
