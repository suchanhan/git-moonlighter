from pico2d import *

class BossMap:
    def __init__(self):
        self.image = load_image('Bossroom.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 360)