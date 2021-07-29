import random 
import time
import pygame
from save import*

pygame.init()

pink = (255,100,180)
white = (255, 255, 255)
marroon = (115,0,0)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 155, 0)
blue = (50, 153, 213)
lime = (180,255,100)

WIDTH = 800
HEIGHT = 600

Running = True

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')
font = pygame.font.SysFont('Times New Roman', 28)
game_over = font.render('GAME OVER', False, red)

FPS = 40
timer = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = 5
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
        self.FPS = 45
        
        self.save_data = Save()
        self.save_data.save()

    def draw(self):
            for element in self.elements:
                pygame.draw.circle(screen, yellow, element, self.radius)

            if self.score == 2:
                for element in self.elements:
                    self.FPS += 3
                    pygame.draw.circle(screen, red, element, self.radius)
                    pygame.draw.line(screen,black,(0,200),(400,200),4)
                    pygame.draw.line(screen,black,(450,250),(750,250),6)

            if self.score == 3:
                for element in self.elements:
                    pygame.draw.circle(screen, blue, element, self.radius)
                    pygame.draw.line(screen,black,(0,200),(400,200),8)
                    pygame.draw.line(screen,black,(450,250),(750,250),4)
                    pygame.draw.line(screen,black,(0,400),(550,400),4)
            if self.score == 4:
                for element in self.elements:
                    pygame.draw.circle(screen, green, element, self.radius)
                    pygame.draw.line(screen,black,(0,200),(400,200),4)
                    pygame.draw.line(screen,black,(450,250),(750,250),6)
            if self.score == 5:
                for element in self.elements:
                    pygame.draw.circle(screen, white, element, self.radius)
                    pygame.draw.line(screen,black,(0,200),(400,200),6)
                    pygame.draw.line(screen,black,(450,250),(750,250),8)
            if self.score == 6:
                for element in self.elements:
                    pygame.draw.circle(screen, lime, element, self.radius) 
                    pygame.draw.line(screen,black,(0,200),(400,200),4)
                    pygame.draw.line(screen,black,(450,250),(750,250),8)
            if self.score == 7:
                for element in self.elements:
                    pygame.draw.circle(screen, pink, element, self.radius) 
                    pygame.draw.line(screen,black,(0,200),(400,200), 8)
                    pygame.draw.line(screen,black,(450,250),(750,250), 10)
            if self.score == 8:
                for element in self.elements:
                    pygame.draw.circle(screen,marroon, element, self.radius)        
                    pygame.draw.line(screen,black,(0,200),(400,200), 8)
                    pygame.draw.line(screen,black,(450,250),(750,250), 6)

    def add_snake(self):
        self.size += 1
        self.score += 1
        self.FPS += 5
        self.elements.append([0, 0])
        self.is_add = False

    def move(self):
        if self.is_add:
            self.add_snake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]
        
        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy


class Food:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 70)
        self.y = random.randint(100, HEIGHT - 70)
        self.image = pygame.image.load("strawberry1.png")
        
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        if snake.score == 2:
            self.image = pygame.image.load("apple1.png")
            
        if snake.score == 3:
            self.image = pygame.image.load("banana.png")

        if snake.score == 4:
            self.image = pygame.image.load("avacado1.png") 

        if snake.score == 5:
            self.image = pygame.image.load("arbuz.png")
            
        if snake.score == 6:
            self.image = pygame.image.load("pototo.png")
        
        if snake.score == 7:
            self.image = pygame.image.load("apple1.png")

def show_score(x, y, score):
            show = font.render('Score: ' + str(score), True, (50, 28, 217))
            screen.blit(show, (x, y))   

def strike():
    if(food.x in range(snake.elements[0][0] - 20, snake.elements[0][0])) and (food.y in range(snake.elements[0][1] - 20, snake.elements[0][1])):
        snake.is_add = True
        food.x = random.randint(50, WIDTH - 70)
        food.y = random.randint(50, HEIGHT - 70)
def walls():
    return snake.elements[0][0] > WIDTH - 25 or snake.elements[0][0] < 30


def show_walls():
    for i in range(0, WIDTH, 15):
        screen.blit(image, (i, 0))
        screen.blit(image, (i, HEIGHT - 20))
        screen.blit(image, (0, i))
        screen.blit(image, (WIDTH - 20, i))

def over():
    screen.fill(blue)
    txt = font.render('GAME OVER', True, black)
    my_score = font.render('Total score: ' + str(snake.score), True, red)
    screen.blit(txt, (300, 200))
    screen.blit(my_score, (300, 250))
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()     
    
snake = Snake()
#snake1 = Snake()
food = Food()

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

image = pygame.image.load('block.jpg')

Running = False
while not Running:
    timer.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.dx = 5
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    snake.dx = -5
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    snake.dx = 0
                    snake.dy = -5
                if event.key == pygame.K_DOWN:
                    snake.dx = 0
                    snake.dy = 5
    
    if walls():
        over()
        Running = False

    strike()
    screen.fill((125, 206, 216))
    snake.move()
    #snake1.move()
    #snake1.draw()
    snake.draw()
    food.draw()
    show_score(35, 45, snake.score)
    #show_score(55, 65, snake1.score)
    show_walls()
    pygame.display.flip()