from pygame.locals import *
from sys import exit
from Player import *
from Car import *
from GameOver import *

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

score = 0 #Score ingame.
musicCrash = os.path.join('Musics', 'carCrash.mp3')
musicWin100 = os.path.join('Musics', 'win100.mp3')

pygame.init()
font = pygame.font.SysFont("calibri", 40)
key = pygame.key.get_pressed()
screen = pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("JumpGame")

back = pygame.Surface((640,480))
background = back.convert()
background.fill(WHITE)
character = pygame.image.load(os.path.join('Images', 'characterStand.png'))
car = pygame.image.load(os.path.join('Images', 'car.png'))
explosion = pygame.image.load(os.path.join('Images', 'explosion.png'))
backgroundImage = pygame.image.load(os.path.join('Images', 'backgroundImage.png')).convert_alpha()
inGame = True
scoreSound = True

while inGame:
    scoreText = font.render("Score : ", True, (GREEN)) #Display of the score.
    score1 = font.render(str(score), True, (GREEN)) #Display of the score.
    distance = Player.positionCharacterX - Car.positionCarX #Count the distance between the car and the character.
    if distance > -60 and distance < 117: #Check if the character got the same X as the car.
        if Player.positionCharacterY > 300: #Check if the character was also at the same Y of the car.
            inGame = False #Stop the game.
            pygame.mixer.music.load(musicCrash)
            pygame.mixer.music.play()
            GameOver(Player.positionCharacterX,Player.positionCharacterY, explosion, backgroundImage, scoreText, score1)

    screen.blit(backgroundImage, (0, 0))
    screen.blit(scoreText, (5, 5))
    screen.blit(score1, (130, 8))
    screen.blit(car, (Car.positionCarX, 351))
    screen.blit(character, (Player.positionCharacterX, Player.positionCharacterY))

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if Player.positionCharacterY == 351 or Player.positionCharacterY == 351.2:
                    character = pygame.image.load(os.path.join('Images', 'characterJump.png'))
                    moveCharacterY = 0.20
            if event.key == K_LEFT:
                    moveCharacterX = 0.2
            if event.key == K_RIGHT:
                    moveCharacterX = -0.2
        elif event.type == KEYUP:
            if event.key == K_LEFT:
                moveCharacterX = 0
            if event.key == K_RIGHT:
                moveCharacterX = 0

    if scoreSound and score >= 100: #Play a little song when the player hit the 100 scores.
        scoreSound = False
        pygame.mixer.music.load(musicWin100)
        pygame.mixer.music.play()

    pygame.display.update()