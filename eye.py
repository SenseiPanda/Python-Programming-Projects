from math import *
from cs1lib import *

class Eye:
    def __init__(self, x, y, rad, r = 0, g = 0, b = 1):
        # Eye position and size.
        self.x = x
        self.y = y
        self.rad = rad
        self.direction = 0

        # Eye color.
        self.r = r
        self.g = g
        self.b = b

    # Have this Eye look at location lx, ly.
    def look_at(self, lx, ly):
        self.direction = atan2(ly - self.y, lx - self.x)

    def draw(self):
        # Draw the outer circle.
        enable_stroke()
        set_fill_color(1, 1, 1)
        draw_circle(self.x, self.y, self.rad)

        # Draw the inner circle.
        set_fill_color(self.r, self.g, self.b)
        ix = 0.4 * self.rad * cos(self.direction) + self.x
        iy = 0.4 * self.rad * sin(self.direction) + self.y
        draw_circle(ix, iy, 0.5 * self.rad)
