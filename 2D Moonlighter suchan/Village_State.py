import random
import json
import os

from pico2d import *
import game_framework
import game_world
import LoadingState

from will import Boy
from village import Village
from dungeon_Gate import Dungeon_Gate
from merchant import  Merchant






name = "MainState"

boy = None
village = None
dungeon_Gate = None
merchant = None

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


    global village
    village = Village()
    game_world.add_object(village, 0)

    global dungeon_Gate
    dungeon_Gate = Dungeon_Gate()
    game_world.add_object(dungeon_Gate,1)

    global merchant
    merchant = Merchant()
    game_world.add_object(merchant, 1)


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
    if collide(boy, dungeon_Gate):
        game_framework.change_state(LoadingState)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
