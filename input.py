import pygame


class controls:
    upPressed, leftPressed, rightPressed, downPressed, spacePressed = (False,) * 5


def inputHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                controls.upPressed = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                controls.leftPressed = True
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                controls.rightPressed = True
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                controls.downPressed = True
            elif event.key == pygame.K_SPACE:
                controls.spacePressed = True
            elif event.key == pygame.K_ESCAPE:
                return False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                controls.upPressed = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                controls.leftPressed = False
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                controls.rightPressed = False
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                controls.downPressed = False
            elif event.key == pygame.K_SPACE:
                controls.spacePressed = False
    return True
