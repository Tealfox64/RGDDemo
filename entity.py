import input
from parameters import TILE_WIDTH, TILE_HEIGHT


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self, tiles):
        if input.controls.downPressed:
            if not collision(self.x / TILE_HEIGHT, (self.y + 16) / TILE_WIDTH, tiles):
                self.y += 1
        if input.controls.upPressed:
            if not collision(self.x / TILE_HEIGHT, (self.y - 1) / TILE_WIDTH, tiles):
                self.y -= 1
        if input.controls.leftPressed:
            if not collision((self.x - 1) / TILE_HEIGHT, self.y / TILE_WIDTH, tiles):
                self.x -= 1
        if input.controls.rightPressed:
            if not collision((self.x + 16) / TILE_HEIGHT, self.y / TILE_WIDTH, tiles):
                self.x += 1


def collision(x, y, tiles):
    if tiles[int(x)][int(y)]:
        return True
    return False