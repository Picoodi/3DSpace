# This is the python script for my 3DSpace programm
# It is a mathematical application for the geometry in 3D Space
# If you do it right it also works for 2D Space
# I will comment the rest of the code as well to make the script understandable
# In the programm you can type help and all commands with explanation will be
# shown to the user in the same window.
# The coordinates are shown in [[x],[y],[z]] because with this matrix multiplication
# can be implemented easily as well.

#the necessary libraries for the project
from math import sqrt




# The vector is one of the basic building blocks of geometry
class Vector:
    # We need all those parameters for mathematics or finding and working with the object
    def __init__(self, name, vector_coordinates, pointA, pointB):
        self.name = name
        self.coordinates = vector_coordinates #Vektior = (x,y,z) as a matrix of course
        self.x =  vector_coordinates[0][0]
        self.y = vector_coordinates[1][0]
        self.z = vector_coordinates[2][0]
        self.PointA = pointA
        self.PointB = pointB

    #This function prints all the information about the vector
    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")
        print(f"Points: {self.PointA} and {self.PointB}")
        print(f"Magnitude of {self.magnitude()}")

    # returns the magnitude of the vector calculated with the 3D Pythagoras
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

    # Lets you multiply the vector with a number aka scalar, the new values are stored
    def scalar_multiplication(self, scalar):
        self.coordinates = [[self.x * scalar],[self.y * scalar],[self.z * scalar]]
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    # creates a new Vector which is the negative vector of the given object
    def negative(self):
        new_name = input("Name of the negative: ")
        new_coordinates = [[self.x * -1],[self.y * -1],[self.z * -1]]
        print(f"Vector {new_name} with coordinates {new_coordinates} got created successfully.")
        all_vectors.append(Vector(new_name, new_coordinates, self.PointB, self.PointA))





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
    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")




# creates a vector with two given points
def create_vector(name, pointA, pointB):

    pointA_exists = False
    pointB_exists = False
    pointA_coordinates = []
    pointB_coordinates = []

    # we go through the list all_points to get the coordinates
    # of the given points
    for element in all_points:
        if element.name == pointA:
            pointA_coordinates = element.coordinates
            pointA_exists = True

        if element.name == pointB:
            pointB_coordinates = element.coordinates
            pointB_exists = True


    if pointA_exists and pointB_exists == True: #if the points don't exist we give back a fail
        #creaing the mathematical vector
        vector_coordinates = [[pointB_coordinates[0][0] - pointA_coordinates[0][0]],
                              [pointB_coordinates[1][0] - pointA_coordinates[1][0]],
                              [pointB_coordinates[2][0] - pointA_coordinates[2][0]]
                              ]

        #creating a successful message and creating the vector object and adding it to the all_vectors list
        print(f"Vector {name} with coordinates {vector_coordinates} got created successfully.")
        all_vectors.append(Vector(name, vector_coordinates, pointA, pointB))


    else:
        print("sry there has been a problem with your points")





def create_point(name, x,y,z):
    #just putting the input into the right list format
    list_of_coordinates = [[x],
                           [y],
                           [z]]

    # creating a successful message and creating the point object and adding it to the all_points list
    print(f"Point {name} with the coordinates {list_of_coordinates} got created successfully.")
    all_points.append(Point(name, list_of_coordinates))



# not jet finished the mirror function. Point and axis mirroring still need to be implemented
def mirror_point(plane, new_name, point_name):
    # plane where the point will be mirrored can be o aka origin , xy, xz, yz
    list_of_coordinates = []
    new_coordinates = []

    # We need the original coordinates of the point from the all_points list
    for element in all_points:
        if element.name == point_name:
            list_of_coordinates = element.coordinates


    # we check which plane it is and change the coordinates accordingly
    if plane == "o":
        new_coordinates = [[list_of_coordinates[0][0] *-1],
                           [list_of_coordinates[1][0] *-1],
                           [list_of_coordinates[2][0] *-1]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "xy":
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0] * -1]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "xz":
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0] * -1],
                           [list_of_coordinates[2][0] ]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "yz":
        new_coordinates = [[list_of_coordinates[0][0] * -1],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0]]]
        new_point = Point(new_name, new_coordinates)


    #If the input of the plane ist not right we give that back to the user and break the function with None return
    else:
        print("Sry your plane to mirror is not defined. See the help page for more infos.")
        return None

    #If everything worked we create a new Point object and add it to all_points list
    print(f"Point {new_name.name} with the coordinates {new_coordinates} got created successfully.")
    all_points.append(new_point)




def add_vectors(VectorA, VectorB, new_name):
    #we take two vectors and try to add them together
    try:
         new_coordinates =[[VectorA.x + VectorB.x],
                           [VectorA.y + VectorB.y],
                           [VectorA.z + VectorB.z]]

         all_vectors.append(Vector(new_name, new_coordinates, None, None))

    #if something went wrong we tell it the user
    except:
        print("There has been a problem with the Vectors of yours")



# The help page shows every command and an explanation for each one
def help():
        print(" \n"
              " \n"
              "Hello Welcome to the help menu \n"
              "\n"
              "\n"
              
              "BASIC COMMANDS \n"
              "- exit                                   exit the programm\n"
              "- help                                   open this help menu\n"          
              "\n"
              "\n"

              "POINTS \n"
              "- point                                  create a new point\n"
              "- delete point                           deletes a specific point\n"
              "- show point                             gives info about a specific point\n"  
              "- all points                             gives info about all points\n"
              "- mirror point                           mirror a point on the given plane\n"
              "                                         possible planes are o,xy,xz,yz\n"
              "\n"

              "VECTORS \n"
              "- vector                                 create a new vector \n"
              "- delete vector                          deletes a specific vector\n"
              "- show vector                            gives info about a specific vector\n"
              "- all vectors                            gives info about all vectors\n"
              "- magnitude vector                       magnitude of a specific vector\n"
              "- add vectors                            lets you add two given vectors\n"
              "- negative vector                        creates the negative vector of the given one\n"
              "- multiply vector                        skalar multiplication of 1 vector\n"
              "\n"
              "\n"

              )





####################START OF THE PROGRAMM########

#Setup lists for the programm that are ESSENTIAL
#We store every Object inside those lists
#All Objects will have a name with which we will find
#the objects the user needs
all_points = []
all_vectors = []


#Saying hello to the user
#Explaining how the axis are named
print("Hello there. If you need help with the programm just type help \n"
      "The coordinates are\n"
      "     z\n"
      "     |\n"
      "     |\n"
      "     +------ y\n"
      "    /\n"
      "   x\n"
      )

#Having the while loop as the start
while True:
    user_input = input("> ")

    #for the rest its always if statements which command the user typed
    #and we use more input() functions to get the necessary information
    # to call the corresponding function
    # we also search the all_points and all_vectors lists to get information

    if user_input.lower() == "exit":
        exit()

    elif user_input.lower() == "help":
        help()


    elif user_input.lower() == "point":
        try:
            name = input("name = ")
            x = float(input("x = "))
            y = float(input("y = "))
            z = float(input("z = "))
            create_point(name, x, y, z)
        except:
            print("There has been a problem with your input")


    elif user_input.lower() == "show point":
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                element.info()


    elif user_input.lower() == "delete point":
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                all_points.remove(element)
                print("successfully deleted")


    elif user_input.lower() == "all points":
        for element in all_points:
            print(element.name, element.coordinates)


    elif user_input.lower() == "mirror point":
        plane = input("With which plane / point / axis wo mirror: ")
        new_name = input("Name of the new point: ")
        name = input("Which point you want to mirror: ")
        try:
            mirror_point(plane, new_name, name)
        except:
            print("There has been a problem with your input")


    elif user_input.lower() == "vector":
        try:
            name = input("Name of the vector: ")
            pointA = input("Starting Point: ")
            pointB = input("End Point: ")
            create_vector(name, pointA, pointB)
        except:
            print("There has been a problem with your input")


    elif user_input.lower() == "show vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    elif user_input.lower() == "all vectors":
        for element in all_vectors:
            print(element.name, element.coordinates)


    elif user_input.lower() == "delete vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.remove(element)
                print("successfully deleted")


    elif user_input.lower() == "magnitude vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                print(element.magnitude())


    elif user_input.lower() == "add vectors":
        new_name = input("New vector name: ")
        VectorA = input("First vector: ")
        VectorB = input("Second vector: ")

        for element in all_vectors:
            if element.name == VectorA:
                VectorA = element
            if element.name == VectorB:
                VectorB = element

        add_vectors(VectorA, VectorB, new_name)


    elif user_input.lower() == "negative vector":
        name =  input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.negative()


    elif user_input.lower() == "multiply vector":
        vector = input("vector name: ")
        number = float(input("multiplied by: "))
        for element in all_vectors:
            if element.name == vector:
                element.scalar_multiplication(number)