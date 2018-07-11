from parameters import TILE_WIDTH, TILE_HEIGHT
import pygame as game
from math import floor
from input import controls
import dust, sound
from random import randint as rand


class player:
    def __init__(self, x, y, everything):
        self.x = x
        self.y = y
        self.xSpeed = 0
        self.ySpeed = 0
        self.health = 3
        self.timer = 0
        self.delay = 0
        self.invincible = 0
        self.everything = everything

        self.groundImage = game.image.load("player.png")
        self.down = [(2, 0, 16, 32), (34, 0, 16, 32), (66, 0, 16, 32), (98, 0, 16, 32), (130, 0, 16, 32),
                     (162, 0, 16, 32), (194, 0, 16, 32), (226, 0, 16, 32)]
        self.up = [(2, 48, 16, 32), (34, 48, 16, 32), (66, 48, 16, 32), (98, 48, 16, 32), (130, 48, 16, 32),
                   (162, 48, 16, 32), (194, 48, 16, 32), (226, 48, 16, 32)]
        self.right = [(2, 96, 16, 32), (34, 96, 16, 32), (66, 96, 16, 32), (98, 96, 16, 32), (130, 96, 16, 32),
                      (162, 96, 16, 32), (194, 96, 16, 32), (226, 96, 16, 32)]
        self.left = [(226, 140, 16, 32), (194, 140, 16, 32), (162, 140, 16, 32), (130, 140, 16, 32), (98, 140, 16, 32),
                     (66, 140, 16, 32), (34, 140, 16, 32), (2, 140, 16, 32)]
        self.attack = [(0, 188, 24, 32), (28, 188, 28, 32), (64, 188, 28, 32), (96, 188, 32, 32)]
        self.heart = game.image.load("heart.png")
        self.direction = self.down
        self.imageIndex = 0
        self.imageSpeed = 0

    def update(self, tiles):
        self.imageSpeed = 0
        if 0 <= self.invincible:
            self.invincible -= 1
        if 0 <= self.delay:
            self.delay -= 1
        if 0 <= self.timer:
            self.timer -= 1
        else:
            if controls.spacePressed and self.delay <= 0:
                sound.whoosh.play(0)
                if self.direction == self.down:
                    self.ySpeed = 5
                elif self.direction == self.right:
                    self.xSpeed = 5
                elif self.direction == self.up:
                    self.ySpeed = -5
                else:
                    self.xSpeed = -5
                self.timer = 5
                self.delay = 32
                controls.spacePressed = False
            else:
                if not (controls.upPressed and controls.downPressed):
                    if controls.upPressed:
                        if tiles[floor(self.x / TILE_WIDTH)][floor((self.y - 2) / TILE_HEIGHT)]:
                            self.direction = self.up
                            self.y -= 2
                            self.imageSpeed = 0.25
                    elif controls.downPressed:
                        if tiles[floor(self.x / TILE_WIDTH)][floor((self.y + 16) / TILE_HEIGHT)]:
                            self.direction = self.down
                            self.y += 2
                            self.imageSpeed = 0.25
                if not (controls.leftPressed and controls.rightPressed):
                    if controls.leftPressed:
                        if tiles[floor((self.x - 2) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]:
                            self.direction = self.left
                            self.x -= 2
                            self.imageSpeed = 0.25
                    elif controls.rightPressed:
                        if tiles[floor((self.x + 16) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]:
                            self.direction = self.right
                            self.x += 2
                            self.imageSpeed = 0.25

        if (tiles[floor((self.x - 2) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)] and
            tiles[floor((self.x + 16) / TILE_WIDTH)][floor(self.y / TILE_HEIGHT)]):
            self.x += self.xSpeed
        else:
            self.xSpeed = 0

        if  (tiles[floor(self.x / TILE_WIDTH)][floor((self.y - 1) / TILE_HEIGHT)] and
             tiles[floor(self.x / TILE_WIDTH)][floor((self.y + 16) / TILE_HEIGHT)]):
            self.y += self.ySpeed
        else:
            self.ySpeed = 0

        # Set xSpeed friction
        if abs(self.xSpeed) <= 0.5:
            self.xSpeed = 0
        else:
            self.xSpeed -= 0.25 * (self.xSpeed / abs(self.xSpeed))

        # Set ySpeed friction
        if abs(self.ySpeed) <= 0.5:
            self.ySpeed = 0
        else:
            self.ySpeed -= 0.25 * (self.ySpeed / abs(self.ySpeed))

    def draw(self, gameDisplay, camera):
        for i in range(self.health):
            gameDisplay.blit(self.heart, (20 * i + 16, 16))
        if 0 > self.timer:
            self.imageIndex = (self.imageIndex + self.imageSpeed) % len(self.direction)
            if self.imageSpeed == 0:
                self.imageIndex = 7
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                            (self.direction[floor(self.imageIndex)]))
        else:
            if self.direction == self.up:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 (self.attack[0]))
            elif self.direction == self.left:
                gameDisplay.blit(self.groundImage, (self.x - camera.x - 8, self.y - camera.y - 16),
                                 (self.attack[1]))
            elif self.direction == self.right:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 (self.attack[2]))
            else:
                gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16),
                                 (self.attack[3]))
            dust.smoke(self.x + rand(-4, 4), self.y + rand(-4, 4) + 16, self.everything)
