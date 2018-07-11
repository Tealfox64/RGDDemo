from math import floor
from random import randint

import pygame as game

import camera, entity, input, enemy, sound, light, events
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH, ENEMY_NUM

# Load game essentials
game.init()
game.font.init()
screen = game.display.set_mode((720, 480))
clock = game.time.Clock()
game.display.set_caption("Duno")
quit = False

count = 1                                               # Floor count
timer = 0

# Load game staples
tile = game.image.load("floorTile.png")                 # Tile image
stairs = game.image.load("stairs.png")                  # Tile image
lighting = light.light()                                # Black image to cover the screen
everything = []                                         # Holds all enemies, dust, and explosions
font = game.font.SysFont("Comic Sans MS", 30)
text = font.render("Floor " + str(count), False, (255, 255, 255))
message = None

# Start playing music at the beginning of the game
sound.song.play(-1)
sound.song.fadeout(200000)
sound.scary.play(-1, fade_ms=200000)

level, rooms = events.placeRooms()          # Create all of the tiles
player = entity.player((rooms[0][0]) * TILE_WIDTH, (rooms[0][1]) * TILE_HEIGHT, everything)
follow = camera.centerScreen(player)
everything[:] = []

# Randomly create enemies
for room in range(1, len(rooms)):
    if randint(0, 1) == 0:
        enemy.ghost((rooms[room][0]) * TILE_WIDTH,
                    (rooms[room][1]) * TILE_HEIGHT, everything, player, lighting)

# Game loop
while input.inputHandler() and not quit:
    if not quit:
        screen.fill((0, 0, 0))

    # Draw every tile and the stairs
    for y in range(max(0, floor(player.y / TILE_HEIGHT - 5)), min(MAP_WIDTH, floor(player.y / TILE_HEIGHT + 6))):
        for x in range(max(0, floor(player.x / TILE_WIDTH - 6)), min(MAP_WIDTH, floor(player.x / TILE_WIDTH + 7))):
            if level[x][y] != 0:                        # 1 represents tiles
                screen.blit(tile, (x * 64 - follow.x, y * 64 - follow.y))
            if level[x][y] == 2:                        # 2 represents stairs
                screen.blit(stairs, (x * 64 - follow.x + 16, y * 64 - follow.y + 16))

    # Update and draw all enemies, dust, and explosions
    for i in everything:
        i.update(level)
        i.draw(screen, follow)

    screen.blit(lighting.image, (0, 0))                 # Draw darkness

    # Update and draw player
    player.update(level)
    follow.update()                                     # Update camera
    player.draw(screen, follow)

    if level[floor(player.x / TILE_WIDTH)][floor((player.y - 1) / TILE_HEIGHT)] == 2:
        count += 1
        text = font.render("Floor " + str(count), False, (255, 255, 255))

        level, rooms = events.placeRooms()  # Create all of the tiles
        player.x = rooms[0][0] * TILE_WIDTH
        player.y = rooms[0][1] * TILE_HEIGHT
        follow = camera.centerScreen(player)
        everything[:] = []

        # Randomly create enemies
        for room in range(1, len(rooms)):
            if randint(0, 1) == 0:
                enemy.ghost((rooms[room][0]) * TILE_WIDTH,
                            (rooms[room][1]) * TILE_HEIGHT, everything, player, lighting)

    screen.blit(text, (600, 0))

    if 125 < lighting.alpha < 130:
        message = font.render("Something is watching you!", False, (0, 0, 0))
        game.draw.rect(screen, (255, 255, 255), (8, 400, 420, 54))
        screen.blit(message, (8, 400))

    if 149.9 < lighting.alpha < 150 or 180 < lighting.alpha < 181:
        sound.scream.play(0)

    if 170 < lighting.alpha < 170.1:
        sound.distantScream.play(0)

    if 200 < lighting.alpha < 205:
        if randint(0, 1) == 0:
            message = font.render("ít's cAtchíng upp!", False, (0, 0, 0))
        else:
            message = font.render("ít's Catchíng up!", False, (0, 0, 0))
        game.draw.rect(screen, (255, 255, 255), (8, 400, 420, 54))
        screen.blit(message, (8, 400))

    if 200 < lighting.alpha < 205:
        if randint(0, 1) == 0:
            message = font.render("ít's cAtchíng upp!", False, (0, 0, 0))
        else:
            message = font.render("ít's Catchíng up!", False, (0, 0, 0))
        game.draw.rect(screen, (255, 255, 255), (8, 400, 420, 54))
        screen.blit(message, (8, 400))

    if player.health == 0:
        player.health = 2
        player.x = rooms[0][0] * TILE_WIDTH
        player.y = rooms[0][1] * TILE_HEIGHT

    if 225 < lighting.alpha:
        quit = True

    game.display.update()                               # Update entire display
    clock.tick(60)                                      # 60 FPS
    lighting.changeTransparency(0.01)                   # Make screen slightly darker with every game loop

    if 125 <= lighting.alpha:
        game.display.set_caption("gamèòvèrr")
        if 175 <= lighting.alpha:
            if randint(0, 1) == 0:
                game.display.set_caption("Yòu hAvè díèD")
            else:
                game.display.set_caption("YòuuhAvèdíèD")

timer = 500

while 0 <= timer:
    message = font.render("Game successfully deleted.", False, (0, 0, 0))
    game.draw.rect(screen, (255, 255, 255), (8, 200, 420, 54))
    screen.blit(message, (8, 200))
    timer -= 1
    game.display.update()                               # Update entire display
    clock.tick(60)                                      # 60 FPS

game.quit()
