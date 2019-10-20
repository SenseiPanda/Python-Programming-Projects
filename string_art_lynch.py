#string_art.py
# this program draws some colorful string art just for funsies
from cs1lib import *
def main():
    def draw_strings(x_A1, y_A1, x_A2, y_A2, x_B1, y_B1, x_B2, y_B2,n):
        disable_stroke()

        set_fill_color(1, 0, 0)  # set 'background' to black by adding black rectangle, only once
        draw_rectangle(0, 0, 400, 400)
        # draw the first rectangle(A) strings will be attached to

        set_fill_color(0, 1, 0)  # sets fill color to green
        draw_rectangle(x_A1, y_A1, (x_A2 - x_A1), (y_A2 - y_A1))
        # draw the first rectangle(A) strings will be attached to
        # if you want different color for 2nd rectangle remove # from next line of code
        set_fill_color(0,0,1)
        draw_rectangle(x_B1, y_B2, (x_B2 - x_B1), (y_B2 - y_B1))
        #draw the second rectangle(B) strings will be attached to

        #now we need to draw n number of strings, specified in the parameter
        #for this, a process is going to be repeated n number of times, so a while loop is needed
        string_number = 0
        #make a function for the length from the end of the stick
        f = 0

        draw_line(x_A1,y_A1,x_A2,y_A2) #see if this function even works, it doesn't show anything
        while (string_number<=n):
            #draw_circle(x_A1,(y_A1 + f* (y_A2 - y_A1)),10) #x values will stay same, vetical stick
            string_number = string_number+1
            set_fill_color(0, 0, 1)

            draw_line(x_A1,(y_A1 + f*(y_A2 - y_A1)),(x_B1 + f*(x_B2 - x_B1)),y_B1)

            print(f*(y_A2 - y_A1)) #check that it's doing what we need it to do

            f = string_number / n

            string_number = string_number+1

            #print(string_number)check stuff


    draw_strings(25, 50, 28, 200, 350, 303, 200, 300, 25)
    return

    start_graphics(main)
    counter = counter+1






