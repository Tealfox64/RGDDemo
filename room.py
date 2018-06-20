import math

from parameters import TILE_WIDTH, TILE_HEIGHT


class Room(object):
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.x2 = x + w
        self.y1 = y
        self.y2 = y + w

        self.w = w
        self.h = h

        self.x = x * TILE_WIDTH
        self.y = y * TILE_HEIGHT

        self.center = (math.floor(((self.x1 + self.x2) / 2)), (math.floor(((self.y1 + self.y2) / 2))))

    def intersects(self, room):
        return self.x1 <= room.x2 and self.x2 >= room.x1 and self.y1 <= room.y2 and room.y2 >= room.y1


