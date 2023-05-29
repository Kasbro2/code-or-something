import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True
def draw
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    screen_size = screen.get_size()


    for i in range(0, screen_size.width, 10):
        for j in range(0, screen_size.hight,10):
            pygame.draw.rect(screen, "red", [i,j,10,10], 1)


    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
