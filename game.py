import pygame

import graphics
import entity
import os
import events
import room
from parameters import TILE_WIDTH, TILE_HEIGHT

pygame.init()

# Initialize screen size, Tuples are important
graphics.init((640, 640))

# Load background
bg = ["assets", "img", "space.png"]
graphics.background = graphics.load(os.path.join(*bg))

# Load sprite
george = entity.George()
graphics.add(george)

# TODO: Verify that rooms list actually goes here
rooms = []
events.placeRooms(rooms)


# Handle exiting
def quit(e):
    global run
    run = False


events.register(pygame.QUIT, quit)

# GAME LOOP

run = True
while run:
    # EVENT HANDLING
    events.update()

    # GAME PHYSICS
    george.update()

    # RENDERING
    graphics.render()
    for r in rooms:
        graphics.drawRoomOutline(r.x, r.y, r.w * TILE_WIDTH, r.h * TILE_HEIGHT)

pygame.quit()
