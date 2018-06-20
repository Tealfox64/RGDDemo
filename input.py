import pygame


class controls:
    upPressed, leftPressed, rightPressed, downPressed, quit = (False,) * 5


def inputHandler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            controls.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                controls.upPressed = True
            elif event.key == pygame.K_a:
                controls.leftPressed = True
            elif event.key == pygame.K_d:
                controls.rightPressed = True
            elif event.key == pygame.K_s:
                controls.downPressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                controls.upPressed = False
            elif event.key == pygame.K_a:
                controls.leftPressed = False
            elif event.key == pygame.K_d:
                controls.rightPressed = False
            elif event.key == pygame.K_s:
                controls.downPressed = False