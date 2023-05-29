import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")

    # RENDER YOUR GAME HERE
    bg = pygame.image.load("bg_shop.jpg")
    seller = pygame.image.load("seller.png")
    seller = pygame.transform.scale(seller, [200, 230])
    chat = pygame.image.load("chat.png")
    screen.blit(bg, [0, 0])
    screen.blit(seller, [50,220])
    screen.blit(chat, [200, 0])

    font = pygame.font.Font(pygame.font.match_font('arial'), 30)
    text = font.render("Hello ma kaspar", True, "white")

    text_width = text.get_rect().width
    text_height = text.get_rect().height

    screen.blit(text, [340 - text_width / 2, 100 - text_height / 2])
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()