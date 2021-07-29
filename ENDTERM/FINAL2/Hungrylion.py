import pygame
import random
import time

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (191, 34, 51)
BLUE = (0, 0, 255)

WIDTH = 800
HEIGHT = 500
screen_size=(800,500)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Hungry lion")
font = pygame.font.SysFont('Times New Roman', 28)
game_over = font.render('GAME OVER', False, RED)
font_small = pygame.font.SysFont("Verdana", 20)

FPS = 60
timer = pygame.time.Clock()
 
class BRect(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.speed = 300
        self.rect = self.image.get_rect()
        
        
    def pos(self):
        self.rect.y = random.randrange(-300, -20)
        self.rect.x = random.randrange(80, WIDTH)
 
    def update(self):
        self.rect.y += 1
 
        if self.rect.y > 510:
            self.pos()
class Rrect(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.speed = 300
        self.rect = self.image.get_rect()
        
        
    def pos(self):
       self.rect.y = random.randrange(-300, -20)
       self.rect.x = random.randrange(80, WIDTH)
 
    def update(self):
        #self.rect.y += 0
        self.rect.x += random.randint(-1, 1)
        self.rect.y += random.randint(-1, 1)
 
        if self.rect.y > 510:
            self.pos()
 
class Player(BRect):
    def update(self):
        #pos = pygame.mouse.get_pos()
        #self.rect.x = pos[0]
        #self.rect.y = pos[1]
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
 
pygame.init()
 
block = pygame.sprite.Group()
blocks = pygame.sprite.Group()

all_sprites_list = pygame.sprite.Group()
 
for i in range(60):
    green_block = Rrect(GREEN, 20, 20)

    green_block.rect.x = random.randrange(WIDTH)
    green_block.rect.y = random.randrange(HEIGHT)
    block.add(green_block)
    all_sprites_list.add(green_block)

    
for i in range(35):
    red_block = BRect(RED, 20, 15)

    red_block.rect.x = random.randrange(WIDTH)
    red_block.rect.y = random.randrange(HEIGHT)
    blocks.add(red_block)
    all_sprites_list.add(red_block)

player = Player(BLUE, 20, 25)
all_sprites_list.add(player)
 
done = False
clock = pygame.time.Clock()
 
score = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if score < -5:
        screen.fill(RED)
        txt = font.render('GAME OVER', True, BLACK)
        my_score = font.render('Total score: ' + str(score), True, WHITE)
        screen.blit(txt, (300, 100))
        screen.blit(my_score, (300, 150))
        pygame.display.flip()
        time.sleep(2)
        done = True
        pygame.quit()  

    if score == 45:
        screen.fill(WHITE)
        txt = font.render('You are the winner!', True, BLUE)
        my_score = font.render('Total score: ' + str(score), True, RED)
        screen.blit(txt, (300, 100))
        screen.blit(my_score, (300, 150))
        pygame.display.flip()
        time.sleep(4)
        done = True
        pygame.quit()

    

    all_sprites_list.update()

    screen.fill((230,255,255))
 
    block_hit_list = pygame.sprite.spritecollide(player, block, True)
    blocks_hit_list = pygame.sprite.spritecollide(player, blocks, True)
 
   
    for green_block in block_hit_list:
        score += 1

    for red_block in blocks_hit_list:
        score -= 1

    scoress = font_small.render('Score:' , True, BLACK)
    scores = font_small.render(str(score) , True, BLACK)
    screen.blit(scoress, (10, 10))
    screen.blit(scores, (80, 10))
        
 
    green_block.pos()
    red_block.pos()
    all_sprites_list.draw(screen)
    clock.tick(40)
    pygame.display.flip()
pygame.quit()