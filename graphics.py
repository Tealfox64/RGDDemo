import pygame
import map
from parameters import MAP_HEIGHT, MAP_WIDTH, TILE_HEIGHT, TILE_WIDTH

# import pygame.image
# from game import rooms

resolution = None
screen = None
background = None
sprites = []
images = {}  # empty dictionary


floorimage = pygame.image.load(("assets/img/floorTile01.png"))




def init(res):
    global resolution, screen
    resolution = res

    # pygame.display.set_mode()
    # Initialize a window or screen for display
    # set_mode(resolution=(0,0), flags=0, depth=0) -> Surface
    # The flags argument controls which type of display you want.
    # There are several to choose from, and you can even combine multiple types using the bitwise or operator,
    # (the pipe "|" character). If you pass 0 or no flags argument it will default to a software driven window.
    # Here are the display flags you will want to choose from:
    #
    # pygame.FULLSCREEN    create a fullscreen display
    # pygame.DOUBLEBUF     recommended for HWSURFACE or OPENGL
    # pygame.HWSURFACE     hardware accelerated, only in FULLSCREEN
    # pygame.OPENGL        create an OpenGL-renderable display
    # pygame.RESIZABLE     display window should be sizeable
    # pygame.NOFRAME       display window will have no border or controls

    screen = pygame.display.set_mode(res)


def add(sprite):
    global sprites
    if sprite not in sprites:
        sprites.append(sprite)


def remove(sprite):
    global sprites
    if sprite in sprites:
        sprites.remove(sprite)


def render(roomMap, player, follow):
    # blit()
    # draw one image onto another
    # blit(source, dest, area=None, special_flags = 0) -> Rect
    # Draws a source Surface onto this Surface.
    # The draw can be positioned with the dest argument.
    # Dest can either be pair of coordinates representing the upper left corner of the source.
    # A Rect can also be passed as the destination and the topleft corner
    # of the rectangle will be used as the position for the blit.
    # The size of the destination rectangle does not effect the blit.
    #
    # An optional area rectangle can be passed as well. This represents a smaller portion of the source Surface to draw.
    #
    global screen, background
    screen.fill((0, 0, 0))

    # before sprites, to be behind sprites
    # screen.blit(background, (0, 0))

    # DRAW ROOMS HERE
    for y in range(MAP_HEIGHT):
        for x in range(MAP_WIDTH):
            if roomMap.level[x][y] == 0:
                drawFloorTile(x * TILE_WIDTH - follow.x, y * TILE_HEIGHT - follow.y, floorimage, TILE_WIDTH, TILE_HEIGHT)

    # DRAW PLAYER HERE
    pygame.draw.rect(screen, (0, 0, 255), [player.x - follow.x, player.y - follow.y, 16, 16])

    for sprite in sprites:
        screen.blit(sprite.sprite, (sprite.x, sprite.y), sprite.frame)

    pygame.display.flip()


def drawFloorTile(x, y, image, w, h):
    # pygame.draw.rect(screen, (255, 255, 255), [x, y, w, h])
    screen.blit(image, (x, y))


def drawBlackTile(x, y, w, h):
        pygame.draw.rect(screen, (0, 0, 0), [x, y, w, h])


def load(path):
    global images
    if path in images:
        return images[path]  # if image is already loaded, just return it
    else:
        images[path] = pygame.image.load(path)
        return images[path]
