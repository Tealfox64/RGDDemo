from parameters import TILE_HEIGHT, TILE_WIDTH


class tile:
    def __init__(self, x, y):
        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT