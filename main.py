# This is the python script for my 3DSpace programm
# It is a mathematical application for the geometry in 3D Space
# If you do it right it also works for 2D Space
# I will comment the rest of the code as well to make the script understandable
# In the programm you can type help and all commands with explanation will be
# shown to the user in the same window.
# The coordinates are shown in [[x],[y],[z]] because with this matrix multiplication
# can be implemented easily as well.

#So far the programm lacks with updating infos like the points the vector originally got created on.
#There will be patches for that in the future.

# the necessary libraries for the project and also the functions from this project in other files
from Classes.Commands import Commands

####################START OF THE PROGRAMM########
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

#dictionary with all the commands that are stored in the Commands class for an easy access
Commands = Commands()
command_dict = {
    "exit": exit,
    "reset": Commands.reset,
    "help": Commands.help,
    "point": Commands.point,
    "show point": Commands.show_point,
    "delete point": Commands.delete_point,
    "rename point": Commands.rename_point,
    "all points": Commands.all_points,
    "mirror point": Commands.mirror_point,
    "position vector": Commands.position_vector,
    "vector": Commands.vector,
    "vector points": Commands.vector_points,
    "delete vector": Commands.delete_vector,
    "show vector": Commands.show_vector,
    "rename vector": Commands.rename_vector,
    "all vectors": Commands.all_vectors,
    "magnitude vector": Commands.magnitude_vector,
    "add vectors": Commands.add_vectors,
    "subtract vectors": Commands.subtract_vectors,
    "negative vector": Commands.negative_vector,
    "multiply vector": Commands.multiply_vector,
    "scalar product": Commands.scalar_product
}

# Having the while loop as the start
if __name__ == '__main__':
    while True:

        user_input = input("> ")
        # for the rest its always if statements which command the user typed
        # and we use more input() functions to get the necessary information
        # to call the corresponding function
        if user_input.lower() in command_dict:
            command = command_dict[user_input.lower()]
            command()