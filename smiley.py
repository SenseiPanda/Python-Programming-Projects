# smiley.py
# <YOUR NAME HERE>
# Code for CS 1 Short Assignment 5
# Draws and moves a smiley face.
# If the mouse button is down, draws the smiley face at the location of the mouse.
# If the 'w' key is pressed, moves the smiley face up.
# If the 's' key is pressed, moves the smiley face down.
# If the 'a' key is pressed, moves the smiley face to the left.
# If the 'd' key is pressed, moves the smiley face to the right.

from cs1lib import *

SPEED = 2   # rate at which the location of the smiley face changes

# Initialize the state variables.
x = 100                 # x location of smiley face center
y = 100                 # y location of smiley face center
moving_up = False       # is 'w' key currently pressed?
moving_down = False     # is 's' key currently pressed?
moving_left = False     # is 'a' key currently pressed?
moving_right = False    # is 'd' key currently pressed?
button_down = False     # is mouse button currently down?

# Key bindings.
MOVE_UP_KEY = 'w'
MOVE_DOWN_KEY = 's'
MOVE_LEFT_KEY = 'a'
MOVE_RIGHT_KEY = 'd'

# Function to draw the smiley face centered at location (x, y).
# Note that because this function does not assign to x and y,
# these variables need not be declared as global.
def draw_smiley(x, y):
    # Draw the outline of the face.
    set_stroke_color(0, 0, 0)   # black outline
    set_fill_color(1, 1, 0)     # yellow fill
    draw_circle(x, y, 25)

    # Draw the mouth.
    set_fill_color(1, 1, 0)     # yellow
    draw_circle(x, y, 15)
    set_stroke_color(1, 1, 0)   # yellow again
    draw_rectangle(x - 16, y - 16, 32, 20)

    # Draw the eyes
    set_stroke_color(0, 0, 0)   # black
    set_fill_color(0, 0, 0)     # black
    draw_circle(x - 10, y - 5, 2)
    draw_circle(x + 10, y - 5, 2)

# When the mouse button is pressed, record that it has been pressed
# and save its location.
def mouse_down(mx, my):
    global x, y, button_down
    button_down = True
    x = mx
    y = my

# When the mouse button is released, record that it has been released.
def mouse_up(mx, my):
    global button_down
    button_down = False

# When the mouse is moved and the button is down, update the
# location of the smiley face.
def mouse_moved(mx, my):
    global x, y
    # YOU FILL THIS IN

# Change a state variable for a key to a new value, if the key
# is one of the four keys of interest.
# First parameter is the key, second parameter is the new state.
def change_key_state(key, state):
    global moving_up, moving_down, moving_left, moving_right

    if key == MOVE_UP_KEY:
        moving_up = state
    elif key == MOVE_DOWN_KEY:
        moving_down = state
    elif key == MOVE_LEFT_KEY:
        moving_left = state
    elif key == MOVE_RIGHT_KEY:
        moving_right = state

# When a key is pressed, if it is one of the four keys of
# interest, record that it was pressed.
def key_down(key):
    change_key_state(key, True)

# When a key is released, if it is one of the four keys of
# interest, record that it was released.
def key_up(key):
    change_key_state(key, False)


# Render a frame of the animation:
#  - Draw the smiley face.
#  - If one of the keys was pressed, update the location of the smiley face.
def draw_frame():
    global x, y

    # Draw a dark green background.
    set_clear_color(0, .412, .243)   # Dartmouth green
    clear()

    draw_smiley(x, y)

    if moving_up:
        y -= SPEED
    elif moving_down:
        y += SPEED
    elif moving_right:
        x += SPEED
    elif moving_left:
        x -= SPEED

def mouse_click(x1,y1):
    global x,y, draw_it
    draw_it = True
    x = x1
    y = y1
# Start the animation.
start_graphics(draw_frame, key_press = key_down, key_release = key_up,
               mouse_press = mouse_down, mouse_release = mouse_up, mouse_move = mouse_moved)