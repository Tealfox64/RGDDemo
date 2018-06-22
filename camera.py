from parameters import resolution, TILE_WIDTH, TILE_HEIGHT


class centerScreen:
    def __init__(self, follow):
        self.x = 0
        self.y = 0
        self.follow = follow

    def update(self):
        self.x = self.follow.x - resolution.res[0] / 2 + TILE_WIDTH / 2
        self.y = self.follow.y - resolution.res[1] / 2 + TILE_HEIGHT / 2
