from parameters import TILE_WIDTH, TILE_HEIGHT
import pygame
from math import floor
from input import controls


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.direction = 180

        self.groundImage = pygame.image.load("player.png")
        self.down = [(2, 0, 16, 32), (34, 0, 16, 32), (66, 0, 16, 32), (98, 0, 16, 32), (130, 0, 16, 32),
                     (162, 0, 16, 32), (194, 0, 16, 32), (226, 0, 16, 32)]
        self.up = [(2, 48, 16, 32), (34, 48, 16, 32), (66, 48, 16, 32), (98, 48, 16, 32), (130, 48, 16, 32),
                   (162, 48, 16, 32), (194, 48, 16, 32), (226, 48, 16, 32)]
        self.right = [(2, 96, 16, 32), (34, 96, 16, 32), (66, 96, 16, 32), (98, 96, 16, 32), (130, 96, 16, 32),
                      (162, 96, 16, 32), (194, 96, 16, 32), (226, 96, 16, 32)]
        self.left = [(226, 140, 16, 32), (194, 140, 16, 32), (162, 140, 16, 32), (130, 140, 16, 32), (98, 140, 16, 32),
                     (66, 140, 16, 32), (34, 140, 16, 32), (2, 140, 16, 32)]
        self.imageIndex = 0
        self.imageSpeed = 0

    def update(self, tiles):
        self.imageSpeed = 0
        if not (controls.upPressed and controls.downPressed):
            if controls.upPressed:
                if not collision(self.x / TILE_HEIGHT, (self.y - 1) / TILE_WIDTH, tiles):
                    self.direction = 0
                    self.y -= 2
                    self.imageSpeed = 0.25
            if controls.downPressed:
                if not collision(self.x / TILE_HEIGHT, (self.y + 16) / TILE_WIDTH, tiles):
                    self.direction = 180
                    self.y += 2
                    self.imageSpeed = 0.25
        if not (controls.leftPressed and controls.rightPressed):
            if controls.leftPressed:
                if not collision((self.x - 1) / TILE_HEIGHT, self.y / TILE_WIDTH, tiles):
                    self.direction = 270
                    self.x -= 2
                    self.imageSpeed = 0.25
            if controls.rightPressed:
                if not collision((self.x + 16) / TILE_HEIGHT, self.y / TILE_WIDTH, tiles):
                    self.direction = 90
                    self.x += 2
                    self.imageSpeed = 0.25

    def draw(self, gameDisplay, camera):
        self.imageIndex = (self.imageIndex + self.imageSpeed) % len(self.down)
        if self.imageSpeed == 0:
            self.imageIndex = 7
        if self.direction == 180:
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                             (self.down[floor(self.imageIndex)]))
        elif self.direction == 0:
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                             (self.up[floor(self.imageIndex)]))
        elif self.direction == 270:
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                             (self.left[floor(self.imageIndex)]))
        elif self.direction == 90:
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                             (self.right[floor(self.imageIndex)]))


def collision(x, y, tiles):
    if tiles[int(x)][int(y)]:
        return True
    return False
