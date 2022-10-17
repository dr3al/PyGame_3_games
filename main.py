import pygame

from resources.images import BRICK, COIN, DOOR, PLAYER
from resources.maps import maps

SCREEN_RES = (1032, 774)

pygame.init()

game = pygame.display.set_mode(SCREEN_RES)

pygame.display.set_caption("Игра")

class Player():
    def __init__(self):
        self.x = 520
        self.y = 172
        self.rx = 563
        self.ry = 215
        self.coins = 0
        self.life = 3
        self.left = 0
        self.right = 0
        self.up = 0
        self.down = 0
        self.canPass = False

    def setModel(self):
        game.blit(PLAYER, (self.x, self.y))

    def setSpeed(self, direction):
        if direction == pygame.K_LEFT:
            player.left = -1
        elif direction == pygame.K_RIGHT:
            player.right = 1
        elif direction == pygame.K_UP:
            player.up = -1
        elif direction == pygame.K_DOWN:
            player.down = 1

    def move(self):
        global map
        global maps
        if player.up != 0 and map[(player.y + player.up) // 43][player.x // 43] != 1 and \
                map[(player.y + player.up) // 43][player.rx // 43] != 1:
            if map[(player.y + player.up) // 43][player.x // 43] == 2:
                self.collectCoin(player.x // 43, (player.y + player.up) // 43)
            elif map[(player.y + player.up) // 43][player.rx // 43] == 2:
                self.collectCoin(player.rx // 43, (player.y + player.up) // 43)
            if (map[(player.y + player.up) // 43][player.x // 43] == 3 or \
                    map[(player.y + player.up) // 43][player.rx // 43] == 3) and self.coins == 4:
                map = maps[1]
            self.y += self.up
            self.ry = self.y + 43

        elif player.down != 0 and map[(player.ry + player.down) // 43][player.x // 43] != 1 and \
                map[(player.ry + player.down) // 43][player.rx // 43] != 1:
            if map[(player.ry + player.down) // 43][player.x // 43] == 2:
                self.collectCoin(player.x // 43, (player.ry + player.down) // 43)
            elif map[(player.ry + player.down) // 43][player.rx // 43] == 2:
                self.collectCoin(player.rx // 43, (player.ry + player.down) // 43)
            if (map[(player.ry + player.down) // 43][player.x // 43] == 3 or \
                    map[(player.ry + player.down) // 43][player.rx // 43] == 3) and self.coins == 4:
                map = maps[1]
            self.y += self.down
            self.ry = self.y + 43

        if player.left != 0 and map[player.y // 43][(player.x + player.left) // 43] != 1 and \
                map[player.ry // 43][(player.x + player.left) // 43] != 1:
            if map[player.y // 43][(player.x + player.left) // 43] == 2:
                self.collectCoin((player.x + player.left) // 43, player.y // 43)
            elif map[player.ry // 43][(player.x + player.left) // 43] == 2:
                self.collectCoin((player.x + player.left) // 43, player.ry // 43)
            if (map[player.y // 43][(player.x + player.left) // 43] == 3 or \
                    map[player.ry // 43][(player.x + player.left) // 43] == 3) and self.coins == 4:
                map = maps[1]
            self.x += self.left
            self.rx = self.x + 43

        elif player.right != 0 and map[player.y // 43][(player.rx + player.right) // 43] != 1 and \
                map[player.ry // 43][(player.rx + player.right) // 43] != 1:
            if map[player.y // 43][(player.rx + player.right) // 43] == 2:
                self.collectCoin((player.rx + player.right) // 43, player.y // 43)
            elif map[player.ry // 43][(player.rx + player.right) // 43] == 2:
                self.collectCoin((player.rx + player.right) // 43, player.ry // 43)
            if (map[player.y // 43][(player.rx + player.right) // 43] == 3 or \
                    map[player.ry // 43][(player.rx + player.right) // 43] == 3) and self.coins == 4:
                map = maps[1]
            self.x += self.right
            self.rx = self.x + 43

    def stop(self, direction):
        if direction == pygame.K_LEFT:
            player.left = 0
        elif direction == pygame.K_RIGHT:
            player.right = 0
        elif direction == pygame.K_UP:
            player.up = 0
        elif direction == pygame.K_DOWN:
            player.down = 0

    def collectCoin(self, x, y):
        global map
        map[y][x] = 0
        self.coins += 1
        if self.coins == 4:
            self.canPass = True
        print(self.coins)

    def reduceLife(self):
        self.life -= 1

player = Player()

def getBlockInfo(pos):
    global player
    if pos == "YTL":
        blockX = player.x // 43
        blockY = (player.y + player.changeY) // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "YTR":
        blockX = player.rx // 43
        blockY = (player.y + player.changeY) // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "YBL":
        blockX = player.x // 43
        blockY = (player.ry + player.changeY) // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "YBR":
        blockX = player.rx // 43
        blockY = (player.ry + player.changeY) // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "XTL":
        blockX = (player.x + player.changeX) // 43
        blockY = player.y // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "XTR":
        blockX = (player.rx + player.changeX) // 43
        blockY = player.y // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "XBL":
        blockX = (player.x + player.changeX) // 43
        blockY = player.ry // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)
    elif pos == "XBR":
        blockX = (player.rx + player.changeX) // 43
        blockY = player.ry // 43
        blockType = map[blockY][blockY]
        return (blockY, blockX, blockType)

def setMap(map):
    №global step
    for y in range(18):
        for x in range(24):
            if map[y][x] == 1:
                game.blit(BRICK, (x * 43, y * 43))
            elif map[y][x] == 2:
                game.blit(COIN, (x * 43, y * 43))
            elif map[y][x] == 3:
                game.blit(DOOR, (x * 43, y * 43))
            elif map[y][x] == 4 and (step // 300 == 1 or step // 300 == 2 or step // 300 == 3):
                game.blit(DOOR, (x * 43, y * 43))
            elif map[y][x] == 5 and step // 300 == 2:
                game.blit(DOOR, (x * 43, y * 43))

running = True
map = maps[0]
step = 0

while running:
    game.fill((95, 50, 25))
    setMap(map)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            player.setSpeed(event.key)

        if event.type == pygame.KEYUP:
            player.stop(event.key)

    player.move()
    player.setModel()

    step += 1
    if step == 1200:
        step = 0


    pygame.display.update()
