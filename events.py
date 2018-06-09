from random import randint

import pygame


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

        # TODO: Fix the intersect detection
        failed = False
        for otherRoom in rooms:
            if newRoom.intersects(otherRoom):
                failed = True
                break


        if not failed:
            # TODO: create the rooms
            # createRoom(newRoom)
            rooms.append(newRoom)
