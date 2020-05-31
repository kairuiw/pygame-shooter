import pygame
import random
from random import seed
from random import randint
from os import path

gs = path.join(path.dirname(__file__),'gs stuff')

WIDTH = 580
HEIGHT = 280
FPS = 60

color1 = 60,179,113
color2 = 220,20,60
color3 = 65,105,225
color4 = 255, 255, 255

font_name = pygame.font.match_font('arial')

def draw(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_sur = font.render(text, True, color4)
    text_rec = text_sur.get_rect()
    text_rec.midtop = (x, y)
    surf.blit(text_sur, text_rec)

class me(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player, (50,25))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, color1, self.rect.center, self.radius)        
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

seed(1)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.picnumber = randint(0, 3)
        self.image_orig = UFOS[self.picnumber]
        self.image_orig.set_colorkey((0, 0, 0))
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = 10
        # pygame.draw.circle(self.image, color2, self.rect.center, self.radius)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)
        self.rect.x = random.randrange(540+50, 540+100)
        self.speedx = random.randrange(1, 5)
        self.speedy = random.randrange(-2, 2)
        self.turn = 0
        self.turn_speed = random.randrange(-7, 7)
        self.lastup = pygame.time.get_ticks()

    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.lastup > 75:
            self.lastup = now
            self.turn = (self.turn + self.turn_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.turn)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x -= self.speedx
        if self.rect.x < 10:
            self.rect.x = random.randrange(540+50, 540+100)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx = random.randrange(1, 5)
            self.speedy = random.randrange(-2, 2)
        self.rect.y -= self.speedy
        if self.rect.y > HEIGHT:
            self.rect.x = random.randrange(540+50, 540+100)
            self.rect.y = random.randrange(HEIGHT - self.rect.height)
            self.speedx = random.randrange(1, 5)
            self.speedy = random.randrange(-2, 2)

class bullet(pygame.sprite.Sprite):
    def __init__(self, y, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(zap,(12, 4))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 5
        # pygame.draw.circle(self.image, color3, self.rect.center, self.radius)        
        self.rect.left = x
        self.rect.centery = y
        self.speedx = 8

    def update(self):
       self.rect.x += self.speedx
       if self.rect.right > WIDTH:
           self.kill()

background = pygame.image.load(path.join(gs, "darkPurple.png")).convert()
background_rect = background.get_rect()
player = pygame.image.load(path.join(gs, "playerShip2_bluehorizontal.png")).convert() 
zap = pygame.image.load(path.join(gs, "laserRed03hor.png")).convert()
UFOS = []
ufo_list = ['ufoBlue.png', 'ufoGreen.png', 'ufoRed.png', 'ufoYellow.png']
for img in ufo_list:
    imgs = pygame.image.load(path.join(gs, img)).convert()
    UFOS.append(pygame.transform.scale(imgs,(25, 25)))

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
        if m.picnumber == 0:
            points += 1
            print("good")
        if m.picnumber == 1:
            points += 2
            print("nice!")
        if m.picnumber == 3:
            points += 5
            print("extreme!!!")
        if m.picnumber == 2:
            points += 10
            print("mastery!!! !!")

        all_sprites.add(m)
        Mobs.add(m)
        points = points + 1

    boom = pygame.sprite.spritecollide(player, Mobs, False)
    if boom:
        running = False 
        print("points:" , points)
    
    surfacekairui.fill((60, 179, 113))
    back = pygame.transform.scale(background, (WIDTH,HEIGHT))
    surfacekairui.blit(back, background_rect)
    all_sprites.draw(surfacekairui)
    draw(surfacekairui, str(points), 20, WIDTH / 2, 5)
    pygame.display.flip()

pygame.quit()