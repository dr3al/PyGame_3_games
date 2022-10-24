import pygame
from random import randint

SCREEN_RES = (600, 600)

pygame.init()

game = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
BITE = pygame.mixer.Sound("Bite.wav")
FONT_SCORE = pygame.font.Font("font.ttf", 30)
FONT_MESSAGE = pygame.font.Font("font.ttf", 50)


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

    def get_snake(self):
        for pos in self.snake:
            pygame.draw.rect(game, (255, 255, 255), (pos[0], pos[1], self.size, self.size))

    def get_score(self):
        text = FONT_SCORE.render(f"Score: {self.score}", True, (255, 0, 0))
        game.blit(text, (0, 0))

    def set_speed(self, key):
        if key == pygame.K_UP and self.changeY == 0:
            self.changeX = 0
            self.changeY = -self.speed
        elif key == pygame.K_DOWN and self.changeY == 0:
            self.changeX = 0
            self.changeY = self.speed
        elif key == pygame.K_LEFT and self.changeX == 0:
            self.changeX = -self.speed
            self.changeY = 0
        elif key == pygame.K_RIGHT and self.changeX == 0:
            self.changeX = self.speed
            self.changeY = 0

    def step(self):
        global frame
        if frame == 3:
            self.snake.append([self.snake[-1][0] + self.changeX, self.snake[-1][1] + self.changeY])
            self.snake.pop(0)
            self.snakeX = [i[0] for i in self.snake]
            self.snakeY = [i[1] for i in self.snake]
            self.check_food()
            frame = 0
        frame += 1

    def check_food(self):
        if (food.x - food.radius <= self.snake[-1][0] <= food.x + food.radius and
                food.y - food.radius <= self.snake[-1][1] <= food.y + food.radius) or \
            (food.x - food.radius <= self.snake[-1][0] + self.size <= food.x + food.radius and
                food.y - food.radius <= self.snake[-1][1] + self.size <= food.y + food.radius):
            food.new_position()
            self.snake.append(self.snake[-1])
            self.score += 1
            BITE.play()
            self.step()

    def check_crash(self):
        if not (0 <= self.snake[-1][0] <= SCREEN_RES[0] and 0 <= self.snake[-1][1] <= SCREEN_RES[1]):
            return 1
        elif self.snake.count(self.snake[-1]) > 1:
            return 1
        else:
            return 0


class Food:
    def __init__(self):
        self.x = randint(0, SCREEN_RES[0])
        self.y = randint(0, SCREEN_RES[1])
        self.radius = 5

    def new_position(self):
        self.x = randint(self.radius, SCREEN_RES[0]-self.radius*2)
        self.y = randint(self.radius, SCREEN_RES[1]-self.radius*2)
        while self.x in snake.snakeX and self.y in snake.snakeY:
            self.x = randint(self.radius, SCREEN_RES[0]-self.radius*2)
            self.y = randint(self.radius, SCREEN_RES[1]-self.radius*2)

    def get_food(self):
        pygame.draw.circle(game, (255, 255, 255), (self.x, self.y), self.radius)


def get_message(message):
    text = FONT_MESSAGE.render(message, True, (255, 0, 0))
    game.blit(text, (200, 250))


snake = Snake()
food = Food()
running = True
lose = False
frame = 0

while running:

    if lose:
        pygame.time.wait(3000)
        running = False

    game.fill((0, 0, 0))
    food.get_food()
    snake.get_snake()
    snake.get_score()
    snake.step()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            snake.set_speed(event.key)
            snake.step()
            continue

    if snake.check_crash():
        get_message("Game over")
        lose = True

    clock.tick(60)

    pygame.display.update()
