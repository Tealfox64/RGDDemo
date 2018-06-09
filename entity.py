import graphics
import os


class Entity(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None


# George is an Entity type (not required to do is-a)
class George(Entity):
    # WARNING, CLASS-LEVEL VARIABLE
    # Split sprite sheet coordinates (192 x 192 file), (48 x 48 ind)
    frames = {
        "up": [(2 * 48, y * 48, 48, 48)
               for y in range(4)],
        "down": [(0 * 48, y * 48, 48, 48)
                 for y in range(4)],
        "left": [(1 * 48, y * 48, 48, 48)
                 for y in range(4)],
        "right": [(3 * 48, y * 48, 48, 48)
                  for y in range(4)],
    }

    def __init__(self):
        # To call the parent's default constructor, you must do it manually:
        super(George, self).__init__()
        # Load the George sprite sheet
        path = ["assets", "img", "george.png"]
        # ***better to create a sprite object with sprite sheet and frame variable
        self.sprite = graphics.load(os.path.join(*path))
        # What position (frame) is he in?
        self.frame = self.frames["down"][0]
        self.frame_num = 0
        self.facing = "down"

    def update(self):
        # pygame.time.Clock to handle delays
        self.frame_num = (self.frame_num + 1) % 4
        self.frame = self.frames[self.facing][self.frame_num]

