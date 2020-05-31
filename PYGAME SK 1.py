import pygame
import random

WIDTH = 580
HEIGHT = 280
FPS = 30

pygame.init()
pygame.mixer.init()
pygamekairui = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("kairui games")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
running = True
while running:
    clock.tick (FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    pygamekairui.fill((0, 255, 0))
    all_sprites.draw(pygamekairui)
    pygame.display.flip()

pygame.quit()
   
