import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (230, 255, 255), (250, 270), 60)
    pygame.draw.circle(screen, (225, 255, 255), (250, 180), 50)
    pygame.draw.circle(screen, (225, 255, 255), (250, 350), 70)

    pygame.draw.circle(screen, [0,0,0], [230,160], 10)
    pygame.draw.circle(screen, [0,0,0], [270,170], 10)

    pygame.draw.polygon(screen,[240, 100, 30], [(250,170),(250,180),(200,180)], width=0)

    pygame.display.flip()


pygame.quit()