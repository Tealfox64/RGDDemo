from parameters import TILE_WIDTH, TILE_HEIGHT
import pygame as game
from math import floor
from input import controls


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0

        self.groundImage = game.image.load("player.png")
        self.down = [(2, 0, 16, 32), (34, 0, 16, 32), (66, 0, 16, 32), (98, 0, 16, 32), (130, 0, 16, 32),
                     (162, 0, 16, 32), (194, 0, 16, 32), (226, 0, 16, 32)]
        self.up = [(2, 48, 16, 32), (34, 48, 16, 32), (66, 48, 16, 32), (98, 48, 16, 32), (130, 48, 16, 32),
                   (162, 48, 16, 32), (194, 48, 16, 32), (226, 48, 16, 32)]
        self.right = [(2, 96, 16, 32), (34, 96, 16, 32), (66, 96, 16, 32), (98, 96, 16, 32), (130, 96, 16, 32),
                      (162, 96, 16, 32), (194, 96, 16, 32), (226, 96, 16, 32)]
        self.left = [(226, 140, 16, 32), (194, 140, 16, 32), (162, 140, 16, 32), (130, 140, 16, 32), (98, 140, 16, 32),
                     (66, 140, 16, 32), (34, 140, 16, 32), (2, 140, 16, 32)]
        self.direction = self.down
        self.imageIndex = 0
        self.imageSpeed = 0

    def update(self, tiles):
        self.imageSpeed = 0
        if not (controls.upPressed and controls.downPressed):
            if controls.upPressed:
                if not tiles[floor(self.x / TILE_WIDTH)][floor((self.y - 1) / TILE_HEIGHT)]:
                    self.direction = self.up
                    self.y -= 2
                    self.imageSpeed = 0.25
            elif controls.downPressed:
                if not tiles[floor(self.x / TILE_WIDTH)][floor((self.y + 16) / TILE_HEIGHT)]:
                    self.direction = self.down
                    self.y += 2
                    self.imageSpeed = 0.25
        if not (controls.leftPressed and controls.rightPressed):
            if controls.leftPressed:
                if not tiles[floor((self.x - 1) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]:
                    self.direction = self.left
                    self.x -= 2
                    self.imageSpeed = 0.25
            elif controls.rightPressed:
                if not tiles[floor((self.x + 16) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]:
                    self.direction = self.right
                    self.x += 2
                    self.imageSpeed = 0.25

        if not (tiles[floor((self.x - 1) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)] or
                tiles[floor((self.x + 16) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]):
            self.x += self.xSpeed
        else:
            self.xSpeed = 0

        if not (tiles[floor(self.x / TILE_WIDTH)][floor((self.y - 1) / TILE_HEIGHT)] or
                tiles[floor(self.x / TILE_WIDTH)][floor((self.y + 16) / TILE_HEIGHT)]):
            self.y += self.ySpeed
        else:
            self.ySpeed = 0

        # Set xSpeed friction
        if abs(self.xSpeed) <= 0.5:
            self.xSpeed = 0
        else:
            self.xSpeed -= (self.xSpeed / abs(self.xSpeed)) / 5

        # Set ySpeed friction
        if abs(self.ySpeed) <= 0.5:
            self.ySpeed = 0
        else:
            self.ySpeed -= (self.ySpeed / abs(self.ySpeed)) / 5

    def draw(self, gameDisplay, camera):
        self.imageIndex = (self.imageIndex + self.imageSpeed) % len(self.direction)
        if self.imageSpeed == 0:
            self.imageIndex = 7
        gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                        (self.direction[floor(self.imageIndex)]))
