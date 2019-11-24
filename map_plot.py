from cs1lib import *
from vertex import Vertex
from load_graph import load_graph
from my_bfs import bfs
PIXEL_WIDTH = 1012
PIXEL_HEIGHT = 800

LINE_WIDTH = 5

image = load_image('dartmouth_map.png')
vertex_dictionary = load_graph('dartmouth_graph.txt')


start_vertex = None
goal_vertex = None
start_chosen = None
goal_chosen = None


#mouse click within a circle radius will trigger

def mouse_down(mx, my):
    global x, y, button_down, start_vertex, start_chosen
    #put 'in circle radius function' in here
    button_down = True
    x = mx
    y = my
    if button_down:
        if start_chosen == None:
            for place in vertex_dictionary:
                v = vertex_dictionary[place]
                if v.in_circle_radius(x, y):
                    print("Start clicked in range " + v.get_name())
                    start_vertex = v
                    print("Start vertex is: " + str(start_vertex.get_name))
                    start_chosen = True


#mouse moved function includes creation of 'goal vertex' variable if mouse hovers over
#circle radius of a point only AFTER a start point has been created

def mouse_moved(mx, my):
    global x, y, start_chosen, goal_vertex, mouse_move
    mouse_move = True
    x = mx
    y = my
    for place in vertex_dictionary:
        v = vertex_dictionary[place]
        if start_chosen:
            if v.in_circle_radius(x, y):
                goal_vertex = v
                print("Goal vertex is: " + str(goal_vertex.get_name()))

#function that draws all of the paths, changes color of start circle when clicked
#starts to run bfs when start vertex is clicked and goal vertex is hovered
#takes path returned by bfs function and illumninates path edges and circles in red

def draw_paths():

        global path
        draw_image(image, 0, 0)
        for place in vertex_dictionary:
            v = vertex_dictionary[place]
            v.draw_vertex_circles(0, 0, 1)
            v.draw_edges(0, 0, 1)

        if start_vertex is not None:
            print("start is not none")
            start_vertex.draw_vertex_circles(0,1,0)

        if goal_vertex is not None:
            print("Start vertex is " + str(start_vertex))
            print("Goal vertex is " + str(goal_vertex))
            path = bfs(start_vertex, goal_vertex)
            print("Path is:  " + str(path))
            for i in range(len(path) - 1):
                 path[i].draw_edge(path[i + 1], 1, 0, 0)
                 path[i].draw_vertex_circles(1,0,0)


#let's get this party started, y'all

start_graphics(draw_paths, height=PIXEL_HEIGHT, width=PIXEL_WIDTH,
mouse_press = mouse_down, mouse_move = mouse_moved)