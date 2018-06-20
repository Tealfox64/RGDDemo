import input


class player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        if input.controls.downPressed:
            self.y += 2
        if input.controls.upPressed:
            self.y -= 2
        if input.controls.leftPressed:
            self.x -= 2
        if input.controls.rightPressed:
            self.x += 2