import pygame, random
pygame.init()

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("mäng")
screen.fill("purple")
clock = pygame.time.Clock()
bg = pygame.image.load("img/snake game bg.png")
playerimg = pygame.image.load("img/snuke.png")
playerimg = pygame.transform.scale(playerimg, [60, 73])  # Scale the player image to the desired size
font = pygame.font.Font(None, 36)

# koordinaadid ja kiirus
posX, posY = screenX / 2, screenY / 2
speedX, speedY = 2, 2
directionX, directionY = 0, 0
lastDirectionX, lastDirectionY = 0, 0  # Store the last valid direction
#enemy - tekitame 5 suvalist vaenlast
enemies = []
for i in range(5):
    enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))
enemyImage = pygame.image.load('img/apple for gmae.png')
enemyImage = pygame.transform.scale(enemyImage, [enemies[0].width, enemies[0].height])
gameover = False


enemyCounter = 0
totalEnemies = 60
score = 0
winning_score = 20

while not gameover:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True

            # klahvivajutus
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                lastDirectionX = directionX = "move_right"
            elif event.key == pygame.K_LEFT:
                lastDirectionX = directionX = "move_left"
            elif event.key == pygame.K_UP:
                lastDirectionY = directionY = "move_up"
            elif event.key == pygame.K_DOWN:
                lastDirectionY = directionY = "move_down"

        # klahvivajutuse vabastamine
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                directionX = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                directionY = 0

    # mängu piirjoonte tuvastamine
    if directionX == "move_left":
        if posX > 0:
            posX -= 3
    elif directionX == "move_right":
        if posX + 30 < screenX:
            posX += 3
    elif lastDirectionX == "move_left":  # Continue moving in the last valid direction
        if posX > 0:
            posX -= 3
    elif lastDirectionX == "move_right":
        if posX + 30 < screenX:
            posX += 3

    if directionY == "move_up":
        if posY > 0:
            posY -= 3
    elif directionY == "move_down":
        if posY + 30 < screenY:
            posY += 3
    elif lastDirectionY == "move_up":  # Continue moving in the last valid direction
        if posY > 0:
            posY -= 3
    elif lastDirectionY == "move_down":
        if posY + 30 < screenY:
            posY += 3

    # Check collision with screen boundaries
    if posX <= 0 or posX + 30 >= screenX or posY <= 0 or posY + 30 >= screenY:
        gameover = True

    screen.blit(bg, (0, -200))
    ruut = screen.blit(playerimg, [posX, posY, 30, 30])

    # enemy loomine
    enemyCounter += 1
    if enemyCounter >= totalEnemies:
        enemyCounter = 0
        enemies.append(pygame.Rect(random.randint(0, screenX - 100), random.randint(0, screenY - 100), 60, 73))

    for enemy in enemies[:]:
        if ruut.colliderect(enemy):
            enemies.remove(enemy)
            score += 1

    for enemy in enemies:
        screen.blit(enemyImage, enemy)
    print(score)
    score_text = font.render("Score: " + str(score), True, "Blue" )
    screen.blit(score_text, (10, 10))


    if score >= winning_score:
        win_text = font.render("You Win!", True, (0, 255, 0))
        screen.blit(win_text, (screenX // 2 - win_text.get_width() // 2, screenY // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting the game
        break

    if gameover:
        gameover_text = font.render("Game Over", True, (255, 0, 0))
        screen.blit(gameover_text,
                    (screenX // 2 - gameover_text.get_width() // 2, screenY // 2 - gameover_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Wait for 2 seconds before quitting the game
        break




    pygame.display.flip()

pygame.quit()