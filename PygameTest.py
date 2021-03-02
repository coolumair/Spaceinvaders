import pygame
import random
import math

# this is needed
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('8717.jpg')

#Title and Icon
pygame.display.set_caption("Space Invader")

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 368
playerY = 480
#playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('monster.png'))
    enemyX.append((random.randint(0, 735)))
    enemyY.append(random.randint(50, 150))

enemyX_change = 0.25
enemyX_pos = 1
enemyY_change = 40

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = "ready"

def bullet(x, y):
    global bullet_state
    bullet_state = "Fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 27:
        return True
    else:
        return False

score_value = 0
score_goal = 15

font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)



def show_score(x,y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over():
    gameOver = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(gameOver, (200, 250))

#game loop 
running = True
while running:
    #background colour
    screen.fill((0, 0, 0))

    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if bullet_state == "ready":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet(playerX, bulletY)
                    bulletX = playerX
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.type == pygame.K_RIGHT or pygame.K_LEFT:
                playerX_change = 0
           """ 
        
        
    if pygame.key.get_pressed()[pygame.K_LEFT]:
            playerX -= 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
            playerX += 1
    
    #boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    #enemy movement
    
    for i in range(num_of_enemies):

        # GameOver
        if enemyY[i] > 480:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over()
            break
        if enemyX[i] <= 0:
            enemyX_pos = 1
            for j in range(num_of_enemies):
                enemyY[j] += enemyY_change
        elif enemyX[i] >= 736:
            enemyX_pos = -1
            for j in range(num_of_enemies):
                enemyY[j] += enemyY_change
    
        enemyX[i] += enemyX_change * enemyX_pos

        #collsion
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        
        enemy(enemyX[i], enemyY[i], i)

    

    #player
    #playerX += playerX_change

    #bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "Fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    
    # enemy speed
    if score_goal == score_value:
        enemyX_change += 0.1
        score_goal += 15

    
    

    player(playerX, playerY)

    show_score(textX, textY)
 


    pygame.display.update()
