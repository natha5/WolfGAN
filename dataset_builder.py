import numpy as np
import pandas as pd


def read_into_array(file_path):

    maze_array = [["0"] * 64 for _ in range(64)]  # Initialize a 64x64 array with zeros
    object_array = [["0"] * 64 for _ in range(64)]


    with open(file_path, 'r') as file:

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


def determine_path(base_path):
    wall_list = []
    objects_list = []

    for i in range(1,60):
        if i < 10:
            current_path = base_path + r"\LEVEL0" + str(i) +".HEX"
        else:
            current_path = base_path + r"\LEVEL" + str(i) +".HEX"
        
        walls, objects = read_into_array(current_path)
        wall_list.append(walls)
        objects_list.append(objects)
    
    return (wall_list, objects_list)
        




full_walls_list = []
full_objects_list = []

walls, objects = determine_path(r"map_dataset\10newones")

full_walls_list.append(walls)
full_objects_list.append(objects)

walls, objects = determine_path(r"map_dataset\base_game")

full_walls_list.append(walls)
full_objects_list.append(objects)

walls, objects = determine_path(r"map_dataset\DHWTCSDL")

full_walls_list.append(walls)
full_objects_list.append(objects)

walls, objects = determine_path(r"map_dataset\Ipank")

full_walls_list.append(walls)
full_objects_list.append(objects)

walls, objects = determine_path(r"map_dataset\spear_v2.0")

full_walls_list.append(walls)
full_objects_list.append(objects)

walls, objects = determine_path(r"map_dataset\W3D-CMP")

full_walls_list.append(walls)
full_objects_list.append(objects)

full_walls_array = np.array(full_walls_list)
full_objects_array = np.array(full_objects_list)

print(full_walls_array.shape)

full_walls_array = np.reshape(full_walls_array,((59*6), (64*64)))
full_objects_array = np.reshape(full_objects_array,((59*6), (64*64)))


df = pd.DataFrame(full_walls_array)

df = pd.concat([df, pd.DataFrame(full_objects_array)], axis=1)

# create column names

column_names = []

for i in range(64*64):
    column_names.append("w"+ str(i+1))

for i in range(64*64):
    column_names.append("o" + str(i+1))


df.columns = column_names

print(df)



