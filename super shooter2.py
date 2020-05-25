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

    def shoot(self):
        wreck = bullet(self.rect.centery, self.rect.right)
        all_sprites.add(wreck)
        bullets.add(wreck)
        
pygame.init()
pygame.mixer.init()
surfacekairui = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("kairui games shoot!")
clock = pygame.time.Clock()

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

class bullet(pygame.sprite.Sprite):
    def __init__(self, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((12, 6))
        self.image.fill((255,215,0))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.centery = y
        self.speedx = 8

    def update(self):
       self.rect.x += self.speedx
       if self.rect.right > WIDTH:
           self.kill()

all_sprites = pygame.sprite.Group()
Mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = me()
all_sprites.add(player)
for i in range(5):
    m = Mob()
    all_sprites.add(m)
    Mobs.add(m)
    
running = True
points = 0
while running:
    clock.tick (FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(Mobs, bullets, True, True)
   
    for hit in hits:
        m = Mob()
        all_sprites.add(m)
        Mobs.add(m)
        points = points + 1

    boom = pygame.sprite.spritecollide(player, Mobs, False)
    if boom:
        running = False 
        print("points:" , points)
    
    surfacekairui.fill((0, 255, 0))
    all_sprites.draw(surfacekairui)
    pygame.display.flip()

pygame.quit()