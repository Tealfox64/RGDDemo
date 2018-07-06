from math import floor
import pygame as game

class explode:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y

        self.group = group

        self.groundImage = game.image.load("explosion.png")
        self.sprite = [(0, 0, 32, 32), (0, 32, 32, 32), (0, 64, 32, 32), (0, 96, 32, 32), (0, 128, 32, 32)]
        self.imageIndex = 0
        self.group.append(self)

    def update(self, tiles):
        self = self     # Do nothing

    def draw(self, gameDisplay, camera):
        try:
            self.imageIndex = (self.imageIndex + 0.1)
            gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.sprite[floor(self.imageIndex)]))
        except:
            self.group.remove(self)
