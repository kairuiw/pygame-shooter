# Pygame 
import pygame
import random

WIDTH = 535
HEIGHT = 269
FPS = 50

# initialise
pygame.init()
pygame.mixer .init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display .set_caption("GS AND GDDGCGVVH'S GAME")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = player()
all_sprites.add(player)
#game loop
running = True
while running:
    # Procces input (events)
    for event in pygame.event.get ():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # Draw / render
    screen.fill(( 0, 255, 0))
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

    
