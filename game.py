import pygame

import graphics
import entity
import os
import events
import map
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH

pygame.init()

# Initialize screen size, Tuples are important
graphics.init((640, 640))

# Load background
bg = ["assets", "img", "space.png"]
graphics.background = graphics.load(os.path.join(*bg))

# Load sprite
george = entity.George()
graphics.add(george)

# map that stores tiles
# TODO: get this to actually work, this is what we should be using, not just drawing rectangles
# TODO: check to see if TILE_WIDTH and TILE_HEIGHT are in the right order
roomMap = map.Map()
roomMap.generateMap(MAP_WIDTH, MAP_HEIGHT)

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
    graphics.render(roomMap)

pygame.quit()
