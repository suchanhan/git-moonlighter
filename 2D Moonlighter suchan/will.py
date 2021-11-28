import game_framework
from pico2d import *
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
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN, DOWN_DOWN, UP_UP, DOWN_UP, ATTACK_DOWN, ATTACK_UP = range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_UP,
    (SDL_KEYDOWN, SDLK_a): ATTACK_DOWN,
    (SDL_KEYUP, SDLK_a): ATTACK_UP,
}


# Boy States

class IdleState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityX += RUN_SPEED_PPS
            boy.TransChange = True
        elif event == LEFT_DOWN:
            boy.velocityX -= RUN_SPEED_PPS
            boy.TransChange == True
        elif event == RIGHT_UP:
            boy.velocityX -= RUN_SPEED_PPS
            boy.TransChange == True
        elif event == LEFT_UP:
            boy.velocityX += RUN_SPEED_PPS
            boy.TransChange == True
        elif event == UP_DOWN:
            boy.velocityY += RUN_SPEED_PPS
            boy.TransChange == False
        elif event == DOWN_DOWN:
            boy.velocityY -= RUN_SPEED_PPS
            boy.TransChange == False
        elif event == UP_UP:
            boy.velocityY -= RUN_SPEED_PPS
            boy.TransChange == False
        elif event == DOWN_UP:
            boy.velocityY += RUN_SPEED_PPS
            boy.TransChange == False

        boy.timer = 1000

    def exit(boy, event):

        pass

    def do(boy):
        boy.frameRL = (boy.frameRL + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.frameUD = (boy.frameUD + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8



    def draw(boy):
        if boy.TransChange == True:
         if boy.dirRL == 1:
            boy.Idleimage.clip_draw(int(boy.frameRL) * 80, 302, 80, 100, boy.x, boy.y,60,60)
         else:
            boy.Idleimage.clip_draw(int(boy.frameRL) * 80, 202, 80, 100, boy.x, boy.y,60,60)
        elif boy.TransChange == False:
            if boy.dirUD == 1:
                boy.Idleimage.clip_draw(int(boy.frameUD) * 80, 0, 80, 100, boy.x, boy.y, 60,60)
            else:
                boy.Idleimage.clip_draw(int(boy.frameUD) * 80, 102, 80, 100, boy.x, boy.y, 60,60)


class RunState:

    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocityX += RUN_SPEED_PPS
            boy.TransChange = True
        elif event == LEFT_DOWN:
            boy.velocityX -= RUN_SPEED_PPS
            boy.TransChange = True
        elif event == RIGHT_UP:
            boy.velocityX -= RUN_SPEED_PPS
            boy.TransChange = True
        elif event == LEFT_UP:
            boy.velocityX += RUN_SPEED_PPS
            boy.TransChange = True
        elif event == UP_DOWN:
            boy.velocityY += RUN_SPEED_PPS
            boy.TransChange = False
        elif event == DOWN_DOWN:
            boy.velocityY -= RUN_SPEED_PPS
            boy.TransChange = False
        elif event == UP_UP:
            boy.velocityY -= RUN_SPEED_PPS
            boy.TransChange = False
        elif event == DOWN_UP:
            boy.velocityY += RUN_SPEED_PPS
            boy.TransChange = False

        boy.dirRL = clamp(-1, boy.velocityX, 1)
        boy.dirUD = clamp(-1, boy.velocityY, 1)


    def exit(boy, event):
        boy.exit()
        pass

    def do(boy):

        boy.frameRL = (boy.frameRL + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.frameUD = (boy.frameUD + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocityX * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

        boy.y += boy.velocityY * game_framework.frame_time
        boy.y = clamp(0, boy.y, 900)


    def draw(boy):
        if boy.TransChange == True:
         if boy.dirRL == 1:
            boy.RunimageLR.clip_draw(int(boy.frameRL) * 35, 0, 35, 40, boy.x, boy.y, 60,60)
         else:
            boy.RunimageLR.clip_draw(int(boy.frameRL) * 35, 40 ,35, 40, boy.x, boy.y, 60,60)
        elif boy.TransChange == False:
         if boy.dirUD == 1:
            boy.RunimageUD.clip_draw(int(boy.frameUD) * 23, 0, 23, 37, boy.x, boy.y, 60,60)
         else:
            boy.RunimageUD.clip_draw(int(boy.frameUD) * 23, 37 ,23, 37, boy.x, boy.y, 60,60)


class SleepState:

    def enter(boy, event):
        if event == ATTACK_DOWN:
            boy.bow -= 1
        elif event == ATTACK_UP:
            boy.bow += 1


    def exit(boy, event):
        pass

    def do(boy):
        boy.bowframe = (boy.bowframe + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        boy.bowframe += boy.bow * game_framework.frame_time

    def draw(boy):
            boy.dirRL == 1

            boy.Bowimage.clip_draw(int(boy.bowframe) * 34, 126, 34, 126, boy.x, boy.y, 60, 60)







next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                UP_UP: RunState, DOWN_UP: RunState, UP_DOWN: RunState, DOWN_DOWN: RunState, ATTACK_DOWN: SleepState,
                ATTACK_UP: SleepState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               UP_UP: IdleState, DOWN_UP: IdleState, UP_DOWN: IdleState, DOWN_DOWN: IdleState, ATTACK_DOWN: SleepState,
                ATTACK_UP: SleepState},

    SleepState: {LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, LEFT_UP: IdleState, RIGHT_UP: IdleState, ATTACK_DOWN: IdleState,
                 ATTACK_UP: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 280
        # Boy is only once created, so instance image loading is fine
        self.RunimageLR = load_image('will_leftright.png')
        self.RunimageUD = load_image('will_frontback.png')
        self.Idleimage = load_image('will_idle.png')
        self.Bowimage = load_image('will_bow.png')
        self.dirRL = 1
        self.dirUD = 1
        self.TransChange = True
        self.velocityX = 0
        self.velocityY = 0
        self.bow = 0
        self.frameRL = 0
        self.frameUD = 0
        self.bowframe = 0
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
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10