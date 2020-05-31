# Pygame 
import pygame
import random

WIDTH = 535
HEIGHT = 269
FPS = 50

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__ (self)
        self.image = pygame.Surface((50,50))
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
# initialise
pygame.init()
pygame.mixer .init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display .set_caption("GS AND GDDGCGVVH'S GAME")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
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

    
