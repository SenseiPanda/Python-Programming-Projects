from cs1lib import *
from eye import Eye

class Face:
    def __init__(self, x, y, size):
        # Face position and size.
        self.x = x
        self.y = y
        self.size = size
        
        # Create the eyes.
        self.lefteye = Eye(x - 15, y - 15, 10)
        self.righteye = Eye(x + 15, y - 15, 10)
        
    # Make this Face look at location lx, ly.
    def look_at(self, lx, ly):
        self.lefteye.look_at(lx, ly)
        self.righteye.look_at(lx, ly)
       
    def draw(self):
        enable_stroke()
        set_fill_color(1, 1, 1)
        draw_circle(self.x, self.y, self.size)                          # draw face
        self.lefteye.draw()                                             # draw eyes
        self.righteye.draw()                                            # draw eyes
        draw_line(self.x, self.y, self.x, self.y + 15)                  # draw nose
        draw_line(self.x - 15, self.y + 20, self.x + 15, self.y + 20)   # draw mouth