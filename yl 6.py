import pygame

# pygame setup
pygame.init()
screenX = 640
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True
# kiirus v midagi
posX, posY = 0, 0
padX, padY = 0, screenY / 1.5
padspeed = 2
speedX = 1
speedY = 4
direction = 0



# ait same piltid
ball_pild = pygame.image.load("img/ball.png")
pad_pild = pygame.image.load('img/pad.png')
ball = pygame.Rect(posX, posY, ball_pild.get_width(), ball_pild.get_height())
pad = pygame.Rect(padX, padY, pad_pild.get_width(), ball_pild.get_height())

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = "move_right"
            elif event.key == pygame.K_LEFT:
                direction = "move_left"
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("light blue")

    # RENDER YOUR GAME HERE


    ball = pygame.Rect(posX, posY, ball_pild.get_width(), ball_pild.get_height())
    pad = pygame.Rect(padX, padY, pad_pild.get_width(), ball_pild.get_height())
    screen.blit(ball_pild, ball)
    screen.blit(pad_pild, pad)
    if direction == "move_right":
        padspeed = 2
    elif direction == "move_left":
        padspeed = -2
    padX += padspeed
    posX += speedX
    posY += speedY
    if padX > screenX - pad.width:
        padspeed = speedX
   if padX < 0:
       



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()