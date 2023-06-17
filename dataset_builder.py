import numpy as np
import pandas as pd

current_file = open(r"map_dataset\base_game\LEVEL01.HEX","r")

current_maze = current_file.readlines()

# now, put the maze data into a list


maze = np.zeros((64,64), str)

for i in range(64):
    for j in range(64):
        for k in range(0,128,2):
            maze[i][j] = str(current_maze[i + 5])[k:k+2]

print(maze)