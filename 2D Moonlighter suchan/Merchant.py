import game_framework
from pico2d import *
import random
# from ball import Ball

import game_world

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 /0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP, SLEEP_TIMER, SPACE = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP
}


# Boy States

class IdleState:

    def enter(golem, event):


        golem.timer = 1000

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    def do(golem):
        golem.frameRL = (golem.frameRL + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        golem.frameUD = (golem.frameUD + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        golem.timer -= 1
        if golem.timer == 0:
            golem.add_event(SLEEP_TIMER)

    def draw(golem):


            golem.MerchantIdle.clip_draw(int(golem.frameRL) * 31, 0, 31, 45, golem.x, golem.y, 100, 100)


         # else:
         #    golem.GolemIdle.clip_draw(int(golem.frameRL) * 89, 230, 89, 115, golem.x, golem.y)

            #     golem.Idleimage.clip_draw(int(golem.frameUD) * 80, 0, 80, 100, golem.x, golem.y, 60,60)
            # else:
            #     golem.Idleimage.clip_draw(int(golem.frameUD) * 80, 100, 80, 100, golem.x, golem.y, 60,60)


class RunState:

    def enter(golem, event):
        # golem.dirRL = clamp(-1, golem.x, 1)

        # if event == RIGHT_DOWN:
        #     boy.velocityX += RUN_SPEED_PPS
        #     boy.TransChange = True
        # elif event == LEFT_DOWN:
        #     boy.velocityX -= RUN_SPEED_PPS
        #     boy.TransChange = True
        # elif event == RIGHT_UP:
        #     boy.velocityX -= RUN_SPEED_PPS
        #     boy.TransChange = True
        # elif event == LEFT_UP:
        #     boy.velocityX += RUN_SPEED_PPS
        #     boy.TransChange = True
        # elif event == UP_DOWN:
        #     boy.velocityY += RUN_SPEED_PPS
        #     boy.TransChange = False
        # elif event == DOWN_DOWN:
        #     boy.velocityY -= RUN_SPEED_PPS
        #     boy.TransChange = False
        # elif event == UP_UP:
        #     boy.velocityY -= RUN_SPEED_PPS
        #     boy.TransChange = False
        # elif event == DOWN_UP:
        #     boy.velocityY += RUN_SPEED_PPS
        #     boy.TransChange = False
        #
        # boy.dirRL = clamp(-1, boy.velocityX, 1)
        # boy.dirUD = clamp(-1, boy.velocityY, 1)
        #
        pass

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    def do(golem):

        golem.frameRL = (golem.frameRL + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        golem.frameUD = (golem.frameUD + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        golem.x += golem.velocityX * game_framework.frame_time
        golem.x = clamp(25, golem.x, 1600 - 25)

        golem.y += golem.velocityY * game_framework.frame_time
        golem.y = clamp(0, golem.y, 900)


    def draw(golem):
        if golem.TransChange == True:
         if golem.dirRL == 1:
            golem.RunimageLR.clip_draw(int(golem.frameRL) * 35, 0, 35, 40, golem.x, golem.y, 60,60)
         else:
            golem.RunimageLR.clip_draw(int(golem.frameRL) * 35, 40 ,35, 40, golem.x,golem.y, 60,60)
        elif golem.TransChange == False:
         if golem.dirUD == 1:
            golem.RunimageUD.clip_draw(int(golem.frameUD) * 23, 0, 23, 37, golem.x, golem.y, 60,60)
         else:
             golem.RunimageUD.clip_draw(int(golem.frameUD) * 23, 37 ,23, 37,golem.x, golem.y, 60,60)


# class SleepState:
#
#     def enter(boy, event):
#         boy.frame = 0
#
#     def exit(boy, event):
#         pass
#
#     def do(boy):
#         boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#
#     def draw(boy):
#         if boy.dir == 1:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
#         else:
#             boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)






# next_state_table = {
#     IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
#                 UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, SPACE: IdleState},
#     RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
#                UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, SPACE: RunState},
#
#     # SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
# }

class Merchant:

    def __init__(self):
        self.x = 600
        self.y = 500

        # Boy is only once created, so instance image loading is fine
        self.RunimageLR = load_image('will_leftright.png')
        self.RunimageUD = load_image('will_frontback.png')
        self.MerchantIdle = load_image('Merchant_idle.png')
        self.dirRL = 1
        self.dirUD = 1
        self.TransChange = True
        self.velocityX = 0
        self.velocityY = 0
        self.frameRL = 0
        self.frameUD = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        # ball = Ball(self.x, self.y, self.dir*3)
        # game_world.add_object(ball, 1)
        pass


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            # self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

