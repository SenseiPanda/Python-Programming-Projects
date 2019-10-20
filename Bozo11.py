# filename: mystery.py
# author:   Zachary Marois
# date:     September 2011
#
# purpose:  Welcomes the user to CS1
# Modeled after the Mystery.java program for CS5
# and roll_over_button.py by Kelsey Harris
# Modified for 19F by Tom Cormen

# imports
from cs1lib import *
import random

window_width = 400
window_height = 400
first_frame = True

def welcome():
    global first_frame

    if first_frame:
        set_clear_color(0, .412, .243)  # background is Dartmouth green
        clear()
        first_frame = False

    # Draw a random ellipse
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    set_fill_color(r, g, b, .75)
    ellipse_x_radius = 50
    ellipse_y_radius = 40

    x = random.randint(ellipse_x_radius, window_width - ellipse_x_radius)
    y = random.randint(ellipse_y_radius, window_height - ellipse_y_radius)
    disable_stroke()
    draw_ellipse(x, y, ellipse_x_radius, ellipse_y_radius)

    # Draw Welcome messages
    enable_stroke()
    set_stroke_color(0, 0, 0, 1)
    draw_text("Welcome", x - 30, y - 5)
    draw_text("To CS 1", x - 25, y + 15)

start_graphics(welcome, width = window_width, height = window_height)