from math import sqrt

# The vector is one of the basic building blocks of geometry
class Vector:
    # We need all those parameters for mathematics or finding and working with the object
    def __init__(self, name, vector_coordinates, pointA, pointB):
        self.name = name
        self.coordinates = vector_coordinates  # Vektor = (x,y,z) as a matrix of course
        self.x = vector_coordinates[0][0]
        self.y = vector_coordinates[1][0]
        self.z = vector_coordinates[2][0]
        self.PointA = pointA
        self.PointB = pointB

    # This function prints all the information about the vector
    def info(self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")
        print(f"Points: {self.PointA} and {self.PointB}")
        print(f"Magnitude of {self.magnitude()}")

    def rename_vector(self, new_name):
        self.name = new_name

    # returns the magnitude of the vector calculated with the 3D Pythagoras
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    # Lets you multiply the vector with a number aka scalar, the new values are stored
    def scalar_multiplication(self, scalar):
        self.coordinates = [[self.x * scalar], [self.y * scalar], [self.z * scalar]]
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    # creates a new Vector which is the negative vector of the given object
    def negative(self):
        new_name = input("Name of the negative: ")
        new_coordinates = [[self.x * -1], [self.y * -1], [self.z * -1]]
        return Vector(new_name, new_coordinates, self.PointB, self.PointA)