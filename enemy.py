from math import atan2, cos, sin, floor
import pygame as game

from parameters import TILE_HEIGHT, TILE_WIDTH


class ghost:
    def __init__(self, x, y, group, player):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.speed = 1
        self.player = player

        self.groundImage = game.image.load("enemy.png")
        self.up = [[(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32)],             # left
                   [(128, 0, 32, 32), (160, 0, 32, 32), (192, 0, 32, 32), (224, 0, 32, 32)]]        # right
        self.down = [[(0, 32, 32, 32), (32, 32, 32, 32), (64, 32, 32, 32), (96, 32, 32, 32)],       # left
                     [(128, 32, 32, 32), (160, 32, 32, 32), (192, 32, 32, 32), (224, 32, 32, 32)]]  # right
        self.imageIndex = 0
        self.imageSpeed = 0
        group.append(self)

    def update(self, tiles):
        self.xSpeed = self.speed * cos(angle(self.x, self.y, self.player.x, self.player.y))
        self.ySpeed = self.speed * sin(angle(self.x, self.y, self.player.x, self.player.y))
        if not tiles[floor((self.x / TILE_HEIGHT) + self.xSpeed)][floor((self.y - 1) / TILE_WIDTH)]:
            self.x += self.xSpeed
        else:
            self.ySpeed = self.speed * (self.ySpeed / abs(self.ySpeed))
        if not tiles[floor(self.x / TILE_HEIGHT)][floor(((self.y - 1) / TILE_WIDTH) + self.ySpeed)]:
            self.y += self.ySpeed
        else:
            if not tiles[floor((self.x / TILE_HEIGHT) + self.xSpeed)][floor((self.y - 1) / TILE_WIDTH)]:
                self.x += self.xSpeed

        self.imageSpeed = 0

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

def angle(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return atan2(dy, dx)
