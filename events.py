from random import randint

from parameters import MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAP_WIDTH, MAP_HEIGHT
from tile import tile

centers = []

def placeRooms():
    temp = []
    map = []

    # Create an empty map
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            temp.append(False)
        map.append(temp[:])
        temp[:] = []

    # Create rooms randomly for each room
    for non in range(MAX_ROOMS):
        for i in range(MAP_WIDTH):
            for j in range(MAP_HEIGHT):
                if randint(0, MAP_HEIGHT * MAP_WIDTH) == 0:
                    createRoom(map, i, j)

    # Create tiles
    for i in range(MAP_WIDTH):
        for j in range(MAP_HEIGHT):
            if map[i][j]:
                temp.append(tile(i, j))

    return temp

def createRoom(map, x, y):
    size = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
    start = [x - size, y - size]

    # If room is out of map
    if x - size < 0 or y - size < 0 or x + size > MAP_WIDTH or y + size > MAP_HEIGHT:
        return

    # If room intersects with another room
    for i in range(size):
        for j in range(size):
            if map[start[0] + i][start[1] + j]:
                return

    # Create room
    for i in range(size):
        for j in range(size):
            map[start[0] + i][start[1] + j] = True
            centers.append([x, y])