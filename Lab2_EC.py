#Lab assignment 2
# This lab opens a text file, reads the file into an array, and then
# establishes sorting functions to sort both characters and numbers in different ways.
# Then, a visualization is made showing the 50 most populous cities in the world.
#Daniel Lynch

#import functions from cs 1 library and city class defined for checkpoint
from city import City
from cs1lib import *
from random import randint
from population import Population


# increase recursion limit if needed
#sys.setrecursionlimit(600000)

#establish the window height and width for the png
WINDOW_HEIGHT = 360
WINDOW_WIDTH = 720

#now open or create files that we will output to, and load image we will need for map

img = load_image('world.png')

in_file = open("world_cities.txt", "r")

out_file_alpha = open('cities_alpha.txt', 'w')

out_file_pop = open('cities_population.txt','w')

out_file_lat = open('cities_latitude.txt','w')

def compare_population(city1,city2):
    if city2<=city1:
        return True


# write sorting functions

#a partition function will find a pivot point within the list and return where that point is
def partition(the_list,p,r):

#initially place the pivot at the end of the list
    pivot = the_list[r]
#randomized quicksort for those 5 points of extra credit!
    the_list[r], the_list[randint(p,r)]
#start j at the beginning and i at the super beginning
    i = p-1

#kick higher values to the right side of the list, lower to the left, and return pivot
    for j in range (p,r):
        if the_list[j]<=pivot:
            i = i + 1
            the_list[i], the_list[j] = the_list[j],the_list[i]
    the_list[i + 1], the_list[r] = the_list[r], the_list[i + 1]
    return i+1



def quicksort(the_list, p = 0, r = None):
    if r== None:
        r= len(the_list)-1
    if len(the_list)<2:
        return
    elif p<=r:
#get that pivot point
        q = (partition(the_list,p,r))
#quicksort the first half of the list
        quicksort(the_list, p, q - 1)
#now quicksort the latter half
        quicksort(the_list, q + 1, r)
#give the user back the sorted list
    return the_list

#let's create arrays that only have city names, pops, lats
alpha_cities = []
population_cities = []
latitude_cities = []

#take only city names
for line in in_file:
#read file in, strip white space, and separate items where there are commas

    new_line =  line.strip()

    items = new_line.split(',')
#make a string for each city item
    myCity =City(items[0],items[1],items[2],items[3],items[4],items[5])
    #myCityPop=Population(items[0],items[1],items[2],items[3],items[4],items[5])
    myCityLat=[float(items[4]),float(items[5]),int(items[3]),(items[1])]
    myCityPop = [int(items[3]),(items[1]),float(items[4]),float(items[5])]

#populate string with only city names first
    alpha_cities.append(str(myCity))
#populate string with populations first
    population_cities.append(myCityPop)
#populate string with latitudes first
    latitude_cities.append(myCityLat)
quicksort(population_cities)
#sort everything
quicksort(alpha_cities)
#quicksort(int(population_cities[0::4]))

quicksort(latitude_cities)

#make sure list is in the right order


#compare to make sure most populous first
if compare_population(population_cities[100],population_cities[1]):

    population_cities.reverse()



#now that we're sorted, we need to get population_cities and
#latitude_cities back into original format
#and also write those files

top_50 = []
#write sorted cities file
for city in alpha_cities:
    out_file_alpha.write(str(city) +'\n')

for pop in population_cities:
    pop =Population(str(pop[0]),str(pop[1]),str(pop[2]),str(pop[3]))
    out_file_pop.write(str(pop) +'\n')

for lat in latitude_cities:
    lat = Population(str(lat[2]),str(lat[3]),str(lat[0]),str(lat[1]))
    out_file_lat.write(str(lat) +'\n')

#make an array for the top 50 cities

for pop in population_cities[0:49]:
    pop = Population(str(pop[0]), str(pop[1]), str(pop[2]), str(pop[3]))
    top_50.append(str(pop))




#if this returns false, then reverse the list so returned list is biggest to smallets
img = load_image('world.png')

def adjust_lat(lat):

    #adjust lat/long to actually coordinates on the picture
    if lat<0:
        y = 180+ (abs(lat)*2)
    elif lat>0:
        y = ((90-lat)*2)
    return y

def adjust_long(long):
    if long<0:
        x = ((180+long)*2)
    else:
        x = 360+(long*2)
    return x

print(top_50)

def draw_frame():
    #draw the window with the image
    global img
    draw_rectangle(0, 0, WINDOW_HEIGHT, WINDOW_WIDTH)
    draw_image(img, 0, 0)

    #convert these numbers
    #draw a circle for each of the top cities with the adjusted coordinates
    for place in top_50:
        place = place.strip()
        things = place.split(',')
        print(things)
        my_lat = float(things[2])
        my_long = float(things[3])
        print(my_lat)
        print(my_long)
        #let's adjust those coordinates
        my_long = adjust_long(my_long)
        my_lat = adjust_lat(my_lat)
        print(my_lat)
        print(my_long)
        #now to draw the circles
        set_fill_color(0, 0.5, 0.5)
        draw_circle(my_long,my_lat,5)


    return

start_graphics(draw_frame,width = WINDOW_WIDTH,height = WINDOW_HEIGHT,framerate=10)


#clean house
out_file_alpha.close()

out_file_pop.close()

out_file_lat.close()

in_file.close()



