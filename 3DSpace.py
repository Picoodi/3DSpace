from math import sqrt




class Vector():
    def __init__(self, name, vector_coordinates, pointA, pointB):
        self.name = name
        self.coordinates = vector_coordinates
        self.x1 =  vector_coordinates[0][0]
        self.x2 = vector_coordinates[1][0]
        self.x3 = vector_coordinates[2][0]
        self.PointA = pointA
        self.PointB = pointB

    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")
        print(f"Points: {self.PointA} and {self.PointB}")
        print(f"Magnitude of {self.magnitude()}")

    def magnitude(self):
        return sqrt(self.x1**2 + self.x2**2 + self.x3**2)





class Point():
    def __init__(self, name, list_of_coordinates):
        self.name = name
        self.coordinates = list_of_coordinates


    def info (self):
        print(f"Name: {self.name}")
        print(f"Coordinates: {self.coordinates}")





def create_vector():
    pointA = input("Starting Point: ")
    pointB = input("End Point: ")


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

        name = pointA + pointB
        print(f"Vector {name} with coordinates {vector_coordinates} got created successfully.")
        name = Vector(name, vector_coordinates, pointA, pointB)
        all_vectors.append(name)




    else:
        print("sry there has been a problem with your points")





def create_point():
    name = input("name = ")
    x1 = int(input("x1 = "))
    x2 = int(input("x2 = "))
    x3 = int(input("x3 = "))
    list_of_coordinates = [[x1],
                           [x2],
                           [x3]]

    print(f"Point {name} with the coordinates {list_of_coordinates} got created successfully.")
    name = Point(name, list_of_coordinates)
    all_points.append(name)




def help():
        print(" \n"
              " \n"
              "Hello Welcome to the help menu \n"
              "If the command includes {} than there it asks for your specific input. \n"
              "In any other case its only the command itself\n"
              "\n"
              "\n"
              
              "BASIC COMMANDS \n"
              "- exit                                   exit the programm\n"
              "- help                                   open this help menu\n"          
              "\n"
              "\n"

              "POINTS \n"
              "- point                                  create a new point\n"
              "- delete point {point_name}              deletes a specific point\n"
              "- show point {point_name}                gives info about a specific point\n"  
              "- all points                             gives info about all points\n"
              "\n"
              "\n"

              "VECTORS \n"
              "- vector                                 create a new vector \n"
              "- delete vector {vector_name}            deletes a specific vector\n"
              "- show vector {vector_name}              gives info about a specific vector\n"
              "- all vectors                            gives info about all vectors\n"
              "- magnitude vector {vector_name}         magnitude of a specific vector\n"
              "\n"
              "\n"

              )







#Setup for the programm
all_points = []
all_vectors = []


while True:
    user_input = input("> ")


    if user_input.lower() == "exit":
        exit()

    if user_input.lower() == "help":
        help()


    if user_input.lower() == "point":
        try:
            create_point()
        except:
            print("Sry thats not a valid input")


    if user_input.startswith("show point "):
        name = str(user_input[11:])
        for element in all_points:
            if element.name == name:
                element.info()


    if user_input.startswith("delete point "):
        name = str(user_input[13:])
        for element in all_points:
            if element.name == name:
                all_points.remove(element)
        print("succesfully deleted")


    if user_input.lower() == "all points":
        for element in all_points:
            print(element.name, element.coordinates)


    if user_input.lower() == "vector":
        create_vector()


    if user_input.startswith("show vector "):
        name = str(user_input[12:])
        for element in all_vectors:
            if element.name == name:
                element.info()


    if user_input.lower() == "all vectors":
        for element in all_vectors:
            print(element.name, element.coordinates)


    if user_input.startswith("delete vector "):
        name = str(user_input[13:])
        for element in all_vectors:
            if element.name == name:
                all_vectors.remove(element)
        print("succesfully deleted")


    if user_input.startswith("magnitude vector "):
        name = str(user_input[17:])
        for element in all_vectors:
            if element.name == name:
                print(element.magnitude())
