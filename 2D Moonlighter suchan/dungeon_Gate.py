from pico2d import *

class Dungeon_Gate:
    def __init__(self):
        self.image = load_image('Dungeon_Gate.png')
        self.x = 800
        self.y = 650

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 150, 120)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10