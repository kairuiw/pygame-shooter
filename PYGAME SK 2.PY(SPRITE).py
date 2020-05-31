import pygame
import random
import os

WIDTH = 580
HEIGHT = 280
FPS = 30

game_folder = os.path.dirname (__file__)
img_folder = os.path.join(game_folder, "TUTORIAL.TEACHERSTUFF")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite .Sprite. __init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        #self.rect.left = 20
        #self.rect.top = 20
        self.y_speed = 5
        self.x_speed = 5
        
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.left > WIDTH - 60:
            #self.x_speed = - 5
            self.rect.x = 0
            
       # if self.rect.left < 0:
          #  self.x_speed = +5
          #  print (self.x_speed)
        if self.rect.top > 100:
            self.y_speed = - 5
        if self.rect.top < 50:
            self.y_speed = 5
            
pygame.init()
pygame.mixer.init()
pygamekairui = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("kairui games")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
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
