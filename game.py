from math import floor
from random import randint

import pygame as game

import camera
import entity
import input
import map
import enemy
from parameters import TILE_WIDTH, TILE_HEIGHT, MAP_HEIGHT, MAP_WIDTH, ENEMY_NUM

game.init()
screen = game.display.set_mode((720, 480))
clock = game.time.Clock()

roomMap = map.Map()
roomMap.generateMap(MAP_WIDTH, MAP_HEIGHT)
level = roomMap.level

# Create player
player = entity.player((roomMap.rooms[0].x1 + 2) * TILE_WIDTH, (roomMap.rooms[0].y1 + 2) * TILE_HEIGHT)
follow = camera.centerScreen(player)

enemies = []
for non in range(ENEMY_NUM):
    temp = randint(1, len(roomMap.rooms) - 1)
    enemy.ghost((roomMap.rooms[temp].x1 + 2) * TILE_WIDTH, (roomMap.rooms[temp].y1 + 2) * TILE_HEIGHT, enemies, player)


while input.inputHandler():
    screen.fill((0, 0, 0))
    for y in range(max(0, floor(player.y / TILE_HEIGHT - 5)), min(MAP_WIDTH, floor(player.y / TILE_HEIGHT + 6))):
        for x in range(max(0, floor(player.x / TILE_WIDTH - 6)), min(MAP_WIDTH, floor(player.x / TILE_WIDTH + 7))):
            if level[x][y] == 0:
                game.draw.rect(screen,
                               (255, 255, 255),
                               (x * TILE_WIDTH - follow.x, y * TILE_HEIGHT - follow.y,
                                TILE_WIDTH, TILE_HEIGHT))
    player.update(level)
    follow.update()
    player.draw(screen, follow)
    for i in enemies:
        i.update(level)
        i.draw(screen, follow)
    game.display.update()
    clock.tick(60)

game.quit()
