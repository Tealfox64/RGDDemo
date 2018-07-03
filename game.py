from random import randint
import pygame as game
import entity
import events
import input
import camera
from parameters import TILE_WIDTH, TILE_HEIGHT, resolution

# Set up py-game
game.init()                                         # Initialize all imported py-game modules
resolution.res = [game.display.Info().current_w, game.display.Info().current_h]
game.mouse.set_cursor((8, 8), (0, 0), (0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0))
screen = game.display.set_mode(resolution.res, game.FULLSCREEN)         # Create game display
clock = game.time.Clock()

# Load game objects
tiles = events.placeRooms()                         # Add rooms
temp = tiles[randint(0, len(tiles))]
player = entity.player(temp)                        # Add player to list of objects
follow = camera.centerScreen(player)

# Handle exiting
def quit(e):
    global run
    run = False



# GAME LOOP
while not input.controls.quit:
    screen.fill((0, 0, 0))                          # Clear screen every frame

    input.inputHandler()                            # Check for user input

    for i in tiles:
        if 0 <= i.x - follow.x + TILE_WIDTH <= resolution.res[0] + TILE_WIDTH:
            if 0 <= i.y - follow.y + TILE_HEIGHT <= resolution.res[1] + TILE_HEIGHT:
                game.draw.rect(screen, (50, 255, 50), [i.x - follow.x, i.y - follow.y, TILE_WIDTH, TILE_HEIGHT])

    player.update(tiles)                            # Update the player
    follow.update()
    game.draw.rect(screen, (255, 255, 255), [player.x - follow.x, player.y - follow.y, TILE_WIDTH, TILE_HEIGHT])

    game.display.update()                           # Update display every frame
    clock.tick(60)                                  # Set frame rate to 60 frames per second

game.quit()
