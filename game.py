from math import floor
from random import randint

import pygame as game

import camera
import entity
import input
import map
import enemy
import sound
import light
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH, ENEMY_NUM

game.init()
screen = game.display.set_mode((720, 480))
clock = game.time.Clock()
tile = game.image.load("assets/img/floorTile01.png")

roomMap = map.Map()
roomMap.generateMap(MAP_WIDTH, MAP_HEIGHT)
level = roomMap.level

# Create player
player = entity.player((roomMap.rooms[0].x1 + 2) * TILE_WIDTH, (roomMap.rooms[0].y1 + 2) * TILE_HEIGHT)
follow = camera.centerScreen(player)

lighting = light.light()
enemies = []
for non in range(ENEMY_NUM):
    temp = randint(1, len(roomMap.rooms) - 1)
    enemy.ghost((roomMap.rooms[temp].x1 + 2) * TILE_WIDTH,
                (roomMap.rooms[temp].y1 + 2) * TILE_HEIGHT, enemies, player, lighting)

sound.song.play(-1)                                # Play music in an infinite loop
while input.inputHandler():
    screen.fill((0, 0, 0))
    for y in range(max(0, floor(player.y / TILE_HEIGHT - 5)), min(MAP_WIDTH, floor(player.y / TILE_HEIGHT + 6))):
        for x in range(max(0, floor(player.x / TILE_WIDTH - 6)), min(MAP_WIDTH, floor(player.x / TILE_WIDTH + 7))):
            if level[x][y] == 0:
                screen.blit(tile, (x * 64 - follow.x, y * 64 - follow.y))
    player.update(level)
    follow.update()
    for i in enemies:
        i.update(level)
        i.draw(screen, follow)
    screen.blit(lighting.image, (0, 0))
    player.draw(screen, follow)
    game.display.update()
    clock.tick(60)
    lighting.changeTransparency(0.01)

game.quit()
