from math import atan2, cos, sin, floor, sqrt
import pygame as game
import explosion

from parameters import TILE_HEIGHT, TILE_WIDTH


class ghost:
    def __init__(self, x, y, group, player):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.speed = 1.5
        self.player = player

        self.aware = False

        self.groundImage = game.image.load("enemy.png")
        self.up = [[(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32)],             # left
                   [(128, 0, 32, 32), (160, 0, 32, 32), (192, 0, 32, 32), (224, 0, 32, 32)]]        # right
        self.down = [[(0, 32, 32, 32), (32, 32, 32, 32), (64, 32, 32, 32), (96, 32, 32, 32)],       # left
                     [(128, 32, 32, 32), (160, 32, 32, 32), (192, 32, 32, 32), (224, 32, 32, 32)]]  # right
        self.imageIndex = 0
        self.group = group
        self.group.append(self)

    def update(self, tiles):
        if self.aware:
            self.xSpeed = self.speed * cos(angle(self.x, self.y, self.player.x, self.player.y))
            self.ySpeed = self.speed * sin(angle(self.x, self.y, self.player.x, self.player.y))
            if not (tiles[floor((self.x + self.xSpeed) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)] and
                    tiles[floor(self.x / TILE_WIDTH)][floor((self.y + self.ySpeed) / TILE_HEIGHT)]):
                if tiles[floor((self.x + self.xSpeed) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]:
                    self.xSpeed = 0
                    self.ySpeed = self.speed * ifNeg(self.ySpeed)
                elif tiles[floor(self.x / TILE_WIDTH)][floor((self.y + self.ySpeed) / TILE_HEIGHT)]:
                    self.xSpeed = self.speed * ifNeg(self.xSpeed)
                    self.ySpeed = 0
            else:
                self.xSpeed = 0
                self.ySpeed = 0
            self.x += self.xSpeed
            self.y += self.ySpeed
            if distance(self, self.player) >= 300:
                self.aware = False
            elif distance(self, self.player) <= 10:
                explosion.explode(self.player.x, self.player.y, self.group)
                self.group.remove(self)
        else:
            if distance(self, self.player) <= 225:
                self.aware = True

    def draw(self, gameDisplay, camera):
        self.imageIndex = (self.imageIndex + 0.05) % len(self.down[0])
        if self.ySpeed >= 0:
            if self.xSpeed <= 0:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.down[0][floor(self.imageIndex)]))
            else:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.down[1][floor(self.imageIndex)]))
        else:
            if self.xSpeed <= 0:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.up[0][floor(self.imageIndex)]))
            else:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.up[1][floor(self.imageIndex)]))


def ifNeg(num):
    if num < 0:
        return -1
    return 1

def angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return atan2(dy, dx)

def distance(enemy, player):
    a = enemy.x - player.x
    b = enemy.y - player.y
    return sqrt((a * a) + (b * b))
