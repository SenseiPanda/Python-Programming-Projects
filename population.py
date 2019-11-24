
class Population:
    def __init__(self, population,city_name, latitude, longitude):
        self.city_name = city_name
        self.population = population
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):

        return str(self.city_name + ","+ self.population + ","+ self.latitude + "," + self.longitude)
