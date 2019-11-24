from vertex import Vertex


# make a function that reads in the file and puts items into a dictionary
def load_graph(data_file):
    # should create one Vertex object per line in the data file and
    # add to a dictionary a reference to each Vertex object it creates
    in_file = open(data_file, "r")
    vertex_dictionary = {}

    text = ""
    for line in in_file:
        split_item = line.split('; ')  # gets an array with an item before each ;
        name = split_item[0]  # the name of the vertex is 1st item in array
        name = name.strip()
        vertices_list = split_item[2].split(',')  # the third item in the array is split into x and y
        vertex_x = int(vertices_list[0])  # record values for x and y as ints
        vertex_y = int(vertices_list[1])
        vertex_dictionary[name] = Vertex(name, vertex_x, vertex_y)



    in_file.close()

    # now make second pass over the file
    in_file = open(data_file, "r")
    for line in in_file:
        split_item = line.split('; ')
        name = split_item[0]

        adjacencies = split_item[1].split(',')
        for item in adjacencies:
            item = item.strip()
            vertex_dictionary[name].adj_list_add(vertex_dictionary[item])
    in_file.close()
    return vertex_dictionary
