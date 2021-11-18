from pico2d import *

class DungeonMap1:
    def __init__(self):
        self.image = load_image('DungeonMapfrist.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(640, 360)



