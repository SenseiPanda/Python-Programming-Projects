
from cs1lib import *
from vertex import *
from load_graph import *
from collections import deque

#bring in our vertex dictionary

vertex_dictionary = load_graph('dartmouth_graph.txt')


def bfs(start, goal):

    #let's expore this frontier, y'all

    frontier = deque()

    #make a backpointers dictionary to populate previous points
    backpointers = {}
    backpointers[start] = None

    #ultiamtely we want to populate an array with the shortest path

    path = []

    frontier.append(start)

    while len(frontier) > 0:
        current = frontier.popleft()
        #start with the start. if current is not goal, explore neighbors, explore frontier,
        # and populate backpointer[neighbors] = current
        if current != goal:
            for adj in current.return_ajd_list():
                if adj not in backpointers:
                    if adj not in frontier:
                        backpointers[adj] = current
                        frontier.append(adj)
        else:
            while current != None:
                path.append(current)
                current = backpointers[current]
            return path


