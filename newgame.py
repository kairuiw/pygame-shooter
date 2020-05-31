import pygame
import random

WIDTH = 580
HEIGHT = 280
FPS = 60

class me(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,25))
        self.image.fill((25, 25, 112))
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.speedy = 0

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom >HEIGHT:
            self.rect.bottom = HEIGHT

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,12))
        self.image.fill((220, 30, 60))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.rect.x = random.randrange(540+50, 540+100)
        self.speedx = random.randrange(1, 5)

    def update(self):
        self.rect.x -= self.speedx
        if self.rect.x < 10:
            self.rect.x = random.randrange(540+50, 540+100)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx = random.randrange(1,5)

all_sprites = pygame.sprite.Group()
Mobs = pygame.sprite.Group()
player = me()
all_sprites.add(player)
for i in range(5):
    m = Mob()
    all_sprites.add(m)
    Mobs.add(m)

running = True
while running:
    clock.tick (FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.init()
pygame.mixer.init()
pygamekairui = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")
clocks = lock = pygame.time.Clock()

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

    all_sprites.draw(pygamekairui)
    pygame.display.flip()

pygame.quit()
pygame.display.flip()

pygame.quit()
   