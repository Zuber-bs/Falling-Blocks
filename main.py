import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
playerX, playerY = 370, 480
playerWidth, playerHeight = 50, 50
playerVel = 0
score = 0
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 40)
font_score = pygame.font.SysFont("comicsansms", 15)
text = font.render("GAME OVER MAN/WOMAN!!", True, (255, 255, 255))

def Person(x, y):
    screen.blit(person, (x, y))

numOfEnemies = 6
enemies = []
enemyWidth = []
enemyHeight = []
enemyX = []
enemyY = []
enemyVel = []

for i in range(numOfEnemies):
    enemyWidth.append(50)
    enemyHeight.append(50)
    enemyX.append(random.randint(0, 750))
    enemyY.append(random.randint(0, 400))
    enemyVel.append(1)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blocks Droping")
icon = pygame.image.load("cloudy.png")
pygame.display.set_icon(icon)
background = pygame.image.load("Background.jpg")

running = True
while running:

    screen.fill(BLACK)
    screen.blit(background, (0, 0))
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerVel = -5

            if event.key == pygame.K_RIGHT:
                playerVel = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerVel = 0

    if playerX > 750:
        playerX = 750

    if playerX < 0:
        playerX = 0



    for i in range(numOfEnemies):
        if enemyY[i] > 600:
            enemyY[i] = 50
            enemyX[i] = random.randint(0, WIDTH-enemyWidth[i])

        enemyY[i] += enemyVel[i]
        pygame.draw.rect(screen, RED, (enemyX[i], enemyY[i], enemyWidth[i], enemyHeight[i]))

        if playerX < enemyX[i] + enemyWidth[i] and \
                playerX + playerWidth > enemyX[i] and \
                playerY < enemyY[i] + enemyHeight[i] and \
                playerY + playerHeight > enemyY[i]:
            screen.fill(BLACK)
            screen.blit(text, (120, 200))
            running = False
            print("Score: {0}".format(score))

        if enemyY[i] > 600:
            score += 1

        if score > 10:
            enemyVel[i] = 2

        if score > 20:
            enemyVel[i] = 5

        if score > 30:
            enemyVel[i] = 10

        if score > 50:
            enemyVel[i] = 20

    text_score = font_score.render("Score: {0}".format(score), True, (255, 255, 255))
    playerX += playerVel
    screen.blit(text_score, (100, 50))
    pygame.draw.rect(screen, (BLUE), (playerX, playerY, playerWidth, playerHeight))
    pygame.display.flip()