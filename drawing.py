from cs1lib import *


# Let's make a function that draws the cover of green eggs and ham!
def seuss():

    clear()
    #disable_stroke() - disable disable stroke so we can get outlines
    # of objects like Cormen's drawing

    #draw the red background
    set_fill_color(1, 0, 0) # bright red
    draw_rectangle(0,0,400,400)

    # draw the white triangle
    set_fill_color(1, 1, 1) # white
    draw_triangle(50,150,300,350,350,50)

    # draw the egg whites
    set_fill_color(1, 1, 1) # white, naturally
    draw_ellipse(130,180,30,20)
    draw_ellipse(180, 220, 30, 20)



    #draw the egg yolks - new function for this??
    #disable_stroke() #no outlines on these guys
    set_fill_color(0,1,0) # green
    #make sure yolks are concentric with previous ellipses
    draw_circle(130,180,10)
    draw_circle(180,220,10)

    #now draw the green ham- green ellipse with white circle space in middle
    #don't need to set fill color bc it's already green
    draw_ellipse(250, 130, 50, 25)

    #hole in the ham
    set_fill_color(1,1,1) #white
    draw_circle(250, 130, 5)

    #this fork is going to be a PITA to draw
    set_fill_color(0,0,1) #blue
    #the fork is just 6 rectangles together pretending to be a fork LOL
    draw_rectangle(235,115, 2,  12)
    draw_rectangle(231, 115, 2, 12)
    draw_rectangle(227, 115, 2, 12)
    draw_rectangle(223, 115, 2, 12)
    draw_rectangle(219, 115, 2, 12)
    draw_rectangle(219, 113, 18, 2)
    draw_rectangle(227, 60, 2, 53)
    draw_line(220,240,280,290)
    #now, sign my work
    draw_text("Daniel Lynch", 50, 350)


start_graphics(seuss)