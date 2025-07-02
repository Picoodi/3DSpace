from Functions.Help_Function import help

from Functions.Point_Functions import *
from Functions.Vector_Functions import *
from storage import all_points, all_vectors


class Commands:

    def help(self):
        help()

    def reset(self):
        all_points.clear()
        all_vectors.clear()
        all_points.append(Point("origin", [[0], [0], [0]]))



    def point(self):
        try:
            name = input("name = ")
            x = float(input("x = "))
            y = float(input("y = "))
            z = float(input("z = "))
            all_points.append(create_point(name, x, y, z))
        except:
            print("There has been a problem with your input.")


    def show_point(self):
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                element.info()

    def delete_point(self):
        name = input("Name of the point: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                all_points.remove(element)
                print("successfully deleted")

    def rename_point(self):
        name = input("Name of the point: ")
        new_name = input("New name: ")
        for element in all_points:
            if element.name.lower() == name.lower():
                element.rename_point(new_name)
                print(f"successfully renamed too {new_name}")


    def all_points(self):
        for element in all_points:
            print(element.name, element.coordinates)


    def mirror_point(self):
        plane = input("With which plane / point / axis wo mirror: ")
        new_name = input("Name of the new point: ")
        name = input("Which point you want to mirror: ")
        try:
            all_points.append(mirror_point(plane, new_name, name, all_points))
        except:
            print("There has been a problem with your input.")


    def position_vector(self):
        point_name = input("Name of the point: ")
        try:
            for element in all_points:
                if element.name == point_name:
                    all_vectors.append(element.position_vector(point_name))

        except:
            print("There has been a problem with your input.")



    def vector(self):
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


    def vector_points(self):
        try:
            name = input("Name of the vector: ")
            pointA = input("Starting Point: ")
            pointB = input("End Point: ")
            all_vectors.append(create_vector_with_points(name, pointA, pointB, all_points))
        except:
            print("There has been a problem with your input.")


    def show_vector(self):
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                element.info()


    def all_vectors(self):
        for element in all_vectors:
            try:
                print(element.name, element.coordinates)
            except:
                print("Problem with this element")


    def delete_vector(self):
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.remove(element)
                print("successfully deleted")


    def rename_vector(self):
        name = input("Name of the vector: ")
        new_name = input("New name: ")
        try:
            for element in all_vectors:
                if element.name.lower() == name.lower():
                    element.rename_vector(new_name)
        except:
            print("There has been a problem with your vector")


    def magnitude_vector(self):
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                print(element.magnitude())


    def add_vectors(self):
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


    def subtract_vectors(self):
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



    def negative_vector(self):
        name = input("Name of the vector: ")
        for element in all_vectors:
            if element.name.strip().lower() == name.strip().lower():
                all_vectors.append(element.negative())


    def multiply_vector(self):
        vector = input("vector name: ")
        number = float(input("multiplied by: "))
        for element in all_vectors:
            if element.name == vector:
                element.scalar_multiplication(number)


    def scalar_product(self):
        vector1 = input("First vector: ")
        vector2 = input("Second vector: ")

        for element in all_vectors:
            if element.name == vector1:
                vector1 = element

            elif element.name == vector2:
                vector2 = element

        try:
            scalar_product(vector1, vector2)

        except:
            print("There has been an error with your vectors")



