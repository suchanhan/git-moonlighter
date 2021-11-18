from pico2d import *

class House:
    def __init__(self):
        self.image = load_image('House.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 360)