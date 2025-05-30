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





def create_vector():
    name = input("Name of the vector: ")
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


        print(f"Vector {name} with coordinates {vector_coordinates} got created successfully.")
        name = Vector(name, vector_coordinates, pointA, pointB)
        all_vectors.append(name)


    else:
        print("sry there has been a problem with your points")





def create_point():
    name = input("name = ")
    x = float(input("x1 = "))
    y = float(input("x2 = "))
    z = float(input("x3 = "))
    list_of_coordinates = [[x],
                           [y],
                           [z]]

    print(f"Point {name} with the coordinates {list_of_coordinates} got created successfully.")
    name = Point(name, list_of_coordinates)
    all_points.append(name)




def mirror_point(plane):
    list_of_coordinates = []
    new_coordinates = []
    new_name = input("Name of the new point: ")
    name = input("Which point you want to mirror: ")
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
        return 1


    print(f"Point {new_name.name} with the coordinates {new_coordinates} got created successfully.")
    all_points.append(new_name)




def add_vectors():
    name = input("New vector name: ")
    VectorA = input("First vector: ")
    VectorB = input("Second vector: ")
    for element in all_vectors:
        if element.name == VectorA:
            VectorA = element
        if element.name == VectorB:
            VectorB = element

    try:
         new_coordinates =[[VectorA.x + VectorB.x],
                           [VectorA.y + VectorB.y],
                           [VectorA.z + VectorB.z]]

         print(f"Vector {name} with coordinates {new_coordinates} got created successfully.")
         name = Vector(name, new_coordinates, None, None)
         all_vectors.append(name)

    except:
        print("There has been a problem with the Vectors of yours")



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
              "- mirror point {plane}                   mirror a point on the given plane\n"
              "                                         possible planes are o,xy,xz,yz\n"
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
            create_point()
        except:
            print("Sry thats not a valid input")


    if user_input.startswith("show point "):
        name = str(user_input[11:])
        for element in all_points:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    if user_input.startswith("delete point "):
        name = str(user_input[13:])
        for element in all_points:
            if element.name.strip().lower() == name.strip().lower():
                all_points.remove(element)
                print("successfully deleted")


    if user_input.lower() == "all points":
        for element in all_points:
            print(element.name, element.coordinates)


    if user_input.startswith("mirror point "):
        plane = str(user_input[13:])
        mirror_point(plane)







    if user_input.lower() == "vector":
        create_vector()


    if user_input.startswith("show vector "):
        name = str(user_input[12:])
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    if user_input.lower() == "all vectors":
        for element in all_vectors:
            print(element.name, element.coordinates)


    if user_input.startswith("delete vector "):
        name = str(user_input[13:])
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.remove(element)
                print("successfully deleted")


    if user_input.startswith("magnitude vector "):
        name = str(user_input[17:])
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                print(element.magnitude())


    if user_input.lower() == "add vectors":
        add_vectors()
