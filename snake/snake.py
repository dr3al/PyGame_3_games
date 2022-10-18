import pygame
from random import randint

SCREEN_RES = (600, 600)

pygame.init()
game = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 30)


class Snake:
    def __init__(self):
        self.snake = [[100, 100]]
        self.snakeX = []
        self.snakeY = []
        self.count = 1
        self.changeX = 0
        self.changeY = 0
        self.speed = 10
        self.size = 10
        self.score = 0

    def getSnake(self):
        for pos in self.snake:
            pygame.draw.rect(game, (255, 255, 255), (pos[0], pos[1], self.size, self.size))

    def getScore(self):
        text = font.render(f"Score: {self.score}", True, (255, 0, 0))
        game.blit(text, (0, 0))

    def setSpeed(self, key):
        if key == pygame.K_UP:
            self.changeX = 0
            self.changeY = -self.speed
        elif key == pygame.K_DOWN:
            self.changeX = 0
            self.changeY = self.speed
        elif key == pygame.K_LEFT:
            self.changeX = -self.speed
            self.changeY = 0
        elif key == pygame.K_RIGHT:
            self.changeX = self.speed
            self.changeY = 0

    def step(self):
        self.snake.append([self.snake[-1][0] + self.changeX, self.snake[-1][1] + self.changeY])
        self.snake.pop(0)
        self.snakeX = [i[0] for i in self.snake]
        self.snakeY = [i[1] for i in self.snake]
        self.checkFood(food)

    def checkFood(self, food):
        if (food.x - food.radius <= self.snake[-1][0] <= food.x + food.radius and\
                food.y - food.radius <= self.snake[-1][1] <= food.y + food.radius) or \
            (food.x - food.radius <= self.snake[-1][0] + self.size <= food.x + food.radius and\
             food.y - food.radius <= self.snake[-1][1] + self.size <= food.y + food.radius):
            food.newPosition(self)
            self.snake.append(self.snake[-1])
            self.score += 1
            self.step()

    def checkCrash(self):
        if not (0 <= self.snake[-1][0] <= SCREEN_RES[0] and 0 <= self.snake[-1][1] <= SCREEN_RES[1]):
            print(1)
            return 1
        elif self.snake.count(self.snake[-1]) > 1:
            print(2)
            return 1
        else:
            return 0


class Food:
    def __init__(self):
        self.x = randint(0, SCREEN_RES[0])
        self.y = randint(0, SCREEN_RES[1])
        self.radius = 5

    def newPosition(self, snake):
        self.x = randint(0, SCREEN_RES[0])
        self.y = randint(0, SCREEN_RES[1])
        while self.x in snake.snakeX and self.y in snake.snakeY:
            self.x = randint(0, SCREEN_RES[0])
            self.y = randint(0, SCREEN_RES[1])

    def getFood(self):
        pygame.draw.circle(game, (255, 255, 255), (self.x, self.y), self.radius)


snake = Snake()
food = Food()
running = True

while running:
    game.fill((0, 0, 0))
    food.getFood()
    snake.getSnake()
    snake.getScore()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            snake.setSpeed(event.key)

    snake.step()
    if snake.checkCrash():
        running = False
    clock.tick(snake.speed)

    pygame.display.update()
