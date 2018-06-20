from parameters import MAP_HEIGHT, MAP_WIDTH, MAX_ROOMS, MAX_ROOM_SIZE, MIN_ROOM_SIZE
import random


class Map(object):
    def __init__(self):
        self.level = []
        self.rooms = []
        # level values of 1 are walls
        # level values of 0 are floors

    def generateMap(self, mapWidth, mapHeight):
        # Creates an empty 2D array
        self.level = [[1 for y in range(mapHeight)]
                      for x in range(mapWidth)]

        self.rooms = []
        num_rooms = 0

        for r in range(MAX_ROOMS):
            # random width and height
            w = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            h = random.randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
            # random position within map boundries
            x = random.randint(0, MAP_WIDTH - w - 1)
            y = random.randint(0, MAP_HEIGHT - h - 1)

            new_room = Rect(x, y, w, h)
            # check for overlap with previous rooms
            failed = False
            for other_room in self.rooms:
                if new_room.intersect(other_room):
                    failed = True
                    break

            if not failed:
                self.createRoom(new_room)
                (new_x, new_y) = new_room.center()

                if num_rooms != 0:
                    # all rooms after the first one
                    # connect to the previous room

                    # center coordinates of the previous room
                    (prev_x, prev_y) = self.rooms[num_rooms - 1].center()

                    # 50% chance that a tunnel will start horizontally
                    if random.randint(0, 1) == 1:
                        self.createHorTunnel(prev_x, new_x, prev_y)
                        self.createVirTunnel(prev_y, new_y, new_x)

                    else:  # else it starts vertically
                        self.createVirTunnel(prev_y, new_y, prev_x)
                        self.createHorTunnel(prev_x, new_x, new_y)

                # append the new room to the list
                self.rooms.append(new_room)
                num_rooms += 1

        return self.level


    def createRoom(self, room):
        # set all tiles within a rectangle to 0
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.level[x][y] = 0

    def createHorTunnel(self, x1, x2, y):
        for x in range(min(int(x1), int(x2)), max(int(x1), int(x2)) + 1):
            self.level[x][int(y)] = 0

    def createVirTunnel(self, y1, y2, x):
        for y in range(min(int(y1), int(y2)), max(int(y1), int(y2)) + 1):
            self.level[int(x)][y] = 0


class Rect: # used for creating rooms
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x+w
        self.y2 = y+h

    def center(self):
        centerX = (self.x1 + self.x2)/2
        centerY = (self.y1 + self.y2)/2
        return (centerX, centerY)

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
            self.y1 <= other.y2 and self.y2 >= other.y1)