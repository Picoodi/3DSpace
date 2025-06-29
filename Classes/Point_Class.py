from Classes.Vector_Class import Vector

# The Point in a 3D Space P = (x,y,z)
class Point:
    # We need all those parameters for mathematics or finding and working with the object
    def __init__(self, name, list_of_coordinates):
        self.name = name
        self.coordinates = list_of_coordinates
        self.x = list_of_coordinates[0][0]
        self.y = list_of_coordinates[1][0]
        self.z = list_of_coordinates[2][0]

    # This function prints all the information about the point
    def info(self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")

    def rename_point(self, new_name):
        self.name = new_name

    def position_vector(self, name):
        #creating the vector object with the same coordinates
        return Vector(f"position_vector_{name}", self.coordinates, "origin", self.name)


