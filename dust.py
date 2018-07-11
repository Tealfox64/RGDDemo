from math import floor
import pygame as game

class smoke:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y

        self.group = group

        self.groundImage = game.image.load("dust.png")
        self.sprite = [(0, 0, 16, 16), (0, 16, 16, 16), (0, 32, 16, 16), (0, 48, 16, 16)]
        self.imageIndex = 0
        self.group.append(self)

    def update(self, tiles):
        if len(self.sprite) - 1 <= self.imageIndex:
            self.group.remove(self)
        self.imageIndex += 0.1

    def draw(self, gameDisplay, camera):
        gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.sprite[floor(self.imageIndex)]))

