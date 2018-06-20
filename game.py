import pygame

import graphics
import entity
import os
import events
import map
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH
import camera
import input

pygame.init()
clock = pygame.time.Clock()

# Initialize screen size, Tuples are important
graphics.init((640, 640))

# Load background
bg = ["assets", "img", "space.png"]
graphics.background = graphics.load(os.path.join(*bg))

# map that stores tiles
# TODO: get this to actually work, this is what we should be using, not just drawing rectangles
# TODO: check to see if TILE_WIDTH and TILE_HEIGHT are in the right order
roomMap = map.Map()
roomMap.generateMap(MAP_WIDTH, MAP_HEIGHT)

# Create player
player = entity.player((roomMap.rooms[0].x1+1) * TILE_WIDTH, (roomMap.rooms[0].y1+2) * TILE_HEIGHT)
follow = camera.centerScreen(player)

# Handle exiting
def quit(e):
    global run
    run = False


events.register(pygame.QUIT, quit)

# GAME LOOP

while not input.controls.quit:
    # EVENT HANDLING
    input.inputHandler()

    # GAME PHYSICS
    player.update()
    follow.update()

    # RENDERING
    graphics.render(roomMap, player, follow)
    clock.tick(60)

pygame.quit()
