# Example file showing a basic pygame "game loop"

import pygame, random
score = 0
# pygame setup
pygame.init()
screenX = 640
screenY = 480
screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True
bg = pygame.image.load("img/bg_rally.jpg")
blue_car = pygame.image.load("img/f1_blue.png")
red_car = pygame.image.load("img/f1_red.png")

track_left = 145
track_right = 495 - blue_car.get_rect().width

coords = []
for _ in range(3):
    coords.append([random.randint(track_left, track_right), random.randint(-100, -10)])





while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit(bg,[0,0])
    screen.blit(red_car, (screenX/2 - red_car.get_rect().width / 2,screenY -red_car.get_rect().height))
    player = pygame.Rect(red_car, (screenX / 2 - red_car.get_rect().width / 2, screenY - red_car.get_rect().height))


    for i in range(len(coords)):
        screen.blit(blue_car, (coords[i][0], coords[i][1]))
        coords[i][1] += 1
        # kui jõuab alla, siis muudame ruduu alguspunkti
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(track_left, track_right)
            score += 1

            font = pygame.font.Font(pygame.font.match_font('ariel'), 30)
            text = font.render(f"Score: {score}", True, [20,20,20])
            screen.blit(text, (0, 0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()