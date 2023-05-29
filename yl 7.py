import pygame, random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
screen.fill("purple")
prev_click = pygame.mouse.get_pressed()
running = True
circle_size = 10
circles = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            # Vasaku kliki vabastamisel tekib ring juhuslikus värvitoonis
            mousePos = pygame.mouse.get_pos()
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            circle =  pygame.draw.circle(screen, color, mousePos, circle_size)
            circles.append(circle)
            for circle in circles:
                pygame.draw.circle(screen,circle[0], circle[1], circle[2])

        # RENDER YOUR GAME HERE


    pygame.display.flip()
    clock.tick(60)
pygame.quit()