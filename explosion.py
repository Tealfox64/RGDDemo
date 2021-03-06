from math import floor
import pygame as game
import sound

class explode:
    def __init__(self, x, y, group):
        self.x = x
        self.y = y

        self.group = group
        sound.explosion.play(0)

        self.groundImage = game.image.load("explosion.png")
        self.sprite = [(0, 0, 32, 32), (0, 32, 32, 32), (0, 64, 32, 32), (0, 96, 32, 32), (0, 128, 32, 32)]
        self.imageIndex = 0
        self.group.append(self)

    def update(self, tiles):
        if len(self.sprite) - 1 <= self.imageIndex:
            self.group.remove(self)
        self.imageIndex += 0.1

    def draw(self, gameDisplay, camera):
        gameDisplay.blit(self.groundImage, (self.x - camera.x, self.y - camera.y - 16), (self.sprite[floor(self.imageIndex)]))
