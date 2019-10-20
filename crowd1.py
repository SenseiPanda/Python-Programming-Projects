'''
Write a Crowd class that generates a sea of faces that tracks your mouse movements.
Your __init__ method should take as a parameter the number of faces in the crowd and
initialize two instance variables:
     (1) how_many, the number of faces.
     (2) people, a reference to list of references to Face objects.  Each Face has
         a size of 50 pixels.  The __init__ method should create the Face objects,
         placing them randomly (the faces can overlap one another), and make each
         item in the list reference one of them.

Your Crowd class should have two other methods:
    (1) look_at should should take as input an x, y location and have each Face in
        the Crowd look at this position.
    (2) draw should draw each Face in the Crowd.

Your methods cannot directly call any Eye methods, but should call the
appropriate Face methods look_at and draw.

You can download the Eye and Face classes, along with this test_harness for testing
your Crowd class, from http://www.cs.dartmouth.edu/~cs1/section/week5 .
'''
from face import Face
from eye import Eye
from cs1lib import *
from random import uniform

class Crowd:
    def __init__(self,how_many):
        self.how_many = how_many  #the number of faces
        self.people = []
        for i in range(how_many):    #draw faces for the number given
            self.people.append(Face(uniform(20,380),uniform(20,380), 50))

#have each face in the crowd look at this position

    def look_at(self, x,y):
        self.x = x
        self.y = y
        for face in self.people:
            face.look_at(x,y)

    def draw(self):
        for face in self.people:
            face.draw


start_graphics(Crowd)