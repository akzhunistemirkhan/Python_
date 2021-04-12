import pygame
import time
import random

pygame.init()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 400
HEIGHT = 600
screen_size=(400,600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Game")

BACKGROUND = pygame.image.load("trassa2.png")

FPS = 60
timer = pygame.time.Clock()

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, WHITE)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy9.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())

        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 400

    def move(self):
        global score 
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            score += 0
            #self.speed = random.randint(500,900) #разные скорости
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

#я
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player16.png")
        self.surf = pygame.Surface(self.image.get_size())
        center = (WIDTH//2, HEIGHT - self.image.get_height()//2)
        self.rect = self.surf.get_rect(center = center)
        self.speed = 300
 
    def move(self):
        pixels_per_frame = self.speed // FPS
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -pixels_per_frame)
        if self.rect.bottom < HEIGHT:        
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, pixels_per_frame)
         
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-pixels_per_frame, 0)
        if self.rect.right < WIDTH:        
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(pixels_per_frame, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#монетка
class money11(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("money5.png")
        self.width, self.height = self.image.get_size()
        self.surf = pygame.Surface(self.image.get_size())
        center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                  -self.height // 2)
        self.rect = self.surf.get_rect(center=center)

        self.speed = 300

    def move(self):
        global score 
        pixels_per_frame = self.speed // FPS
        self.rect.move_ip(0, pixels_per_frame)
        if self.rect.top > HEIGHT:
            score += 0
            self.speed = random.randint(100,400) #разные скорости
            center = (random.randint(self.width // 2, WIDTH - self.width // 2), 
                    -self.height // 2)
            self.rect.center = center
    def draw(self, surface):
        surface.blit(self.image, self.rect) 

enemy = Enemy()
Money = money11()
player = Player()
        
enemies = pygame.sprite.Group()
enemies.add(enemy)
bonus = pygame.sprite.Group()
bonus.add(Money)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(Money)
all_sprites.add(enemy) 


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

score = 0
done = False
while not done:
    timer.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if pygame.sprite.spritecollideany(player, enemies):
        pygame.mixer.Sound('crash.wav').play()
        screen.fill(RED)
        text = game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over, (30,250))
        pygame.display.flip()
        for sprite in all_sprites:
            sprite.kill() 
        time.sleep(4)
        done = True
    
    screen.blit(BACKGROUND, (0, 0))

    scores = font_small.render(str(score), False, RED)
    screen.blit(scores, (10, 10))

    for sprite in all_sprites:
        sprite.move()
        sprite.draw(screen)

    #добавление монет    
    collide = pygame.sprite.spritecollide(player, bonus, True)
    if collide:
        Money = money11()
        all_sprites.add(Money)
        bonus.add(Money)
        score += 5
        pygame.display.update()

    pygame.display.flip()

#pygame.quit()