import Shared
import random

def MoveCar():
    Shared.positionCarX -= Shared.SpeedMoveCar  # Make the car move left.

def ModelCar():
    if Shared.model == 1:
        if Shared.positionCarX == 700:
            Shared.SpeedMoveCar = Shared.tabSpeed[0]
        if Shared.positionCarX < -200:
            Shared.SpeedMoveCar = 0
            Shared.positionCarX = 700
            Shared.score += 1
            Shared.model = random.randint(1, 5)
    elif Shared.model == 2:
        if Shared.positionCarX == 700:
            Shared.SpeedMoveCar = Shared.tabSpeed[1]
        if Shared.positionCarX < -200:
            Shared.SpeedMoveCar = 0
            Shared.positionCarX = 700
            Shared.score += 2
            Shared.model = random.randint(1, 5)
    elif Shared.model == 3:
        if Shared.positionCarX == 700:
            Shared.SpeedMoveCar = Shared.tabSpeed[2]
        if Shared.positionCarX < -200:
            Shared.SpeedMoveCar = 0
            Shared.positionCarX = 700
            Shared.score += 3
            Shared.model = random.randint(1, 5)
    elif Shared.model == 4:
        if Shared.positionCarX == 700:
            Shared.SpeedMoveCar = Shared.tabSpeed[3]
        if Shared.positionCarX < -200:
            Shared.SpeedMoveCar = 0
            Shared.positionCarX = 700
            Shared.score += 4
            Shared.model = random.randint(1, 5)
    elif Shared.model == 5:
        if Shared.positionCarX == 700:
            Shared.SpeedMoveCar = Shared.tabSpeed[4]
        if Shared.positionCarX < -200:
            Shared.SpeedMoveCar = 0
            Shared.positionCarX = 700
            Shared.score += 5
            Shared.model = random.randint(1, 5)

if __name__ == '__main__':
    print("You must use the module Game.py as Main.")