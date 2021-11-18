from pico2d import *

class Potal:
    def __init__(self):
        self.image = load_image('FirstDungeondoor.png')
        self.x = 640
        self.y = 650
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y, 100, 80)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
