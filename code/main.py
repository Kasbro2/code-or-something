import math
import pygame
pygame.init()
while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = false
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("potato")
screen.fill([204, 255, 255])

pygame.draw.line(screen, [255,0,0], [0,0], [640,480], 2)
pygame.draw.rect(screen, [55,55,0],[50,50,200,200],2)
pygame.draw.circle(screen,"pink",[150,180],100,2)
pygame.draw.polygon(screen, "purple",[[260,80],[300,80],[300,100],[450,80],[550,200],[260,200]],2)
pygame.draw.ellipse(screen,"green",[50,200,200,100],2)
pygame.draw.arc(screen, [0,127,255],[10,10,140,135],0, math.pi * 1,5)
font= pygame.font.Font(pygame.font.match_font("arial"), 30)
font.set_underline(True)
text = font.render("tere kartul", True,[0,0,0])
text_width = text.get_rect().width
screen.blit(text, [200,200])

pygame.display.flip()