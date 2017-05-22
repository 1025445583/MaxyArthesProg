import Shared

def CheckLevel():
    if Shared.score < 15:
        Shared.level = 1
    elif Shared.score >= 15 and Shared.score < 50:
        Shared.level = 2
        Shared.speedCharacterX = 0.4
        Shared.speedCharacterY = 0.4
    else:
        Shared.level = 3
        Shared.speedCharacterX = 0.6
        Shared.speedCharacterY = 0.6

def SpeedLevel():
    if Shared.level == 1:
        Shared.tabSpeed = [0.1, 0.2, 0.3, 0.4, 0.5]
    elif Shared.level == 2:
        Shared.tabSpeed = [0.5, 0.6, 0.7, 0.8, 0.9]
    else:
        Shared.tabSpeed = [0.8, 0.9, 1.0, 1.1, 1.2]

if __name__ == '__main__':
    print("You must use the module Game.py as Main.")