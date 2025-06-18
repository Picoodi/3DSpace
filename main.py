# This is the python script for my 3DSpace programm
# It is a mathematical application for the geometry in 3D Space
# If you do it right it also works for 2D Space
# I will comment the rest of the code as well to make the script understandable
# In the programm you can type help and all commands with explanation will be
# shown to the user in the same window.
# The coordinates are shown in [[x],[y],[z]] because with this matrix multiplication
# can be implemented easily as well.

# the necessary libraries for the project
from math import sqrt, sin, cos, tan, asin, acos, atan

from Functions.Help_Function import help

from Functions.Point_Functions import *
from Functions.Vector_Functions import *


####################START OF THE PROGRAMM########

# Setup lists for the programm that are ESSENTIAL
# We store every Object inside those lists
# All Objects will have a name with which we will find
# the objects the user needs
all_points = []
all_vectors = []
# the origin point is already defined. Important for creating vectors
all_points.append(Point("origin", [[0], [0], [0]]))

# Saying hello to the user
# Explaining how the axis are named
print("Hello there. If you need help with the programm just type help \n"
      "The coordinates are\n"
      "     z\n"
      "     |\n"
      "     |\n"
      "     +------ y\n"
      "    /\n"
      "   x\n"
      "The point (0/0/0) is already defined with the name origin"
      )

# Having the while loop as the start
while True:
    user_input = input("> ")

    # for the rest its always if statements which command the user typed
    # and we use more input() functions to get the necessary information
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
            all_points.append(create_point(name, x, y, z))
        except:
            print("There has been a problem with your input.")


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


    elif user_input.lower() == "rename point":
        name = input("Name of the point: ")
        new_name = input("New name: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                element.rename_point(new_name)
                print(f"successfully renamed too {new_name}")


    elif user_input.lower() == "all points":
        for element in all_points:
            print(element.name, element.coordinates)


    elif user_input.lower() == "mirror point":
        plane = input("With which plane / point / axis wo mirror: ")
        new_name = input("Name of the new point: ")
        name = input("Which point you want to mirror: ")
        try:
            all_points.append(mirror_point(plane, new_name, name, all_points))
        except:
            print("There has been a problem with your input.")


    elif user_input.lower() == "position vector":
        point_name = input("Name of the point: ")
        try:
            for element in all_points:
                if element.name == point_name:
                    all_vectors.append(element.position_vector(point_name))
        except:
            print("There has been a problem with your input.")



    elif user_input.lower() == "vector":
        try:
            name = input("name = ")
            x = float(input("x = "))
            y = float(input("y = "))
            z = float(input("z = "))
            Vector, VectorTip = create_vector(name, x, y, z)
            all_vectors.append(Vector)
            all_points.append(VectorTip)
        except:
            print("There has been a problem with your input.")


    elif user_input.lower() == "vector points":
        try:
            name = input("Name of the vector: ")
            pointA = input("Starting Point: ")
            pointB = input("End Point: ")
            all_vectors.append(create_vector_with_points(name, pointA, pointB, all_points))
        except:
            print("There has been a problem with your input.")


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

    elif user_input.lower() == "rename vector":
        name = input("Name of the vector: ")
        new_name = input("New name: ")
        for element in all_vectors:
            if element.name.lower() == name.lower():
                element.rename_vector(new_name)
                print(f"successfully renamed too {new_name}")


    elif user_input.lower() == "magnitude vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                print(element.magnitude())


    elif user_input.lower() == "add vectors":
        new_name = input("New vector name: ")
        VectorA = input("First vector: ")
        VectorB = input("Second vector: ")

        try:
            for element in all_vectors:
                if element.name == VectorA:
                    VectorA = element
                if element.name == VectorB:
                    VectorB = element

            all_vectors.append(add_vectors(VectorA, VectorB, new_name))

        except:
            print("There has been a problem with the Vectors of yours.")


    elif user_input.lower() == "subtract vectors":
        new_name = input("New vector name: ")
        VectorA = input("First vector: ")
        VectorB = input("Second vector: ")

        try:
            for element in all_vectors:
                if element.name == VectorA:
                    VectorA = element
                if element.name == VectorB:
                    VectorB = element

            all_vectors.append(subtract_vectors(VectorA, VectorB, new_name))

        except:
            print("There has been a problem with the Vectors of yours.")



    elif user_input.lower() == "negative vector":
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.append(element.negative())


    elif user_input.lower() == "multiply vector":
        vector = input("vector name: ")
        number = float(input("multiplied by: "))
        for element in all_vectors:
            if element.name == vector:
                element.scalar_multiplication(number)