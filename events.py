from random import randint
from math import floor
from parameters import MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAP_WIDTH, MAP_HEIGHT
from tile import tile


def placeRooms():
    rooms = []          # All centers of the rooms
    temp = []           # Used for filling the map and holding the tiles
    fullMap = []

    # Create an empty map
    for i in range(MAP_HEIGHT):
        for j in range(MAP_WIDTH):
            temp.append(False)
        fullMap.append(temp[:])
        temp[:] = []

    # Create rooms randomly for each room
    for non in range(MAX_ROOMS):
        createRoom(fullMap, rooms, randint(0, MAP_WIDTH), randint(0, MAP_HEIGHT))

    createHalls(fullMap, sorted(rooms, key=lambda x: (x[1] + x[0])))

    # Create tiles
    for i in range(MAP_WIDTH):
        for j in range(MAP_HEIGHT):
            if fullMap[i][j]:
                temp.append(tile(i, j))

    return temp


def createRoom(fullMap, rooms, x, y):
    size = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)            # Size of room
    start = [x - floor((size / 2)), y - floor((size / 2))]  # Center of room

    # If room is out of map
    if x - size < 0 or y - size < 0 or x + size > MAP_WIDTH or y + size > MAP_HEIGHT:
        return False

    # If room intersects with another room
    for i in range(size):
        for j in range(size):
            if fullMap[start[0] + i][start[1] + j]:
                return False

    # Create room
    for i in range(1, size - 1):
        for j in range(1, size - 1):
            fullMap[start[0] + i][start[1] + j] = True
    rooms.append([x, y])

    return True


def createHalls(fullMap, rooms):
    for i in range(len(rooms) - 1):
        # Fixed X and Y corrdinates
        temp1 = max(rooms[i][1], rooms[i + 1][1])
        temp2 = rooms[i][0] if min(rooms[i][1], rooms[i + 1][1]) == rooms[i][1] else rooms[i + 1][0]

        # Alternate between creating horizzonal and vertical hallways
        if 1 % 2 == 0:
            temp1, temp2 = temp1, temp2

        # Connect the rooms horizontally
        for j in range(min(rooms[i][0], rooms[i + 1][0]), max(rooms[i][0], rooms[i + 1][0]) + 1):
            fullMap[j][temp1] = True

        # Connect the rooms vertically
        for j in range(min(rooms[i][1], rooms[i + 1][1]), max(rooms[i][1], rooms[i + 1][1])):
            fullMap[temp2][j] = True
