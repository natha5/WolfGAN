import numpy as np
import pandas as pd


def read_into_array():

    maze_array = [["0"] * 64 for _ in range(64)]  # Initialize a 64x64 array with zeros
    object_array = [["0"] * 64 for _ in range(64)]


    with open(r"map_dataset\base_game\LEVEL01.HEX", 'r') as file:

        for _ in range(5): # skip first 5 lines
            file.readline()

        for i in range(64):
            line = file.read(128)  # Read 128 characters (64 values) at a time
            for j in range(64):
                value = line[j*2 : j*2+2]  # Extract the 2-character value
                maze_array[i][j] = str(value)
            file.readline()  # Skip the remaining characters in the line (if any)
    
        for _ in range(3): # skip 3 more lines
            file.readline()

        for i in range(64):
            line = file.read(128)  # Read 128 characters (64 values) at a time
            for j in range(64):
                value = line[j*2 : j*2+2]  # Extract the 2-character value
                object_array[i][j] = str(value)
            file.readline()  # Skip the remaining characters in the line (if any)

    return(maze_array,object_array)

