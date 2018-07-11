import pygame
from math import floor

class light:
    def __init__(self):
        self.image = pygame.image.load("lighting.png").convert()
        self.alpha = 0.0

    def changeTransparency(self, inc):
        self.alpha += inc
        self.image.set_alpha(floor(self.alpha))
