import pygame
from random import randint

SCREEN_RES = (540, 335)

pygame.init()

BACKGROUND = pygame.image.load('background.png')
EGG = pygame.image.load("egg.png")
LIFE = pygame.image.load("life.png")
LT = pygame.image.load("LT.png")
LB = pygame.image.load("LB.png")
RT = pygame.image.load("RT.png")
RB = pygame.image.load("RB.png")
FONT = pygame.font.Font("font.ttf", 30)
COLLECT = pygame.mixer.Sound("Collect.wav")
OOPS = pygame.mixer.Sound("Oops.wav")

game = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption("Wolf")
clock = pygame.time.Clock()


class Wolf:
    def __init__(self):
        self.x = 270
        self.y = 126
        self.view = RT
        self.score = 0
        self.lives = 3
        self.lives_pos = [(121, 28), (173, 28), (225, 28)]

    def changePos(self, key):
        if key == pygame.K_LEFT:
            self.x = 112
            self.y = 128
            if self.view == RT:
                self.view = LT
            elif self.view == RB:
                self.view = LB

        elif key == pygame.K_RIGHT:
            self.x = 270
            self.y = 126
            if self.view == LT:
                self.view = RT
            elif self.view == LB:
                self.view = RB

        elif key == pygame.K_UP:
            if self.view == LB:
                self.x = 112
                self.y = 128
                self.view = LT
            elif self.view == RB:
                self.x = 270
                self.y = 126
                self.view = RT

        elif key == pygame.K_DOWN:
            if self.view == LT:
                self.x = 112
                self.y = 128
                self.view = LB
            elif self.view == RT:
                self.x = 270
                self.y = 128
                self.view = RB

    def getWolf(self):
        global lose

        game.blit(self.view, (self.x, self.y))

        score = FONT.render(str(self.score), True, (255, 0, 0))
        game.blit(score, (390, 50))

        match self.lives:
            case 2:
                game.blit(LIFE, self.lives_pos[0])
            case 1:
                game.blit(LIFE, self.lives_pos[0])
                game.blit(LIFE, self.lives_pos[1])
            case 0:
                game.blit(LIFE, self.lives_pos[0])
                game.blit(LIFE, self.lives_pos[1])
                game.blit(LIFE, self.lives_pos[2])
                show_message("Game over!")
                lose = True


class Egg:
    def __init__(self):
        self.eggs = ["RB0"]
        self.pos = {"LT0": (34, 106), "LT1": (52, 117), "LT2": (70, 128), "LT3": (88, 139), "LT4": (112, 150),
                    "LB0": (34, 188), "LB1": (52, 199), "LB2": (70, 210), "LB3": (88, 221), "LB4": (106, 232),
                    "RT0": (492, 106), "RT1": (474, 117), "RT2": (456, 128), "RT3": (438, 139), "RT4": (420, 150),
                    "RB0": (492, 191), "RB1": (474, 202), "RB2": (456, 212), "RB3": (438, 224), "RB4": (420, 235)}

    def move(self):
        global frame
        if frame == 40:
            if len(self.eggs) == 5:
                if (self.eggs[0][0:2] == "LT" and wolf.view == LT) or (self.eggs[0][0:2] == "RT" and wolf.view == RT) or\
                        (self.eggs[0][0:2] == "LB" and wolf.view == LB) or (self.eggs[0][0:2] == "RB" and wolf.view == RB):
                    wolf.score += 1
                    COLLECT.play()
                else:
                    wolf.lives -= 1
                    OOPS.play()

                self.eggs.pop(0)

            self.eggs = [i[0:2]+str(int(i[2])+1) for i in self.eggs]
            match randint(1, 4):
                case 1:
                    self.eggs.append("LT0")
                case 2:
                    self.eggs.append("LB0")
                case 3:
                    self.eggs.append("RT0")
                case 4:
                    self.eggs.append("RB0")

            frame = 0

        frame += 1

    def getEggs(self):
        for i in self.eggs:
            game.blit(EGG, self.pos[i])


def show_message(message):
    text = FONT.render(message, True, (0, 0, 0))
    game.blit(text, (128, 70))


wolf = Wolf()
egg = Egg()

running = True
lose = False
frame = 0

while running:
    if lose:
        pygame.time.wait(3000)
        running = False

    game.blit(BACKGROUND, (0, 0))
    egg.getEggs()
    wolf.getWolf()
    egg.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            wolf.changePos(event.key)

    clock.tick(60)

    pygame.display.update()
