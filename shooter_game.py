#Create your own shooter

from pygame import *
from random import randint
from time import time as timer
import random
WIDTH = 700
HEIGHT = 500
lost = 0
score = 0
winning = 0
losing = 0
max_lost = 0
hp = 1
rel_time = False
num_fire = 0
window = display.set_mode((WIDTH,HEIGHT))
display.set_caption("Space shoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooter 2........000000000")
clock = time.Clock()
background = transform.scale(image.load("galaxy.jpg"),(WIDTH,HEIGHT))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx-2, self.rect.top, 15, 20,12)
        bullets.add(bullet)

        bullet2 = Bullet("bullet.png", self.rect.centerx-10, self.rect.top, 15, 20,10)
        bullets.add(bullet2)

        bullet3 = Bullet("bullet.png", self.rect.centerx+10, self.rect.top, 15, 20,13)
        bullets.add(bullet3)

        bullet4 = Bullet("bullet.png", self.rect.centerx-20, self.rect.top, 15, 20,12)
        bullets.add(bullet4)

        bullet5 = Bullet("bullet.png", self.rect.centerx+20, self.rect.top, 15, 20,14)
        bullets.add(bullet5)

        bullet6 = Bullet("bullet.png", self.rect.centerx-5, self.rect.top, 15, 20,16)
        bullets.add(bullet6)



        
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            global lost
            lost += 1
            self.rect.x = random.randint(80,WIDTH - 80)
            self.rect.y = 0

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

enemies = sprite.Group()
bullets = sprite.Group()
spaceship = Player("santaaa.png",5,HEIGHT - 100,80,100,10)
for i in range(6):
    enemy1 = Enemy("santa11.png",random.randint(80,WIDTH - 80), -10, 80,50, random.randint(1,5))
    enemies.add(enemy1)
asteroids  = sprite.Group()
for i in range(1,10):
    asteroid = Enemy("asteroid.png",random.randint(80,WIDTH - 80), -10, 80,50, random.randint(1,5))
    asteroid.add(asteroids)

run = True
mixer.init()
mixer.music.load("music.mp3")
mixer.music.play(-1) 
fire_sound = mixer.Sound("fire.ogg")
font.init()
font1 = font.SysFont("Arial", 80)
win = font1.render("You Win!", True, (255,255,255))
lose = font1.render("You Lose ha ha", True,(180,0,0))
font2 = font.Font(None, 36)
finish = False


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_r:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    spaceship.fire()
                    fire_sound.play()
                if num_fire >= 5 and rel_time == False:
                    last_time = timer()
                    rel_time = True
                


    if not finish:
        window.blit(background,(0,0))
        
        spaceship.update()
        spaceship.reset()
        enemies.update()
        enemies.draw(window)
        bullets.update()
        bullets.draw(window)
        asteroids.update()
        asteroids.draw(window)
        collides = sprite.groupcollide(enemies,bullets,True,True)
        if rel_time == True:
            now_time = timer()
            
            if now_time - last_time < 3:
                reload = font2.render("wait, reloading. please stand by",1,(150,0,0))
                window.blit(reload,(260,460))
            else:
                num_fire = 0
                rel_time = False
        for is_collide in collides:
            
            enemy = Enemy("santa11.png",random.randint(80,WIDTH - 80), -10, 80,50, random.randint(1,5))
            enemies.add(enemy)
            score += 1
        text = font2.render("Score:" + str(score), 1, (255,255,255))
        window.blit(text,(10,20))
        text_lose = font2.render("Missed:" + str(lost),1,(255,255,255))
        window.blit(text_lose,(10,50))
        if score >= 100:
            finish = True
            window.blit(win,(200,200))
        if lost >= 30:
            finish = True
            window.blit(lose,(200,200))
        display.update()
    
    else:
        finish = False
        score = 0
        lost = 0
        for b in bullets:
            b.kill()
        for m in enemies:
            m.kill()
        time.delay(3000)
        for i in range(1,6):
            monster = Enemy("santa11.png",randint(80,WIDTH - 80), -40,80,50, randint(1,5))
            enemies.add(enemies)
    clock.tick(60)