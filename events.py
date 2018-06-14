from random import randint

import pygame
import math

from parameters import MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAP_WIDTH, MAP_HEIGHT
from room import Room

listeners = {
    pygame.QUIT: [],
}


def register(type, handler):
    global listeners
    if handler not in listeners[type]:
        listeners[type].append(handler)


def update():
    global listeners
    for e in pygame.event.get():
        if e.type in listeners:
            for l in listeners[e.type]:
                l(e.type)


# pygame.event.get()
# get events from the queue
# get() -> Eventlist
# get(type) -> Eventlist
# get(typelist) -> Eventlist
# This will get all the messages and remove them from the queue.
# If a type or sequence of types is given only those messages will be removed from the queue.
#
# If you are only taking specific events from the queue,
# be aware that the queue could eventually fill up with the events you are not interested.

# TODO: We may need to put this somewhere else
# TODO: ASK TEACHER HOW TO PASS THIS BY REFERENCE TO GO FASTER
def placeRooms(rooms):
    # create room storage array
    # clear the old room
    rooms[:] = []

    # create random for each room
    for r in range(MAX_ROOMS):
        # width and height between max and min room sizes
        w = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)
        h = randint(MIN_ROOM_SIZE, MAX_ROOM_SIZE)

        # x and y coordinates where room won't go past 1 tile border around map
        x = randint(1, MAP_WIDTH - w - 1)
        y = randint(1, MAP_HEIGHT - h - 1)

        newRoom = Room(x, y, w, h)

        # TODO: Fix the intersect detection... unless we want to keep it
        failed = False
        for otherRoom in rooms:
            if newRoom.intersects(otherRoom):
                failed = True
                break

        if not failed:
            # TODO: Create this function to actually carve out the rooms into the map
            # createRoom(newRoom)

            newCenter = newRoom.center

            if rooms.length != 0:
                # store center of previous room
                prevCenter = rooms[rooms.length - 1].center

                # carve out corridors between rooms based on centers
                # randomly start with horizontal or vertical corridors
                if randint(2) == 1:
                    hCorridor(int(prevCenter.x), int(newCenter.x), int(prevCenter.y))
                    vCorridor(int(prevCenter.y), int(newCenter.y), int(prevCenter.x))
                else:
                    vCorridor(int(prevCenter.y), int(newCenter.y), int(prevCenter.x))
                    hCorridor(int(prevCenter.x), int(newCenter.x), int(prevCenter.y))

        if not failed:
            rooms.append(newRoom)


# TODO: GET THESE CORRIDOR FUNCTIONS DONE
def hCorridor(x1, x2, y):
    x1 = int(x1)
    x2 = int(x2)
    # TODO: This loop should remove carved tiles from our map
    for x in range(int(math.min(x1, x2)), (int(math.max(x1, x2)) + 1)):
        # TODO: Create the function that actually removes the tile from the map.
        # Probably isn't going to be exactly this function call from the website:
        map[x][y].parent.removeChild(map[x][y])

        # TODO: This uses the constructor for the Tile class
        # place a new unblocked tile (based off of website function call):
        # cannot call "new" in python
        # map[x][y] = new Tile(Tile.DARK_GROUND, false, false)

        # TODO: Figure out what the heck this thing means
        # add tile as a new game object
        # addChild(map[x][y])

        # TODO: implement this method into the Tile class
        # set the location of the tile appropriately
        # map[x][y].setLoc(x, y)


def vCorridor(y1, y2, x):
    x1 = int(y1)
    x2 = int(y2)
    # TODO: This loop should remove carved tiles from our map
    for y in range(int(math.min(y1, y2)), (int(math.max(y1, y2)) + 1)):
        # TODO: Create the function that actually removes the tile from the map.
        # Probably isn't going to be exactly this function call from the website:
        map[x][y].parent.removeChild(map[x][y])

        # TODO: This uses the constructor for the Tile class
        # place a new unblocked tile (based off of website function call):
        # cannot call "new" in python
        # map[x][y] = new Tile(Tile.DARK_GROUND, false, false)

        # TODO: Figure out what the heck this thing means
        # add tile as a new game object
        # addChild(map[x][y])

        # TODO: implement this method into the Tile class
        # set the location of the tile appropriately
        # map[x][y].setLoc(x, y)
