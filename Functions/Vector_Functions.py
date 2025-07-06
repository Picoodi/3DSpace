from Classes.Vector_Class import Vector
from Classes.Point_Class import Point

from math import acos, degrees


def create_vector(name, x, y, z):
    # just putting the input into the right list format
    list_of_coordinates = [[x],
                           [y],
                           [z]]

    # we create a point that is the tip of the vector
    VectorTip = Point(f"tip_of_{name}", list_of_coordinates)

    #creating the vector object
    return Vector(name, list_of_coordinates, "origin", f"tip_of_{name}") , VectorTip





# creates a vector with two given points
def create_vector_with_points(name, pointA, pointB, all_points):
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

    if pointA_exists and pointB_exists == True:  # if the points don't exist we give back a fail
        # creating the mathematical vector
        vector_coordinates = [[pointB_coordinates[0][0] - pointA_coordinates[0][0]],
                              [pointB_coordinates[1][0] - pointA_coordinates[1][0]],
                              [pointB_coordinates[2][0] - pointA_coordinates[2][0]]
                              ]

        # creating the vector object
        return Vector(name, vector_coordinates, pointA, pointB)


    else:
        print("sry there has been a problem with your points")




def add_vectors(VectorA, VectorB, new_name):
    # we take two vectors and try to add them together
    new_coordinates = [[VectorA.x + VectorB.x],
                       [VectorA.y + VectorB.y],
                       [VectorA.z + VectorB.z]]

    return Vector(new_name, new_coordinates, None, None)








def subtract_vectors(VectorA, VectorB, new_name):
    try:
        new_coordinates = [[VectorA.x - VectorB.x],
                           [VectorA.y - VectorB.y],
                           [VectorA.z - VectorB.z]]

        print(f"Vector {new_name} with the coordinates {new_coordinates} got created successfully.")
        return Vector(new_name, new_coordinates, None, None)

    except:
        print("There has been a problem with the Vectors of yours.")






#function for calculating the scalar porduct and the angles between two vectors
def scalar_product(vector1, vector2):
    scalar = vector1.x * vector2.x + vector1.y * vector2.y + vector1.z * vector2.z #scalar through the coordinates
    angle_radian = acos(scalar / (vector1.magnitude() * vector2.magnitude())) #formula for the angle
    angle_degrees = degrees(angle_radian) #acos above gives back the radian, here we calculate it to degrees

    if scalar == 0:
        print("The vectors are orthogonal which means a 90 degree angle.")

    else:
        print(f"The vectors have a scalar of {scalar} and an angle of {angle_radian} radian or {angle_degrees} degrees")



def cross_product(vectorA, vectorB, new_name):
    new_vector = [
        [vectorA.y * vectorB.z - vectorA.z * vectorB.y],
        [vectorA.z * vectorB.x - vectorA.x * vectorB.z],
        [vectorA.x * vectorB.y - vectorA.y * vectorB.x]
    ]

    return Vector(new_name, new_vector, None, None)