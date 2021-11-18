from pico2d import *

class Loading:
    def __init__(self):
        self.image = load_image('RoadingImage.png')
        self.x = 640
        self.y = 360
    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

