import input
from parameters import TILE_WIDTH, TILE_HEIGHT


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, tiles):
        if input.controls.downPressed:
            #if collision(self.x, self.y + 2, tiles):
            self.y += 2
        if input.controls.upPressed:
            #if collision(self.x, self.y - 2, tiles):
            self.y -= 2
        if input.controls.leftPressed:
            #if collision(self.x - 2, self.y, tiles):
            self.x -= 2
        if input.controls.rightPressed:
            #if collision(self.x + 2, self.y, tiles):
            self.x += 2


def collision(x, y, tiles):
    for i in tiles:
        if x + 16 <= i.x + TILE_WIDTH and x >= i.x and y + 16 <= i.y + TILE_HEIGHT and y >= i.y:
            return True
