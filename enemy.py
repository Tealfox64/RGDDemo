from math import atan2, cos, sin, floor, sqrt, pi
import pygame as game
import explosion
from random import randint as rand

from parameters import TILE_HEIGHT, TILE_WIDTH


class ghost:
    def __init__(self, x, y, group, player, progress):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.speed = 1.5
        self.player = player
        self.offset = progress

        self.aware = False

        self.groundImage = game.image.load("enemy.png")
        self.up = [[(0, 0, 32, 32), (32, 0, 32, 32), (64, 0, 32, 32), (96, 0, 32, 32)],             # Left
                   [(128, 0, 32, 32), (160, 0, 32, 32), (192, 0, 32, 32), (224, 0, 32, 32)]]        # Right
        self.down = [[(0, 32, 32, 32), (32, 32, 32, 32), (64, 32, 32, 32), (96, 32, 32, 32)],       # Left
                     [(128, 32, 32, 32), (160, 32, 32, 32), (192, 32, 32, 32), (224, 32, 32, 32)]]  # Right
        self.imageIndex = 0
        self.group = group
        self.group.append(self)

    def update(self, tiles):
        if self.aware:
            self.xSpeed = self.speed * cos(angle(self, self.player))
            self.ySpeed = self.speed * sin(angle(self, self.player))
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
                self.player.xSpeed = 5 * cos(angle(self, self.player))
                self.player.ySpeed = 5 * sin(angle(self, self.player))
                explosion.explode(self.player.x, self.player.y, self.group)
                self.group.remove(self)
        else:
            if distance(self, self.player) <= 225:
                self.aware = True

    def draw(self, gameDisplay, camera):
        self.imageIndex = (self.imageIndex + 0.05) % len(self.down[0])
        if not(angle(self, self.player) * 180 / pi < 0):
            if not (-90 < angle(self, self.player) * 180 / pi < 90):
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 glitchImage(self.down[0][floor(self.imageIndex)], floor(self.offset.alpha)))
            else:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 glitchImage(self.down[1][floor(self.imageIndex)], floor(self.offset.alpha)))
        else:
            if not(-90 < angle(self, self.player) * 180 / pi < 90):
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 glitchImage(self.up[0][floor(self.imageIndex)], floor(self.offset.alpha)))
            else:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 glitchImage(self.up[1][floor(self.imageIndex)], floor(self.offset.alpha)))


def ifNeg(num):
    if num < 0:
        return -1
    return 1

def angle(first, second):
    dx = second.x - first.x
    dy = second.y - first.y
    return atan2(dy, dx)

def distance(enemy, player):
    a = enemy.x - player.x
    b = enemy.y - player.y
    return sqrt((a * a) + (b * b))

def glitchImage(image, offset):
    if offset < 100:
        return image
    return image[0] + (rand(0, offset) - (offset / 2) / 16), image[1], image[2], image[3]