"""This utility creates directories for the Sleuth files for University
of London's 'Intro to Programming I' course.

Run the program in the folder where you want to create the directories.
You can create all the directories, or just the rookie/pro stages."""

import os

# get current directory
CURRENT_PATH = os.getcwd()
SUB_PATHS = [1, 2, 3, 4]


def create_structure():
    """Create directories and sub-directories required for rookie and
    pro stages of Sleuth cases."""

    print("Files are created in the working directory.")
    print("Which folders do you want to create?")

    # prompt user for input and repeat if invalid
    answer = None
    valid_inputs = ["a", "r", "p", "x"]
    while answer not in valid_inputs:
        answer = input("(A)ll (R)ookie (P)ro, or e(X)it: ")
        answer = answer.lower()

    if answer == "a":
        create_rookie()
        create_pro()
        print("Complete")
    elif answer == "r":
        create_rookie()
        print("Complete")
    elif answer == "p":
        create_pro()
        print("Complete")
    else:
        exit()


def create_rookie():
    """Create rookie folder function."""

    # create arrays for parent folders and sub folders
    parent_paths = [101, 201, 202, 301, 302, 303, 401, 402, 403]

    # loop for creating 9 parent folders, each 4 with sub folders
    for directory in parent_paths:
        new_parent_path = CURRENT_PATH + "/{}".format(directory)
        os.mkdir(new_parent_path)

        for sub_directory in SUB_PATHS:
            new_sub_path = new_parent_path + "/{}".format(sub_directory)
            os.mkdir(new_sub_path)


def create_pro():
    """Create pro folder function"""

    # create arrays for parent folders and sub folders
    parent_paths = [501, 502, 601, 701, 702, 801, 802]

    # loop for creating 7 parent folders, each 4 with sub folders
    for directory in parent_paths:
        new_parent_path = CURRENT_PATH + "/{}".format(directory)
        os.mkdir(new_parent_path)

        for sub_directory in SUB_PATHS:
            new_sub_path = new_parent_path + "/{}".format(sub_directory)
            os.mkdir(new_sub_path)


# execute functions according to user input
if __name__ == "__main__":
    create_structure()
