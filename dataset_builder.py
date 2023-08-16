import numpy as np
import pandas as pd
import csv


def read_into_array(file_path):

    maze_array = [[0] * 64 for _ in range(64)]  # Initialize a 64x64 array with zeros
    #object_array = [["0"] * 64 for _ in range(64)]

    try:
        with open(file_path, 'r') as file:

            for _ in range(5): # skip first 5 lines
                file.readline()

            for i in range(64):
                line = file.read(128)  # Read 128 characters (64 values) at a time
                for j in range(64):
                    value = line[j*2 : j*2+2]  # Extract the 2-character value
                    maze_array[i][j] = hex_string_to_int(str(value))
                file.readline()  # Skip the remaining characters in the line (if any)
        return(maze_array)        
    except IOError:
        print("file does not exist, skipping")
        return 0


    


def determine_path(base_path, dataset_size):
    wall_list = []
    #objects_list = []

    for i in range(1,dataset_size + 1):
        if i < 10:
            current_path = base_path + r"/LEVEL0" + str(i) +".HEX"
        else:
            current_path = base_path + r"/LEVEL" + str(i) +".HEX"
        
        print("Map #" + str(i))

        walls = read_into_array(current_path)

        if walls == 0:
            print("going to next map")
        else:
            wall_list.append(walls)
        #objects_list.append(objects)
    
    return (wall_list)
        

def hex_string_to_int(value):
    decimal_value = int(value, 16)
    return decimal_value



walls = determine_path(r"map_dataset/10newones", 10)
full_walls_array = np.array(walls)

walls = determine_path(r"map_dataset/base_game", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/beltran", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/bunker", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/clonewar", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/DHWTCSDL", 30)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/Fox_v1.0", 43)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/Ipank" , 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/last_waltz" , 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/NACW3D" , 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/ragnarok", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/spear_v2.0", 29)
full_walls_array = np.append(full_walls_array, walls)

walls= determine_path(r"map_dataset/W3D-CMP", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/wlfbel_2", 60)
full_walls_array = np.append(full_walls_array, walls)

walls = determine_path(r"map_dataset/wlfbel_3", 60)
full_walls_array = np.append(full_walls_array, walls)




print(full_walls_array.shape)

no_of_lines = int(full_walls_array.shape[0] / 64)
no_of_maps = int(no_of_lines / 64)

print("No of maps=" + str(no_of_maps))

full_walls_array = full_walls_array.reshape(no_of_lines,64)

print(full_walls_array.shape)


np.savetxt('dataset.csv', full_walls_array, delimiter=',', fmt='%i')