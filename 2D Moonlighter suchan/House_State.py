import random
import json
import os

from pico2d import *
import game_framework
import game_world
import LoadingState

from will import Boy
from house import House
from house_door import House_door






name = "HouseState"

boy = None
village = None
house_door = None
house = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)


    global house
    house = House()
    game_world.add_object(house,0)

    global house_door
    house_door = House_door()
    game_world.add_object(house_door, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(boy, house_door):
        game_framework.change_state(LoadingState)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
