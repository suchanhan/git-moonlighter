import random
import json
import os

from pico2d import *
import game_framework
import game_world
import BossMap_State
import main_state
import Village_State

from LoadingImage import Loading







name = "LoadingState"


loading = None


def enter():
    global loading
    loading = Loading()
    game_world.add_object(loading, 0)



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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
                game_framework.change_state(BossMap_State)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_d:
                game_framework.change_state(main_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
                game_framework.change_state(Village_State)



def update():
    for game_object in game_world.all_objects():
        game_object.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






