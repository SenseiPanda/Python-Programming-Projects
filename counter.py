
class Counter:
    def __init__(self,limit , initial = 0, min_digits=1):
        # define some instance variables
        self.min_digits = min_digits
        self.value = initial #keep track of value variable
        self.limit = limit
        #the current count


    def get_value(self):
        return self.value


    def __str__(self):

        #pad stuff with zeros
        return str((self.min_digits-len(str(self.value))*'0')+str(self.value))


    def tick(self):
        self.value = self.value - 1

        #if it's zero
        if self.value <0:
            self.value == self.limit-1
            #look! it wrapped around?
            return True
        return False










#when in doubt about these types of things, draw a picture
#this is great practice for the next exam --will ask a question



import time

