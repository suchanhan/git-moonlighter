from pico2d import *
import random



DUNGEON_WIDTH, DUNGEON_HEIGHT = 1280, 720


class Character:
    def __init__(self):
        self.image = load_image('char.png')



    def draw(self):
        self.image.draw(400,200)

def handle_events():
    global running
    global dir_y
    global dir_x
    global h
    global a
    global frame_x

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:


               if event.key == SDLK_UP:
                   frame_x = 28

                   dir_y += 1
                   h = 86
               elif event.key == SDLK_DOWN:
                  frame_x = 28

                  dir_y -= 1
                  h = 129
               elif event.key == SDLK_LEFT:
                  frame_x = 28

                  dir_x += 1

                  h = 43
               elif event.key == SDLK_a:

                   frame_x = 42
                   h = 0

               elif event.key == SDLK_ESCAPE:
                   runnung = False
        elif event.type == SDL_KEYUP:



               if event.key == SDLK_UP:
                  frame_x = 28
                  dir_y -= 1
                  h = 86

               elif event.key == SDLK_DOWN:
                   frame_x = 28

                   dir_y += 1
                   h = 129


               elif event.key == SDLK_LEFT:
                   frame_x = 28

                   dir_x -= 1
                   h = 43







open_canvas(DUNGEON_WIDTH, DUNGEON_HEIGHT)

Dungeon_Map = load_image("DungeonMap.png")
character = Character()
#character_MoveL = load_image("캐릭터 달리기.PNG")
character_MoveWD = load_image("랄프.png")


running = True
x = 1000
y = 400
h = 129
a = 0
frame = 0
frame_x = 0
dir_x = 0
dir_y = 0
events = get_events()




while running:
    clear_canvas()
    Dungeon_Map.draw(DUNGEON_WIDTH//2, DUNGEON_HEIGHT//2)

    #if events.key == SDLK_RIGHT:
    #character_MoveL.clip_draw(frame * 68,0,68,100,x,90)
    #elif events.key == SDLK_LEFT:






    character_MoveWD.clip_draw(frame * frame_x, h, 30, 43, x, y,75,75)



    handle_events()
    update_canvas()

    y += dir_y * 10
    x -= dir_x * 10



    frame = (frame + 1) % 5



    delay(0.07)

close_canvas()

