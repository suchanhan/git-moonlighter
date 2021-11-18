import game_framework
import pico2d

import main_state
import Village_State
import  House_State

pico2d.open_canvas(1280, 720)
game_framework.run(House_State)
pico2d.close_canvas()