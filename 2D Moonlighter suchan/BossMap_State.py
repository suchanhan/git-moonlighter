from pico2d import *
import game_framework
import game_world

from will import Boy
from bossMap import BossMap
from Boss1 import Boss





name = "MainState"

boy = None
bossMap = None
boss = None

def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global bossMap
    bossMap = BossMap()
    game_world.add_object(bossMap, 0)

    global golem
    golem = Boss()
    game_world.add_object(golem, 1)


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
    # fill here


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
