import pygame
import os
pygame.init()

pygame.font.init()

fontsPath = os.path.join("fonts","COMIC.TTF")

font = pygame.font.Font(fontsPath,32)

text = font.render("Hello World",True,(255,255,0))

textRect = text.get_rect()

textRect.center = (400,300)

window = pygame.display.set_mode((800,600))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    window.blit(text,textRect)

    pygame.display.flip()

pygame.quit()