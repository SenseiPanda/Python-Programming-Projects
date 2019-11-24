#-
#--
#----
#------
# This is my first computer game built in python. PONG
#------
#----
#---
#--
from cs1lib import *


#drawing constants that won't change
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVE = 10
FRAME_RATE = 50

#the x-values of the paddles won't change, make them constants

PADDLE_ONE_X = 0
PADDLE_TWO_X = 380

#give initial y values
y1 = 0
y2 = 320
#identify the keys and what they will do when pressed
MOVE_ONE_UP_KEY = 'a'
MOVE_ONE_DOWN_KEY = 'z'
MOVE_TWO_UP_KEY = 'k'
MOVE_TWO_DOWN_KEY = 'm'

moving_one_up = False     # is 'a' key currently pressed?
moving_one_down = False   # is 'z' key currently pressed?
moving_two_up = False     # is 'k' key currently pressed?
moving_two_down = False   # is 'm' key currently pressed?


#each time a movement key is pressed, the paddles will be redrawn
def draw_paddles(y1,y2):

    #draw the paddle w/ initial position
    set_fill_color(0,0.75,0)

    #paddle number one dynamic position
    draw_rectangle(PADDLE_ONE_X,y1,PADDLE_WIDTH,PADDLE_HEIGHT)
    #paddle number two dynamic position
    draw_rectangle(PADDLE_TWO_X,y2,PADDLE_WIDTH,PADDLE_HEIGHT)


#now to make state variables for the keys, as we did in the smiley exercise
def change_key_state(key, state):
    global moving_one_up, moving_one_down, moving_two_up, moving_two_down

    if key == MOVE_ONE_UP_KEY:
        moving_one_up = state
    elif key == MOVE_ONE_DOWN_KEY:
        moving_one_down = state
    elif key == MOVE_TWO_UP_KEY:
        moving_two_up = state
    elif key == MOVE_TWO_DOWN_KEY:
        moving_two_down = state

def key_down(key):
    change_key_state(key, True)

# When a key is released, if it is one of the four keys of
# interest, record that it was released.
def key_up(key):
    change_key_state(key, False)

def draw_frame():
    global y1, y2
    # draw a teal background
    set_fill_color(0, 0.5, 0.5)  # bright red
    draw_rectangle(0, 0, 400, 400)

    draw_paddles(y1,y2)

    if moving_one_up:
        if y1>0:
            y1 -= PADDLE_MOVE
    elif moving_one_down:
        if y1<320:
            y1 += PADDLE_MOVE
    elif moving_two_up:
        if y2>0:
            y2 -= PADDLE_MOVE
    elif moving_two_down:
        if y2<320:
            y2 += PADDLE_MOVE




start_graphics(draw_frame, key_press = key_down, key_release = key_up,
               width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate=50, title = "Pong")