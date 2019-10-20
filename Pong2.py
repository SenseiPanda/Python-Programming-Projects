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

#10/4 goals:
#be able to move both paddles at the same time
#get a bounce off of the paddle
#get a bounce off of the horizontal lines



#drawing constants that won't change
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_MOVE = 10
FRAME_RATE = 50
SPEED = 4
BALL_RADIUS = 10
#the x-values of the paddles won't change, make them constants

#x and y velocities of the ball, in pixels per frame
v_x = -2
v_y = 2


PADDLE_ONE_X = 0
PADDLE_TWO_X = 380

#give a starting position for the ball in the center of the screen
BALL_START_X = WINDOW_WIDTH/2
BALL_START_Y = WINDOW_HEIGHT/2

#give initial y values
y1 = 0
y2 = WINDOW_HEIGHT-PADDLE_HEIGHT

#identify the keys and what they will do when pressed
MOVE_ONE_UP_KEY = 'a'
MOVE_ONE_DOWN_KEY = 'z'
MOVE_TWO_UP_KEY = 'k'
MOVE_TWO_DOWN_KEY = 'm'
QUIT_KEY = 'q'
SPACE_KEY = 'space'

#initialize states for the keys that can be pressed
moving_one_up = False     # is 'a' key currently pressed?
moving_one_down = False   # is 'z' key currently pressed?
moving_two_up = False     # is 'k' key currently pressed?
moving_two_down = False   # is 'm' key currently pressed?
quitting = False          # did user hit 'q' to quit?
start_game = False        # did user hit 'space' to start game?

FRAME_RATE = 60     # how many frames to display per second
TIMESTEP = 1.0 / FRAME_RATE

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
    global moving_one_up, moving_one_down, moving_two_up, moving_two_down, quitting, start_game
    if key == SPACE_KEY:
        start_game = state
    elif key == MOVE_ONE_UP_KEY:
        moving_one_up = state
        if  moving_one_up and key== MOVE_TWO_DOWN_KEY:
            moving_two_down = state       #still stumped as to how to move both paddles at once
    elif key == MOVE_ONE_DOWN_KEY:
        moving_one_down = state
    elif key == MOVE_TWO_UP_KEY:
        moving_two_up = state
    elif key == MOVE_TWO_DOWN_KEY:
        moving_two_down = state
    elif key == QUIT_KEY:
        quitting = state

# now if two keys are pressed at once(this still doesn't work):

    if key == MOVE_ONE_UP_KEY and key==MOVE_TWO_DOWN_KEY:
        moving_one_up = state
        moving_two_down = state
    if key == MOVE_ONE_DOWN_KEY and key==MOVE_TWO_DOWN_KEY:
        moving_one_down = state
        moving_two_down = state
    if key == MOVE_ONE_UP_KEY and key==MOVE_TWO_UP_KEY:
        moving_one_up = state
        moving_two_up = state
    if key == MOVE_ONE_DOWN_KEY and key==MOVE_TWO_UP_KEY:
        moving_one_down = state
        moving_two_up = state

# define if a key is being pressed

def key_down(key):
    change_key_state(key, True)


# When a key is released, if it is one of the four keys of
# interest, record that it was released.

def key_up(key):
    change_key_state(key, False)

#initialize variables for where the ball is going to start

x = BALL_START_X
y = BALL_START_Y
ball_moving = True

# where is the ball going next?

def compute_next_position(position, velocity, timestep):
    return position + velocity * timestep

#now let's get this f***ing party started.

#this program is a function of drawing and redrawing things over and over quickly

#drawings happen so quickly that the brain sees rigid motion as smooth motion

def draw_frame():

    #bring some variables in that we're going to need
    global y1, y2, next_x, next_y, ball_moving,x,y

    # draw a teal background

    set_fill_color(0, 0.5, 0.5)
    draw_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)   #draw the window with constants from earlier

    draw_paddles(y1,y2)

    #below is dead code, couldn't get this feature to work
    #draw_text("Press the space key to start the game",WINDOW_WIDTH/5,WINDOW_HEIGHT/2)

    #take key states and make paddles do stuff

    if moving_one_up:

        if y1 > 0:   #does the paddle have room to move?
            y1 -= PADDLE_MOVE
    elif moving_one_down:
        if y1 < 320: #does the paddle have room to move?
            y1 += PADDLE_MOVE
    elif moving_two_up:
        if y2 > 0:
            y2 -= PADDLE_MOVE
    elif moving_two_down:
        if y2 < 320:
            y2 += PADDLE_MOVE
    elif quitting:   #did the user hit the quit key? if so, cancel program
        cs1_quit()
    elif x > 400:    #if the ball goes past a vertical wall, it's game over
        cs1_quit()
    elif x < 0:
        cs1_quit()
    global v_x, v_y, ball_horizontal_left_x, ball_horizontal_right_x, ball_bottom, ball_top
    set_fill_color(.3, .5, 1)  # blue ball

    set_stroke_width(2)

    # draw the ball
    disable_stroke()
    draw_circle(x, y, BALL_RADIUS)
    # get endpoints of ball, to set up detection function if it hits wall
    ball_horizontal_left_x = (x - BALL_RADIUS / 2)
    ball_horizontal_right_x = (x + BALL_RADIUS / 2)
    ball_bottom = (y + BALL_RADIUS / 2)
    ball_top = (y - BALL_RADIUS / 2)

    # make the ball move
    next_x = x + v_x
    next_y = y + v_y

    if ball_moving:

        x = x + v_x    #x position moves in velocity increments
        y = y + v_y    #y position moves in velocity increments

        #write if statements that change direction of x-velocity of ball if paddles are contacted

        if contact_paddle():

            v_x = -1 * v_x
            if x < WINDOW_WIDTH/2:    #on left side of window
                x = x + 10            #why +10? get the hell out of dodge to avoid slithering
            elif x > WINDOW_WIDTH/2:  #on right side of window
                x = x - 10

        if contact_wall():
            v_y = -1 * v_y
            if y > WINDOW_HEIGHT/2:  #on top of window
                y = y - 10
            elif y < WINDOW_HEIGHT/2:  #on bottom of window
                y = y + 10

    return    #because we usually put return at the end of things and it makes stuff work


#define variables for y positions of paddles

left_paddle_top = y1
left_paddle_bottom= y1 + PADDLE_HEIGHT

right_paddle_bottom= y2 + PADDLE_HEIGHT
left_paddle_right_edge_x = PADDLE_WIDTH
right_paddle_left_edge_x = WINDOW_WIDTH - PADDLE_WIDTH


#set up functions to detect whether ball has made contact with a surface, either the paddles or the wall


def contact_paddle():

    #bring in global stuff that we'll need for this function

    global ball_horizontal_left_x, y, ball_horizontal_right_x,y1,y2
    global left_paddle_bottom,  right_paddle_bottom
    left_paddle_bottom = y1 + PADDLE_HEIGHT
    right_paddle_bottom= y2 + PADDLE_HEIGHT

    #did the side of the ball hit?
    if ball_horizontal_left_x-BALL_RADIUS < left_paddle_right_edge_x:
        if y1<next_y:
            if left_paddle_bottom>next_y:
                return True

    # do the same thing for the right paddle

    if ball_horizontal_right_x+BALL_RADIUS> right_paddle_left_edge_x:

        if  y2<next_y:
            if right_paddle_bottom>next_y:
                #print(next_y) #it's not making it in here for some reason
                return True

    return False

#make a function that returns true if horizontal walls contacted

def contact_wall():
    global  y, y1, y2, ball_bottom, ball_top
    if ball_bottom>WINDOW_HEIGHT:
        return True
    elif ball_top<0:
        return True

    return False


#not going to lie, don't know much about this start_graphics thing, but it makes a bunch of references
#to the cs1lib and magically everything works

start_graphics(draw_frame, key_press = key_down, key_release = key_up,
               width = WINDOW_WIDTH, height = WINDOW_HEIGHT, framerate=FRAME_RATE, title = "Pong" )