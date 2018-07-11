class centerScreen:
    def __init__(self, follow):
        self.x = 0
        self.y = 0
        self.follow = follow

    def update(self):
        self.x = self.follow.x - 360 + 8
        self.y = self.follow.y - 240
