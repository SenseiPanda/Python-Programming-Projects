from cs1lib import *

KEY_TO_PRESS = 'a'
mouse_click = False

def clicked(mx,my):
    global x,y
    mouse_click = True
    x = mx
    y = my
def change_key_state(key, state):
    global pressed

    if key == KEY_TO_PRESS:
        pressed = state

def key_down(key):
    change_key_state(key, True)

# When a key is released, if it is one of the four keys of
# interest, record that it was released.
def key_up(key):
    change_key_state(key, False)

def print_output():
    if pressed:
        if mouse_click:
            print(x,y)



start_graphics(key_press = key_down, key_release = key_up,mouse_press=clicked)