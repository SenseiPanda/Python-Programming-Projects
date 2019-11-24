

#city class


class City:
    def __init__(self, country_code,city_name, region,population,latitude, longitude):
        self.country_code = country_code
        self.city_name = city_name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):

        return str(self.city_name + "," + self.population + "," + self.latitude + "," + self.longitude)


#add functions in here that have .le

#4>5 calls __ge__

#just like print calls __str__

#to override this, redefine function def __ge__():

#when including start_graphics, set window to 720 by 360 (create constants for these)

# (0,0) will actually be in the middle of the graph and thus (360,180) because 0,0 is in Africa

#every recursive function is going to be a log of some number, usually n.log.n

#quick sort divides list in half


# def recursive_loop():
#     for i in range(6):
#         if i
# def partition(list,p,r):
#     log n
#     .
#     .
#     n
#       return i +1
# def quicksort(list,p=0, r = None): this will be a recursive function
#     n^2
#     .
#     .
#     n^x
#if list[j] <pivot move i
#move pivot into i + 1
#tuple switch
# list[i],list[i]=list[j], list[i]

#p isnt always equal to zero
# r is not always equal to len(list)