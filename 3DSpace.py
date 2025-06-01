from math import sqrt




class Vector:
    def __init__(self, name, vector_coordinates, pointA, pointB):
        self.name = name
        self.coordinates = vector_coordinates
        self.x =  vector_coordinates[0][0]
        self.y = vector_coordinates[1][0]
        self.z = vector_coordinates[2][0]
        self.PointA = pointA
        self.PointB = pointB

    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")
        print(f"Points: {self.PointA} and {self.PointB}")
        print(f"Magnitude of {self.magnitude()}")

    def magnitude(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)


    def scalar_multiplication(self, scalar):
        self.coordinates = [[self.x * scalar],[self.y * scalar],[self.z * scalar]]
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    def negative(self):
        name = "-" + self.name
        new_coordinates = [[self.x * -1],[self.y * -1],[self.z * -1]]
        print(f"Vector {name} with coordinates {new_coordinates} got created successfully.")
        name = Vector(name, new_coordinates, self.PointB, self.PointA)
        all_vectors.append(name)



class Point:
    def __init__(self, name, list_of_coordinates):
        self.name = name
        self.coordinates = list_of_coordinates
        self.x = list_of_coordinates[0][0]
        self.y = list_of_coordinates[1][0]
        self.z = list_of_coordinates[2][0]


    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")





def create_vector(name, pointA, pointB):

    pointA_exists = False
    pointB_exists = False
    pointA_coordinates = []
    pointB_coordinates = []

    for element in all_points:
        if element.name == pointA:
            pointA_coordinates = element.coordinates
            pointA_exists = True

        if element.name == pointB:
            pointB_coordinates = element.coordinates
            pointB_exists = True


    if pointA_exists and pointB_exists == True:
        vector_coordinates = [[pointB_coordinates[0][0] - pointA_coordinates[0][0]],
                              [pointB_coordinates[1][0] - pointA_coordinates[1][0]],
                              [pointB_coordinates[2][0] - pointA_coordinates[2][0]]
                              ]


        print(f"Vector {name} with coordinates {vector_coordinates} got created successfully.")
        name = Vector(name, vector_coordinates, pointA, pointB)
        all_vectors.append(name)


    else:
        print("sry there has been a problem with your points")





def create_point(name, x,y,z):
    list_of_coordinates = [[x],
                           [y],
                           [z]]

    print(f"Point {name} with the coordinates {list_of_coordinates} got created successfully.")
    name = Point(name, list_of_coordinates)
    all_points.append(name)




def mirror_point(plane, new_name, name):
    list_of_coordinates = []
    new_coordinates = []

    for element in all_points:
        if element.name == name:
            list_of_coordinates = element.coordinates


    if plane == "o":
        new_coordinates = [[list_of_coordinates[0][0] *-1],
                           [list_of_coordinates[1][0] *-1],
                           [list_of_coordinates[2][0] *-1]]
        new_name = Point(new_name, new_coordinates)

    elif plane == "xy":
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0] * -1]]
        new_name = Point(new_name, new_coordinates)

    elif plane == "xz":
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0] * -1],
                           [list_of_coordinates[2][0] ]]
        new_name = Point(new_name, new_coordinates)

    elif plane == "yz":
        new_coordinates = [[list_of_coordinates[0][0] * -1],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0]]]
        new_name = Point(new_name, new_coordinates)

    else:
        print("Sry your plane to mirror is not defined. See the help page for more infos.")
        return None


    print(f"Point {new_name.name} with the coordinates {new_coordinates} got created successfully.")
    all_points.append(new_name)




def add_vectors(VectorA, VectorB, new_name):

    try:
         new_coordinates =[[VectorA.x + VectorB.x],
                           [VectorA.y + VectorB.y],
                           [VectorA.z + VectorB.z]]

         print(f"Vector {new_name} with coordinates {new_coordinates} got created successfully.")
         new_name = Vector(new_name, new_coordinates, None, None)
         all_vectors.append(name)

    except:
        print("There has been a problem with the Vectors of yours")




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

#Setup lists for the programm
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

while True:
    user_input = input("> ")

    if user_input.lower() == "exit":
        exit()

    if user_input.lower() == "help":
        help()


    if user_input.lower() == "point":
        try:
            name = input("name = ")
            x = float(input("x = "))
            y = float(input("y = "))
            z = float(input("z = "))
            create_point(name, x, y, z)
        except:
            print("There has been a problem with your input")


    if user_input.lower() == "show point":
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    if user_input.lower() == "delete point":
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.strip().lower() == name.strip().lower():
                all_points.remove(element)
                print("successfully deleted")


    if user_input.lower() == "all points":
        for element in all_points:
            print(element.name, element.coordinates)


    if user_input.lower() == "mirror point":
        plane = input("With which plane / point / axis wo mirror: ")
        new_name = input("Name of the new point: ")
        name = input("Which point you want to mirror: ")
        try:
            mirror_point(plane, new_name,name)
        except:
            print("There has been a problem with your input")


    if user_input.lower() == "vector":
        try:
            name = input("Name of the vector: ")
            pointA = input("Starting Point: ")
            pointB = input("End Point: ")
            create_vector(name, pointA, pointB)
        except:
            print("There has been a problem with your input")


    if user_input.lower() == "show vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    if user_input.lower() == "all vectors":
        for element in all_vectors:
            print(element.name, element.coordinates)


    if user_input.lower() == "delete vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.remove(element)
                print("successfully deleted")


    if user_input.lower() == "magnitude vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                print(element.magnitude())


    if user_input.lower() == "add vectors":
        new_name = input("New vector name: ")
        VectorA = input("First vector: ")
        VectorB = input("Second vector: ")

        for element in all_vectors:
            if element.name == VectorA:
                VectorA = element
            if element.name == VectorB:
                VectorB = element

        add_vectors(VectorA, VectorB, new_name)


    if user_input.lower() == "negative vector":
        name =  input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.negative()


    if user_input.lower() == "multiply vector":
        vector = input("vector name: ")
        number = float(input("multiplied by: "))
        for element in all_vectors:
            if element.name == vector:
                element.scalar_multiplication(number)