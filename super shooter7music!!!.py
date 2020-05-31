import pygame
import random
from random import seed
from random import randint
from os import path

gs = path.join(path.dirname(__file__),'gs stuff')
gs_mu = path.join(path.dirname(__file__),'gs music')

WIDTH = 580
HEIGHT = 280
FPS = 60
POWERUP_TIME = 10000

color1 = 60, 179, 113
color2 = 220, 20, 60
color3 = 65, 105, 225
color4 = 255, 127, 80
color5 = 148, 0, 211
color6 = 199, 21, 133

font_name = pygame.font.match_font('arial')

def draw(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_sur = font.render(text, True, color4)
    text_rec = text_sur.get_rect()
    text_rec.midtop = (x, y)
    surf.blit(text_sur, text_rec)

def spawnmob():
    m = Mob()
    all_sprites.add(m)
    Mobs.add(m)

def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    bar_length = 180
    bar_height = 20
    fill = (pct / 50) * bar_length
    out_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, fill, bar_height)
    pygame.draw.rect(surf, color5, fill_rect)
    pygame.draw.rect(surf, color6, out_rect, 2)

def draw_lives(surf, x, y, lives, img):
    for l in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x + 8 * l
        img_rect.y = y
        surf.blit(img, img_rect)

def show_dead_sc():
    draw(surfacekairui, 'SHOOT EM UP', 75, WIDTH / 2, HEIGHT / 4)
    draw(surfacekairui, 'use arrow keys to move, use space to fire. :)', 25, WIDTH / 2, HEIGHT / 2)
    draw(surfacekairui, 'press any key to start. :]', 12, WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.flip()
    wait = True
    while wait:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                wait = False

class me(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player, (50, 25))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, color1, self.rect.center, self.radius)        
        self.rect.centery = HEIGHT/2
        self.speedy = 0
        self.shield = 50
        self.shoot_delay = 200
        self.last_shot = pygame.time.get_ticks()
        self.lives = 5
        self.hid = False
        self.hid_time = pygame.time.get_ticks()
        self.powerlvl = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        if self.powerlvl >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.powerlvl -= 1
            self.power_time = pygame.time.get_ticks()

        if self.hid and pygame.time.get_ticks() - self.hid_time > 1200:
            self.hid = False
            self.rect.centery = HEIGHT / 2 
            self.rect.left = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            self.shoot()
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
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            self.last_shot = now
            if self.powerlvl == 1:
                Bullet = bullet(self.rect.centery, self.rect.right)
                all_sprites.add(Bullet)
                bullets.add(Bullet)
                shoots.play()
            if self.powerlvl >= 2:
                Bullet1 = bullet(self.rect.top, self.rect.centerx)
                Bullet2 = bullet(self.rect.bottom, self.rect.centerx)
                all_sprites.add(Bullet1)
                all_sprites.add(Bullet2)
                bullets.add(Bullet1)
                bullets.add(Bullet2)
                shoots.play()
            if self.powerlvl >= 3:
                Bullet21 = bullet(self.rect.centery, self.rect.right)
                Bullet22 = bullet(self.rect.bottom, self.rect.centerx)
                Bullet23 = bullet(self.rect.top, self.rect.centerx)
                all_sprites.add(Bullet21)
                all_sprites.add(Bullet22)
                all_sprites.add(Bullet23)
                bullets.add(Bullet21)
                bullets.add(Bullet22)
                bullets.add(Bullet23)
                shoots.play()
            
    def pow(self):
        self.powerlvl += 1
        self.power_time = pygame.time.get_ticks()
    
    def hide(self):
        self.hid = True
        self.hid_time = pygame.time.get_ticks()
        self.rect.center = (- 200, HEIGHT / 2 )
        
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

class exploder(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = ex_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.radius = 5
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(ex_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = ex_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

class powerup(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['sh', 'gu', 'la'])
        self.image = pow_imgs[self.type]
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedx = -3

    def update(self):
       self.rect.x += self.speedx
       if self.rect.right < 0:
           self.kill()


background = pygame.image.load(path.join(gs, "darkPurple.png")).convert()
background_rect = background.get_rect()
player = pygame.image.load(path.join(gs, "playerShip2_bluehorizontal.png")).convert()
mini_player = pygame.transform.scale(player,(20,10))
mini_player.set_colorkey((0, 0, 0)) 
zap = pygame.image.load(path.join(gs, "laserRed03hor.png")).convert()
UFOS = []
ufo_list = ['ufoBlue.png', 'ufoGreen.png', 'ufoYellow.png', 'ufoRed.png']
for img in ufo_list:
    imgs = pygame.image.load(path.join(gs, img)).convert()
    UFOS.append(pygame.transform.scale(imgs, (25, 25)))

ex_anim = {}
ex_anim['lg'] = []
ex_anim['sm'] = []
ex_anim['pl'] = []

for x in range(9):
    filenamer = 'regularExplosion0{}.png'.format(x)
    ex_imgs = pygame.image.load(path.join(gs, filenamer)).convert()
    ex_imgs.set_colorkey((0, 0, 0))
    ex_imgs_lg = pygame.transform.scale(ex_imgs, (50, 50))
    ex_anim['lg'].append(ex_imgs_lg)
    ex_imgs_sm = pygame.transform.scale(ex_imgs, (12, 12))
    ex_anim['sm'].append(ex_imgs_sm)
    filenames = 'sonicExplosion0{}.png'.format(x)
    ex_imgs2 = pygame.image.load(path.join(gs, filenames)).convert()
    ex_imgs2.set_colorkey((0, 0, 0))
    ex_anim['pl'].append(ex_imgs2)

pow_imgs = {}
pow_imgs['sh'] = pygame.image.load(path.join(gs, 'shield_gold.png')).convert()
pow_imgs['gu'] = pygame.image.load(path.join(gs, 'bolt_gold.png')).convert()
pow_imgs['la'] = pygame.image.load(path.join(gs, 'laser_gold.png')).convert()

shoots = pygame.mixer.Sound(path.join(gs_mu, 'Laser.wav'))
shoots.set_volume(.15)

explode = pygame.mixer.Sound(path.join(gs_mu, 'Explosion.wav'))
explode.set_volume(.15)

pygame.mixer.music.load(path.join(gs_mu, 'battleThemeA.MP3'))
pygame.mixer.music.set_volume(.05)

all_sprites = pygame.sprite.Group()
Mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
puss = pygame.sprite.Group()
player = me()
all_sprites.add(player)
for i in range(4):
    spawnmob()
points = 0
    
pygame.mixer.music.play(loops = -1)

dead_play = True   
running = True
points = 0
while running:
    if dead_play:
        show_dead_sc()
        dead_play = False
        all_sprites = pygame.sprite.Group()
        Mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        puss = pygame.sprite.Group()
        player = me()
        all_sprites.add(player)
        for i in range(4):
            spawnmob()
        points = 0

    clock.tick (FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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
        if m.picnumber == 2:
            points += 5 
            print("extreme!!!") 
        if m.picnumber == 3:
            points += 10
            print("mastery!!! !!")
        explode.play()
        expl = exploder(hit.rect.center, 'lg')
        all_sprites.add(expl)
        if random.random() > 0.7:
            power = powerup(hit.rect.center)
            all_sprites.add(power)
            puss.add(power)
        spawnmob()

    boom = pygame.sprite.spritecollide(player, Mobs, True)
    for bom in boom:
        m = Mob()
        if m.picnumber == 0:
            player.shield -= 1
        if m.picnumber == 1:
            player.shield -= 2
        if m.picnumber == 2:
            player.shield -= 4
        if m.picnumber == 3:
            player.shield -= 8
        spawnmob()
        expl = exploder(bom.rect.center, 'sm')
        all_sprites.add(expl)
        if player.shield <= 0:
            death_expl = exploder(player.rect.center, 'pl')
            all_sprites.add(death_expl)
            player.hide()
            player.lives -= 1
            player.shield = 50

            if not player.lives == 0  and not death_expl.alive():
                dead_play = True 
                print("points:" , points)

    crash = pygame.sprite.spritecollide(player, puss, True)
    for crsh in crash:
        if crsh.type == 'sh':
            player.shield += 15
            if player.shield >= 50:
                player.shield = 50
        if crsh.type == 'gu':
            player.pow()
        if crsh.type == 'la':
            player.lives += 1
            if player.lives >= 5:
                player.lives = 5
    
    surfacekairui.fill((60, 179, 113))
    back = pygame.transform.scale(background, (WIDTH,HEIGHT))
    surfacekairui.blit(back, background_rect)
    all_sprites.draw(surfacekairui)
    draw(surfacekairui, str(points), 20, WIDTH / 2, 5)
    draw_shield_bar(surfacekairui, 10, 10, player.shield)
    draw_lives(surfacekairui, WIDTH - 100, HEIGHT - 15, player.lives, mini_player)
    pygame.display.flip()

pygame.quit()