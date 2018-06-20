from random import randint

import pygame

import entity
import events
import input
import camera
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_WIDTH, MAP_HEIGHT

# Set up pygame
pygame.init()                                       # initialize all imported pygame modules
gameDisplay = pygame.display.set_mode((720, 480))   # create game display
clock = pygame.time.Clock()

# Load game objects
tiles = events.placeRooms()                         # Add rooms
temp = tiles[randint(0, len(tiles))]
player = entity.player(temp.x + 8, temp.y + 8)      # Add player to list of objects
follow = camera.centerScreen(player)

# GAME LOOP
while not input.controls.quit:
    gameDisplay.fill((0, 0, 0))                     # Clear screen every frame

    input.inputHandler()                            # Check for user input

    for i in tiles:
        pygame.draw.rect(gameDisplay, (50, 255, 50), [i.x - follow.x, i.y - follow.y, TILE_WIDTH, TILE_HEIGHT])

    player.update(tiles)                            # Update the player
    follow.update()
    pygame.draw.rect(gameDisplay, (255, 255, 255), [player.x - follow.x, player.y - follow.y, 16, 16])

    pygame.display.update()                         # update display every frame
    clock.tick(60)                                  # Set frame rate to 60 frames per second

pygame.quit()
