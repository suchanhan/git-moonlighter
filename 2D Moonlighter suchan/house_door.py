from pico2d import *

class House_door:
    def __init__(self):
        self.image = load_image('house_door.png')
        self.x = 800
        self.y = 90
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10