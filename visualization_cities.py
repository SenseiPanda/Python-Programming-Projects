#this code does not run on its own, it can only run in the great 'Lab 2' codebase

for pop in population_cities[0:49]:
    pop = Population(str(pop[0]), str(pop[1]), str(pop[2]), str(pop[3]))
    top_50.append(str(pop))

# if this returns false, then reverse the list so returned list is biggest to smallets
img = load_image('world.png')


def adjust_lat(lat):
    # adjust lat/long to actually coordinates on the picture
    if lat < 0:
        y = 180 + (abs(lat) * 2)
    elif lat > 0:
        y = ((90 - lat) * 2)
    return y


def adjust_long(long):
    if long < 0:
        x = ((180 + long) * 2)
    else:
        x = 360 + (long * 2)
    return x


print(top_50)


def draw_frame():
    global img
    draw_rectangle(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
    draw_image(img, 0, 0)

    # convert these numbers
    for place in top_50:
        place = place.strip()
        things = place.split(',')
        print(things)
        my_lat = float(things[2])
        my_long = float(things[3])
        print(my_lat)
        print(my_long)
        my_long = adjust_long(my_long)
        my_lat = adjust_lat(my_lat)
        print(my_lat)
        print(my_long)
        set_fill_color(0, 0.5, 0.5)
        draw_circle(my_long, my_lat, 5)

    return


start_graphics(draw_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, framerate=1)

