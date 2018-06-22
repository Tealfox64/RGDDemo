import input
from parameters import TILE_WIDTH, TILE_HEIGHT


class player:
    def __init__(self, block):
        self.x = block.x
        self.y = block.y
        self.xSpeed = 0
        self.ySpeed = 0
        self.timer = 0

    def update(self, tiles):
        if self.timer > 0:
            self.move()
        else:
            self.xSpeed, self.ySpeed = (0,) * 2
            if input.controls.upPressed:
                if collision(self.x, self.y - TILE_HEIGHT, tiles):
                    self.timer = 8
                    self.ySpeed = -4
            elif input.controls.downPressed:
                if collision(self.x, self.y + TILE_HEIGHT, tiles):
                    self.timer = 8
                    self.ySpeed = 4
            elif input.controls.leftPressed:
                if collision(self.x - TILE_WIDTH, self.y, tiles):
                    self.timer = 8
                    self.xSpeed = -4
            elif input.controls.rightPressed:
                if collision(self.x + TILE_WIDTH, self.y, tiles):
                    self.timer = 8
                    self.xSpeed = 4

    def move(self):
        self.timer -= 1
        self.x += self.xSpeed
        self.y += self.ySpeed


def collision(x, y, tiles):
    for i in tiles:
        if i.x == x and i.y == y:
            return True
    return False
