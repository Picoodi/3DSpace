from Classes.Point_Class import Point

def create_point(name, x, y, z):
    # just putting the input into the right list format
    list_of_coordinates = [[x],
                           [y],
                           [z]]

    # creating a successful message and creating the point object and adding it to the all_points list
    print(f"Point {name} with the coordinates {list_of_coordinates} got created successfully.")
    return Point(name, list_of_coordinates)




# not jet finished the mirror function. Point and axis mirroring still need to be implemented
def mirror_point(plane, new_name, point_name, list_of_all_points):
    # plane where the point will be mirrored can be o aka origin , xy, xz, yz
    list_of_coordinates = []
    new_coordinates = []

    # We need the original coordinates of the point from the all_points list
    for element in list_of_all_points:
        if element.name == point_name:
            list_of_coordinates = element.coordinates

    # we check which plane it is and change the coordinates accordingly
    if plane == "o":  # Every coordinate times -1
        new_coordinates = [[list_of_coordinates[0][0] * -1],
                           [list_of_coordinates[1][0] * -1],
                           [list_of_coordinates[2][0] * -1]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "xy":  # the z coordinate times -1
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0] * -1]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "xz":  # the y coordinate times -1
        new_coordinates = [[list_of_coordinates[0][0]],
                           [list_of_coordinates[1][0] * -1],
                           [list_of_coordinates[2][0]]]
        new_point = Point(new_name, new_coordinates)

    elif plane == "yz":  # the x coordinate times -1
        new_coordinates = [[list_of_coordinates[0][0] * -1],
                           [list_of_coordinates[1][0]],
                           [list_of_coordinates[2][0]]]
        new_point = Point(new_name, new_coordinates)


    # For the next planes, geometrically we create a vector to the point we want
    # to mirror through. We double its magnitude and calculate the new_coordinates
    # of the new point with the original point plus the vector.

    elif plane == "x":  # Point on x-Axis is (x from point /0/0)
        mirror_vector_coordinates = [[2 * (list_of_coordinates[0][0] - list_of_coordinates[0][0])],
                                     [2 * (0 - list_of_coordinates[1][0])],
                                     [2 * (0 - list_of_coordinates[2][0])]
                                     ]

        new_coordinates = [[list_of_coordinates[0][0] + mirror_vector_coordinates[0][0]],
                           [list_of_coordinates[1][0] + mirror_vector_coordinates[1][0]],
                           [list_of_coordinates[2][0] + mirror_vector_coordinates[2][0]]
                           ]

        new_point = Point(new_name, new_coordinates)


    elif plane == "y":  # Point on x-Axis is (0/y from point /0)
        mirror_vector_coordinates = [[2 * (0 - list_of_coordinates[0][0])],
                                     [2 * (list_of_coordinates[1][0] - list_of_coordinates[1][0])],
                                     [2 * (0 - list_of_coordinates[2][0])]
                                     ]

        new_coordinates = [[list_of_coordinates[0][0] + mirror_vector_coordinates[0][0]],
                           [list_of_coordinates[1][0] + mirror_vector_coordinates[1][0]],
                           [list_of_coordinates[2][0] + mirror_vector_coordinates[2][0]]
                           ]

        new_point = Point(new_name, new_coordinates)


    elif plane == "z":  # Point on x-Axis is (0/0/z from point)
        mirror_vector_coordinates = [[2 * (0 - list_of_coordinates[0][0])],
                                     [2 * (0 - list_of_coordinates[1][0])],
                                     [2 * (list_of_coordinates[2][0] - list_of_coordinates[2][0])]
                                     ]

        new_coordinates = [[list_of_coordinates[0][0] + mirror_vector_coordinates[0][0]],
                           [list_of_coordinates[1][0] + mirror_vector_coordinates[1][0]],
                           [list_of_coordinates[2][0] + mirror_vector_coordinates[2][0]]
                           ]

        new_point = Point(new_name, new_coordinates)



    elif plane == "point":  # Here we create the vector between the two points, double and create the new point
        mirror_point = input("Mirror point: ")
        mirror_point_coordinates = []
        for element in list_of_all_points:
            if element.name == mirror_point:
                mirror_point_coordinates = element.coordinates

        mirror_vector_coordinates = [[2 * (mirror_point_coordinates[0][0] - list_of_coordinates[0][0])],
                                     [2 * (mirror_point_coordinates[1][0] - list_of_coordinates[1][0])],
                                     [2 * (mirror_point_coordinates[2][0] - list_of_coordinates[2][0])]
                                     ]

        new_coordinates = [[list_of_coordinates[0][0] + mirror_vector_coordinates[0][0]],
                           [list_of_coordinates[1][0] + mirror_vector_coordinates[1][0]],
                           [list_of_coordinates[2][0] + mirror_vector_coordinates[2][0]]
                           ]

        print(new_coordinates)
        new_point = Point(new_name, new_coordinates)


    # If the input of the plane ist not right we give that back to the user and break the function with None return
    else:
        print("Sry your plane to mirror is not defined. See the help page for more infos.")
        return None

    # If everything worked we create a new Point object and add it to all_points list
    print(f"Point {new_name} with the coordinates {new_coordinates} got created successfully.")
    return new_point