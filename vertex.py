from cs1lib import *

CIRCLE_RADIUS = 10
STROKE_WIDTH = 10


class Vertex:
    def __init__(self, v_name, vertex_x, vertex_y):
        self.v_name = v_name  # (string)
        self.vertex_x = vertex_x  # (int)
        self.vertex_y = vertex_y  # (int)
        self.adj_vertex_list = []  # (list)

    #have method for returning string of self for checkpoint

    def __str__(self):
        for item in self.adj_vertex_list:
            i = 0
            j = len(self.adj_vertex_list) - 1
            adj_list = ""
            while i < j:
                adj_list += self.adj_vertex_list[i].get_name() + ', '
                i += 1
            adj_list += self.adj_vertex_list[i].get_name()
        return (self.v_name + ";" + " Location: " + str(self.vertex_x) + "," + str(
            self.vertex_y) + ';' + " Adjacent Vertices: " + adj_list)

    #method for returning a list of neighbors for an object

    def return_ajd_list(self):
        return self.adj_vertex_list

    def get_name(self):
        return self.v_name

    #method for populating adjancency list

    def adj_list_add(self, point):
        self.adj_vertex_list.append(point)

    #draw all of the circles on the map

    def draw_vertex_circles(self, r, g, b):
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.vertex_x, self.vertex_y, CIRCLE_RADIUS)


    #have function that takes a reference to another vertex object and then
    #draws a rectangle(edge) between the two vertices

    def draw_edges(self, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)

        for adj in self.adj_vertex_list:
            draw_line(self.vertex_x, self.vertex_y, adj.vertex_x, adj.vertex_y)

    #additional 'draw_edge' method

    def draw_edge(self, vertex, r, g, b):
        enable_stroke()
        set_stroke_color(r, g, b)
        set_stroke_width(STROKE_WIDTH)
        draw_line(self.vertex_x, self.vertex_y, vertex.vertex_x, vertex.vertex_y)

    def get_x(self):

        return self.vertex_x

    def get_y(self):

        return self.vertex_y

    #if the initial click is inside a circle radius return true

    def in_circle_radius(self, x, y):
        if abs(self.vertex_x-x) <= CIRCLE_RADIUS and abs(self.vertex_y-y) <= CIRCLE_RADIUS:
            return True


