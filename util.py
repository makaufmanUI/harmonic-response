"""
# util.py

Utility functions for Frequency Response simulation data.

Data files should be stored in a directory structure such as:
```txt
sim1/
    data/
        acceleration/       # acceleration frequency response data
            DIMM1.txt
            DIMM2.txt
            DIMM3.txt
            ...
        deformation/        # deformation frequency response data
            DIMM1.txt
            DIMM2.txt
            DIMM3.txt
            ...
        velocity/           # velocity frequency response data
            DIMM1.txt
            DIMM2.txt
            DIMM3.txt
            ...
```
"""

import re
import os
import numpy as np
import pandas as pd
from typing import NamedTuple
from collections import namedtuple





def get_data_files(parent_folder: str, pattern: str = '.*\.txt') -> NamedTuple:
    """
    Return a list of simulation data files from a parent folder.

    ## Example
    ```python
    data_files = get_data_files("sim1")
    
    print(data_files.velocity)
        ['DIMM1.txt', 'DIMM2.txt', 'DIMM3.txt', ...]
    print(data_files.deformation)
        ['DIMM1.txt', 'DIMM2.txt', 'DIMM3.txt', ...]
    print(data_files.acceleration)
        ['DIMM1.txt', 'DIMM2.txt', 'DIMM3.txt', ...]
    ```
    """
    velocity_files = []
    deformation_files = []
    acceleration_files = []
    velocity_path = f"{parent_folder}/data/velocity/"
    deformation_path = f"{parent_folder}/data/deformation/"
    acceleration_path = f"{parent_folder}/data/acceleration/"
    for file in os.listdir(velocity_path):
        if re.search(pattern, file):
            velocity_files.append(file)
    for file in os.listdir(deformation_path):
        if re.search(pattern, file):
            deformation_files.append(file)
    for file in os.listdir(acceleration_path):
        if re.search(pattern, file):
            acceleration_files.append(file)
    data_files = namedtuple("data_files", ["velocity", "deformation", "acceleration"])
    return data_files(velocity_files, deformation_files, acceleration_files)





def get_deformation_data_files(parent_folder: str, pattern: str = '.*\.txt') -> NamedTuple:
    """
    Return a list of deformation simulation data files from a parent folder.

    ## Example
    """
    deformation_files_x = []
    deformation_files_y = []
    deformation_files_z = []
    deformation_path = f"{parent_folder}/data/deformation/"
    for file in os.listdir(deformation_path):
        if re.search(pattern, file):
            if 'x.txt' in file:
                deformation_files_x.append(file)
            elif 'y.txt' in file:
                deformation_files_y.append(file)
            elif 'z.txt' in file:
                deformation_files_z.append(file)
    deformation_data_files = namedtuple("deformation_data_files", ["x", "y", "z"])
    return deformation_data_files(deformation_files_x, deformation_files_y, deformation_files_z)





def get_acceleration_data_files(parent_folder: str, pattern: str = '.*\.txt') -> NamedTuple:
    """
    Return a list of acceleration simulation data files from a parent folder.

    ## Example
    """
    acceleration_files_x = []
    acceleration_files_y = []
    acceleration_files_z = []
    acceleration_path = f"{parent_folder}/data/acceleration/"
    for file in os.listdir(acceleration_path):
        if re.search(pattern, file):
            if 'x.txt' in file:
                acceleration_files_x.append(file)
            elif 'y.txt' in file:
                acceleration_files_y.append(file)
            elif 'z.txt' in file:
                acceleration_files_z.append(file)
    acceleration_data_files = namedtuple("acceleration_data_files", ["x", "y", "z"])
    return acceleration_data_files(acceleration_files_x, acceleration_files_y, acceleration_files_z)






def get_velocity_data_files(parent_folder: str, pattern: str = '.*\.txt') -> NamedTuple:
    """
    Return a list of velocity simulation data files from a parent folder.

    ## Example
    """
    velocity_files_x = []
    velocity_files_y = []
    velocity_files_z = []
    velocity_path = f"{parent_folder}/data/velocity/"
    for file in os.listdir(velocity_path):
        if re.search(pattern, file):
            if 'x.txt' in file:
                velocity_files_x.append(file)
            elif 'y.txt' in file:
                velocity_files_y.append(file)
            elif 'z.txt' in file:
                velocity_files_z.append(file)
    velocity_data_files = namedtuple("velocity_data_files", ["x", "y", "z"])
    return velocity_data_files(velocity_files_x, velocity_files_y, velocity_files_z)





# def get_velocity_data(parent_folder: str) -> NamedTuple:
#     """
#     Return a namedtuple of Pandas `DataFrame`s for velocity data of each DIMM in a simulation.

#     ## Example
#     ```python
#     velocity_data = get_velocity_data("sim1")
    
#     print(velocity_data.DIMM1)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     print(velocity_data.DIMM2)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     print(velocity_data.DIMM3)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     ```
#     """
#     data_files = get_data_files(parent_folder)
#     velocity_dataframes = []
#     for file in data_files.velocity:
#         with open(file, 'r') as f:
#             lines = f.readlines()
#         with open(file, 'w') as f:
#             for line in lines:
#                 if 'Angle' in line:
#                     f.write(line[:line.find('Angle')+5] + ' [deg]\n')
#                 else:
#                     f.write(line)
#         df = pd.read_csv(file, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
#         df['Amplitude'] *= 1e3
#         velocity_dataframes.append(df)
#     velocity_data = namedtuple("velocity_data", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
#     return velocity_data(*velocity_dataframes)





def get_deformation_data(parent_folder: str) -> NamedTuple:
    """
    Return a namedtuple of Pandas `DataFrame`s for deformation data of each DIMM in a simulation.

    ## Example
    ```python
    deformation_data = get_deformation_data("sim1")
    
    print(deformation_data.DIMM1)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(deformation_data.DIMM2)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(deformation_data.DIMM3)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    ```
    """
    deformation_data_files = get_deformation_data_files(parent_folder)
    deformation_dataframes_x = []
    for file in deformation_data_files.x:
        with open(f"{parent_folder}/data/deformation/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/deformation/{file}", 'w') as f:
            for line in lines:
                if 'Angle' in line:
                    f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                else:
                    f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        df['Amplitude'] *= 1e3
        deformation_dataframes_x.append(df)
    deformation_dataframes_y = []
    for file in deformation_data_files.y:
        with open(f"{parent_folder}/data/deformation/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/deformation/{file}", 'w') as f:
            for line in lines:
                if 'Angle' in line:
                    f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                else:
                    f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        df['Amplitude'] *= 1e3
        deformation_dataframes_y.append(df)
    deformation_dataframes_z = []
    for file in deformation_data_files.z:
        with open(f"{parent_folder}/data/deformation/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/deformation/{file}", 'w') as f:
            for line in lines:
                if 'Angle' in line:
                    f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                else:
                    f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/deformation/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        df['Amplitude'] *= 1e3
        deformation_dataframes_z.append(df)
    deformation_data = namedtuple("deformation_data", ["x", "y", "z"])
    deformation_data_x = namedtuple("deformation_data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    deformation_data_y = namedtuple("deformation_data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    deformation_data_z = namedtuple("deformation_data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    return deformation_data(deformation_data_x(*deformation_dataframes_x), deformation_data_y(*deformation_dataframes_y), deformation_data_z(*deformation_dataframes_z))
    # return deformation_data_x(*deformation_dataframes_x), deformation_data_y(*deformation_dataframes_y), deformation_data_z(*deformation_dataframes_z)







def get_acceleration_data(parent_folder: str) -> NamedTuple:
    """
    Return a namedtuple of Pandas `DataFrame`s for acceleration data of each DIMM in a simulation.

    ## Example
    ```python
    acceleration_data = get_acceleration_data("sim1")
    
    print(acceleration_data.DIMM1)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(acceleration_data.DIMM2)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(acceleration_data.DIMM3)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    ```
    """
    acceleration_data_files = get_acceleration_data_files(parent_folder)
    acceleration_dataframes_x = []
    for file in acceleration_data_files.x:
        with open(f"{parent_folder}/data/acceleration/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/acceleration/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s2]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line and 'deg' not in line:
                #     f.write(line[:line.find('Amplitude')+9] + ' [m/s2]' + line[line.find('Amplitude')+18:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        # add a new 'Amplitude_g' column to the dataframe
        df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
        acceleration_dataframes_x.append(df)
    acceleration_dataframes_y = []
    for file in acceleration_data_files.y:
        with open(f"{parent_folder}/data/acceleration/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/acceleration/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s2]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line and 'deg' not in line:
                #     f.write(line[:line.find('Amplitude')+9] + ' [m/s2]' + line[line.find('Amplitude')+18:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        # df['Amplitude_g'] = df['Amplitude_g'] / 9.81
        df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
        acceleration_dataframes_y.append(df)
    acceleration_dataframes_z = []
    for file in acceleration_data_files.z:
        with open(f"{parent_folder}/data/acceleration/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/acceleration/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s2]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line and 'deg' not in line:
                #     f.write(line[:line.find('Amplitude')+9] + ' [m/s2]' + line[line.find('Amplitude')+18:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/acceleration/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        # df['Amplitude_g'] = df['Amplitude_g'] / 9.81
        df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
        acceleration_dataframes_z.append(df)
    acceleration_data = namedtuple("acceleration_data", ["x", "y", "z"])
    acceleration_data_x = namedtuple("acceleration_data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    acceleration_data_y = namedtuple("acceleration_data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    acceleration_data_z = namedtuple("acceleration_data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    return acceleration_data(acceleration_data_x(*acceleration_dataframes_x), acceleration_data_y(*acceleration_dataframes_y), acceleration_data_z(*acceleration_dataframes_z))







def get_velocity_data(parent_folder: str) -> NamedTuple:
    """
    Return a namedtuple of Pandas `DataFrame`s for velocity data of each DIMM in a simulation.

    ## Example
    ```python
    velocity_data = get_velocity_data("sim1")
    
    print(velocity_data.DIMM1)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(velocity_data.DIMM2)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    print(velocity_data.DIMM3)
            Frequency  Amplitude  Phase Angle
        0   1.0        1.0        1.0
        1   2.0        2.0        2.0
        2   3.0        3.0        3.0
    ```
    """
    velocity_data_files = get_velocity_data_files(parent_folder)
    velocity_dataframes_x = []
    for file in velocity_data_files.x:
        with open(f"{parent_folder}/data/velocity/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/velocity/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line:
                #     f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        velocity_dataframes_x.append(df)
    velocity_dataframes_y = []
    for file in velocity_data_files.y:
        with open(f"{parent_folder}/data/velocity/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/velocity/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line:
                #     f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        velocity_dataframes_y.append(df)
    velocity_dataframes_z = []
    for file in velocity_data_files.z:
        with open(f"{parent_folder}/data/velocity/{file}", 'r') as f:
            lines = f.readlines()
        with open(f"{parent_folder}/data/velocity/{file}", 'w') as f:
            for line in lines:
                if line == lines[0]:
                    f.write("\tFrequency [Hz]\tAmplitude [m/s]\tPhase Angle [deg]\n")
                else:
                    f.write(line)
                # if 'Angle' in line:
                #     f.write(line[:line.find('Angle')+5] + ' [deg]\n')
                # else:
                #     f.write(line)
        df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
        # df = pd.read_csv(f"{parent_folder}/data/velocity/{file}", sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
        velocity_dataframes_z.append(df)
    velocity_data = namedtuple("velocity_data", ["x", "y", "z"])
    velocity_data_x = namedtuple("velocity_data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    velocity_data_y = namedtuple("velocity_data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    velocity_data_z = namedtuple("velocity_data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    return velocity_data(velocity_data_x(*velocity_dataframes_x), velocity_data_y(*velocity_dataframes_y), velocity_data_z(*velocity_dataframes_z))










# def get_acceleration_data2(parent_folder: str) -> NamedTuple:
#     """
#     Return a namedtuple of Pandas `DataFrame`s for acceleration data of each DIMM in a simulation.

#     ## Example
#     ```python
#     acceleration_data = get_acceleration_data("sim1")
    
#     print(acceleration_data.DIMM1)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     print(acceleration_data.DIMM2)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     print(acceleration_data.DIMM3)
#             Frequency  Amplitude  Phase Angle
#         0   1.0        1.0        1.0
#         1   2.0        2.0        2.0
#         2   3.0        3.0        3.0
#     ```
#     """
#     data_files = get_data_files(parent_folder)
#     acceleration_dataframes = []
#     for file in data_files.acceleration:
#         with open(file, 'r') as f:
#             lines = f.readlines()
#         with open(file, 'w') as f:
#             for line in lines:
#                 if 'Angle' in line:
#                     f.write(line[:line.find('Angle')+5] + ' [deg]\n')
#                 else:
#                     f.write(line)
#         df = pd.read_csv(file, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'], index_col=0)
#         df['Amplitude'] *= 1e3
#         acceleration_dataframes.append(df)
#     acceleration_data = namedtuple("acceleration_data", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
#     return acceleration_data(*acceleration_dataframes)






def describe(data: NamedTuple, data_type: str, axis: str, save_as: str = None) -> None:
    """
    Describe the simulation data.

    ## Parameters
    - `data`: A namedtuple of Pandas `DataFrame`s, each containing data for a DIMM.
    - `data_type`: The type of data. Must be one of `["velocity", "acceleration", "deformation"]`.
    - `axis`: The axis of the data. Must be one of `["x", "y", "z"]`.
    - `save_as` (Optional): If provided, the descriptive data will be saved as a file with the given name.
    """
    if not save_as:
        print("\n")
        for i, d in enumerate(data):
            print(f"DIMM{i+1}")
            print(d.describe())
            print("\n")
    if save_as:
        if '.txt' not in save_as:
            save_as += '.txt'
        print(f"{data_type.title()} ({axis.title()}) Description\n" + ('-'*(len(data_type) + 16)) + '\n\n', file=open(save_as, 'w'))
        with open(save_as, 'a') as f:
            for i, d in enumerate(data):
                print(f"DIMM{i+1}\n" + ('-'*5), file=f)
                print(d.describe(), file=f)
                if i != 7: print("\n\n", file=f)







def load_dfs_from_description__acceleration(filepath: str) -> NamedTuple:
    """
    Loads the acceleration DIMM data from a description file.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[6:]
    DIMM1_lines = lines[:9]
    DIMM2_lines = lines[14:23]
    DIMM3_lines = lines[28:37]
    DIMM4_lines = lines[42:51]
    DIMM5_lines = lines[56:65]
    DIMM6_lines = lines[70:79]
    DIMM7_lines = lines[84:93]
    DIMM8_lines = lines[98:107]

    def d(lines):
        lines[0] = '\t' + lines[0]
        lines = lines[:1] + lines[2:]
        return lines
    
    DIMM1_lines = d(DIMM1_lines)
    DIMM2_lines = d(DIMM2_lines)
    DIMM3_lines = d(DIMM3_lines)
    DIMM4_lines = d(DIMM4_lines)
    DIMM5_lines = d(DIMM5_lines)
    DIMM6_lines = d(DIMM6_lines)
    DIMM7_lines = d(DIMM7_lines)
    DIMM8_lines = d(DIMM8_lines)

    def to_df(lines):
        """
        Structure of lines:
        lines[0] = '\t' + "Frequency" + '\t' + "Amplitude_g" + '\t' + "Amplitude" + '\t' + "Phase Angle"
        lines[1] = "mean" + '\t' + str(mean) + '\t' + str(mean) + '\t' + str(mean) + '\t' + str(mean)
        lines[2] = "std" + '\t' + str(std) + '\t' + str(std) + '\t' + str(std) + '\t' + str(std)
        lines[3] = "min" + '\t' + str(min) + '\t' + str(min) + '\t' + str(min) + '\t' + str(min)
        lines[4] = "25%" + '\t' + str(25%) + '\t' + str(25%) + '\t' + str(25%) + '\t' + str(25%)
        lines[5] = "50%" + '\t' + str(50%) + '\t' + str(50%) + '\t' + str(50%) + '\t' + str(50%)
        lines[6] = "75%" + '\t' + str(75%) + '\t' + str(75%) + '\t' + str(75%) + '\t' + str(75%)
        lines[7] = "max" + '\t' + str(max) + '\t' + str(max) + '\t' + str(max) + '\t' + str(max)
        """
        rows = [line.split(r'\s+') for line in lines]
        rows = [r[0] for r in rows]
        columns = rows[0].split('\t')
        columns = [c.split(' ') for c in columns[1:]][0]
        columns = columns[:-1]
        columns[-1] = columns[-1] + "_Angle"
        newcolumns = []
        for c in columns:
            if len(c) > 1:
                newcolumns.append(c)
        columns = newcolumns
        rows = rows[1:]
        rows = [r.split(' ') for r in rows]
        rows = [r[1:] for r in rows]
        newrows = []
        for r in rows:
            r3 = []
            for r2 in r:
                if len(r2) > 1:
                    r3.append(r2)
            newrows.append(r3)
        rows = newrows
        df = pd.DataFrame(rows, columns=columns)
        columns = list(df.columns)
        columns[1], columns[2] = columns[2], columns[1]
        rows = df.values.tolist()
        for r in rows:
            r[1], r[2] = r[2], r[1]
        df2 = pd.DataFrame(rows, columns=columns)
        df2['Frequency'] = df2['Frequency'].astype(float).map(lambda x: '{:.4f}'.format(x))
        df2['Frequency'] = df2['Frequency'].astype(str)
        df2['Frequency'] = df2['Frequency'].map(lambda x: x[:5])
        df2['Amplitude'] = df2['Amplitude'].astype(float).map(lambda x: '{:.4f}'.format(round(x, 4)))
        df2['Amplitude'] = df2['Amplitude'].astype(str)
        df2['Amplitude'] = df2['Amplitude'].map(lambda x: x[:6])
        df2['Amplitude_g'] = df2['Amplitude_g'].astype(float).map(lambda x: '{:.4f}'.format(round(x, 4)))
        df2['Amplitude_g'] = df2['Amplitude_g'].astype(str)
        df2['Amplitude_g'] = df2['Amplitude_g'].map(lambda x: x[:6])
        df2['Phase_Angle'] = df2['Phase_Angle'].astype(float).map(lambda x: '{:.4f}'.format(round(x, 3)))
        df2['Phase_Angle'] = df2['Phase_Angle'].astype(str)
        df2['Phase_Angle'] = df2['Phase_Angle'].map(lambda x: x[:6] if float(x) < 0 else x[:5])
        return df2
    
    DIMM1_df = to_df(DIMM1_lines)
    DIMM2_df = to_df(DIMM2_lines)
    DIMM3_df = to_df(DIMM3_lines)
    DIMM4_df = to_df(DIMM4_lines)
    DIMM5_df = to_df(DIMM5_lines)
    DIMM6_df = to_df(DIMM6_lines)
    DIMM7_df = to_df(DIMM7_lines)
    DIMM8_df = to_df(DIMM8_lines)

    acceleration_data = namedtuple("acceleration_data", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    return acceleration_data(DIMM1_df, DIMM2_df, DIMM3_df, DIMM4_df, DIMM5_df, DIMM6_df, DIMM7_df, DIMM8_df)








def load_dfs_from_description__velocity_deformation(filepath: str) -> NamedTuple:
    """
    Loads the velocity DIMM data from a description file.
    """
    with open(filepath, 'r') as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    lines = lines[6:]
    DIMM1_lines = lines[:9]
    DIMM2_lines = lines[14:23]
    DIMM3_lines = lines[28:37]
    DIMM4_lines = lines[42:51]
    DIMM5_lines = lines[56:65]
    DIMM6_lines = lines[70:79]
    DIMM7_lines = lines[84:93]
    DIMM8_lines = lines[98:107]

    def d(lines):
        lines[0] = '\t' + lines[0]
        lines = lines[:1] + lines[2:]
        return lines
    
    DIMM1_lines = d(DIMM1_lines)
    DIMM2_lines = d(DIMM2_lines)
    DIMM3_lines = d(DIMM3_lines)
    DIMM4_lines = d(DIMM4_lines)
    DIMM5_lines = d(DIMM5_lines)
    DIMM6_lines = d(DIMM6_lines)
    DIMM7_lines = d(DIMM7_lines)
    DIMM8_lines = d(DIMM8_lines)

    def to_df(lines):
        """
        Structure of lines:
        lines[0] = '\t' + "Frequency" + '\t' + "Amplitude" + '\t' + "Phase Angle"
        lines[1] = "mean" + '\t' + str(mean) + '\t' + str(mean) + '\t' + str(mean)
        lines[2] = "std" + '\t' + str(std) + '\t' + str(std) + '\t' + str(std)
        lines[3] = "min" + '\t' + str(min) + '\t' + str(min) + '\t' + str(min)
        lines[4] = "25%" + '\t' + str(25%) + '\t' + str(25%) + '\t' + str(25%)
        lines[5] = "50%" + '\t' + str(50%) + '\t' + str(50%) + '\t' + str(50%)
        lines[6] = "75%" + '\t' + str(75%) + '\t' + str(75%) + '\t' + str(75%)
        lines[7] = "max" + '\t' + str(max) + '\t' + str(max) + '\t' + str(max)
        """
        rows = [line.split(r'\s+') for line in lines]
        rows = [r[0] for r in rows]
        columns = rows[0].split('\t')
        columns = [c.split(' ') for c in columns[1:]][0]
        columns = columns[:-1]
        columns[-1] = columns[-1] + "_Angle"
        newcolumns = []
        for c in columns:
            if len(c) > 1:
                newcolumns.append(c)
        columns = newcolumns
        rows = rows[1:]
        rows = [r.split(' ') for r in rows]
        rows = [r[1:] for r in rows]
        newrows = []
        for r in rows:
            r3 = []
            for r2 in r:
                if len(r2) > 1:
                    r3.append(r2)
            newrows.append(r3)
        rows = newrows
        df = pd.DataFrame(rows, columns=columns)
        # columns = list(df.columns)
        # columns[1], columns[2] = columns[2], columns[1]
        # rows = df.values.tolist()
        # for r in rows:
        #     r[1], r[2] = r[2], r[1]
        df2 = pd.DataFrame(rows, columns=columns)
        df2['Frequency'] = df2['Frequency'].astype(float).map(lambda x: '{:.4f}'.format(x))
        df2['Frequency'] = df2['Frequency'].astype(str)
        df2['Frequency'] = df2['Frequency'].map(lambda x: x[:5])
        df2['Amplitude'] = df2['Amplitude'].astype(float).map(lambda x: '{:.6f}'.format(round(x, 6)))
        df2['Amplitude'] = df2['Amplitude'].astype(str)
        df2['Amplitude'] = df2['Amplitude'].map(lambda x: x[:8])
        # df2['Amplitude_g'] = df2['Amplitude_g'].astype(float).map(lambda x: '{:.4f}'.format(round(x, 4)))
        # df2['Amplitude_g'] = df2['Amplitude_g'].astype(str)
        # df2['Amplitude_g'] = df2['Amplitude_g'].map(lambda x: x[:6])
        df2['Phase_Angle'] = df2['Phase_Angle'].astype(float).map(lambda x: '{:.4f}'.format(round(x, 3)))
        df2['Phase_Angle'] = df2['Phase_Angle'].astype(str)
        df2['Phase_Angle'] = df2['Phase_Angle'].map(lambda x: x[:6] if float(x) < 0 else x[:5])
        return df2
    
    DIMM1_df = to_df(DIMM1_lines)
    DIMM2_df = to_df(DIMM2_lines)
    DIMM3_df = to_df(DIMM3_lines)
    DIMM4_df = to_df(DIMM4_lines)
    DIMM5_df = to_df(DIMM5_lines)
    DIMM6_df = to_df(DIMM6_lines)
    DIMM7_df = to_df(DIMM7_lines)
    DIMM8_df = to_df(DIMM8_lines)

    acceleration_data = namedtuple("acceleration_data", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
    return acceleration_data(DIMM1_df, DIMM2_df, DIMM3_df, DIMM4_df, DIMM5_df, DIMM6_df, DIMM7_df, DIMM8_df)









def write_dfs_to_google_sheets__acceleration(df_namedtuple: NamedTuple) -> None:
    """
    Writes the acceleration data to Google Sheets.
    """
    from stuff import GoogleSheets
    sheet = GoogleSheets("PythonTest")
    sheet.clear_worksheet()
    d1, d2, d3, d4, d5, d6, d7, d8 = df_namedtuple
    sheet.set_acell_contents_range("B1:E8", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d1['Frequency'][0]}", f"{d1['Amplitude'][0]}", f"{d1['Amplitude_g'][0]}", f"{d1['Phase_Angle'][0]}"],
            [f"{d1['Frequency'][1]}", f"{d1['Amplitude'][1]}", f"{d1['Amplitude_g'][1]}", f"{d1['Phase_Angle'][1]}"],
            [f"{d1['Frequency'][2]}", f"{d1['Amplitude'][2]}", f"{d1['Amplitude_g'][2]}", f"{d1['Phase_Angle'][2]}"],
            [f"{d1['Frequency'][3]}", f"{d1['Amplitude'][3]}", f"{d1['Amplitude_g'][3]}", f"{d1['Phase_Angle'][3]}"],
            [f"{d1['Frequency'][4]}", f"{d1['Amplitude'][4]}", f"{d1['Amplitude_g'][4]}", f"{d1['Phase_Angle'][4]}"],
            [f"{d1['Frequency'][5]}", f"{d1['Amplitude'][5]}", f"{d1['Amplitude_g'][5]}", f"{d1['Phase_Angle'][5]}"],
            [f"{d1['Frequency'][6]}", f"{d1['Amplitude'][6]}", f"{d1['Amplitude_g'][6]}", f"{d1['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B12:E19", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d2['Frequency'][0]}", f"{d2['Amplitude'][0]}", f"{d2['Amplitude_g'][0]}", f"{d2['Phase_Angle'][0]}"],
            [f"{d2['Frequency'][1]}", f"{d2['Amplitude'][1]}", f"{d2['Amplitude_g'][1]}", f"{d2['Phase_Angle'][1]}"],
            [f"{d2['Frequency'][2]}", f"{d2['Amplitude'][2]}", f"{d2['Amplitude_g'][2]}", f"{d2['Phase_Angle'][2]}"],
            [f"{d2['Frequency'][3]}", f"{d2['Amplitude'][3]}", f"{d2['Amplitude_g'][3]}", f"{d2['Phase_Angle'][3]}"],
            [f"{d2['Frequency'][4]}", f"{d2['Amplitude'][4]}", f"{d2['Amplitude_g'][4]}", f"{d2['Phase_Angle'][4]}"],
            [f"{d2['Frequency'][5]}", f"{d2['Amplitude'][5]}", f"{d2['Amplitude_g'][5]}", f"{d2['Phase_Angle'][5]}"],
            [f"{d2['Frequency'][6]}", f"{d2['Amplitude'][6]}", f"{d2['Amplitude_g'][6]}", f"{d2['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B23:E30", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d3['Frequency'][0]}", f"{d3['Amplitude'][0]}", f"{d3['Amplitude_g'][0]}", f"{d3['Phase_Angle'][0]}"],
            [f"{d3['Frequency'][1]}", f"{d3['Amplitude'][1]}", f"{d3['Amplitude_g'][1]}", f"{d3['Phase_Angle'][1]}"],
            [f"{d3['Frequency'][2]}", f"{d3['Amplitude'][2]}", f"{d3['Amplitude_g'][2]}", f"{d3['Phase_Angle'][2]}"],
            [f"{d3['Frequency'][3]}", f"{d3['Amplitude'][3]}", f"{d3['Amplitude_g'][3]}", f"{d3['Phase_Angle'][3]}"],
            [f"{d3['Frequency'][4]}", f"{d3['Amplitude'][4]}", f"{d3['Amplitude_g'][4]}", f"{d3['Phase_Angle'][4]}"],
            [f"{d3['Frequency'][5]}", f"{d3['Amplitude'][5]}", f"{d3['Amplitude_g'][5]}", f"{d3['Phase_Angle'][5]}"],
            [f"{d3['Frequency'][6]}", f"{d3['Amplitude'][6]}", f"{d3['Amplitude_g'][6]}", f"{d3['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B34:E41", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d4['Frequency'][0]}", f"{d4['Amplitude'][0]}", f"{d4['Amplitude_g'][0]}", f"{d4['Phase_Angle'][0]}"],
            [f"{d4['Frequency'][1]}", f"{d4['Amplitude'][1]}", f"{d4['Amplitude_g'][1]}", f"{d4['Phase_Angle'][1]}"],
            [f"{d4['Frequency'][2]}", f"{d4['Amplitude'][2]}", f"{d4['Amplitude_g'][2]}", f"{d4['Phase_Angle'][2]}"],
            [f"{d4['Frequency'][3]}", f"{d4['Amplitude'][3]}", f"{d4['Amplitude_g'][3]}", f"{d4['Phase_Angle'][3]}"],
            [f"{d4['Frequency'][4]}", f"{d4['Amplitude'][4]}", f"{d4['Amplitude_g'][4]}", f"{d4['Phase_Angle'][4]}"],
            [f"{d4['Frequency'][5]}", f"{d4['Amplitude'][5]}", f"{d4['Amplitude_g'][5]}", f"{d4['Phase_Angle'][5]}"],
            [f"{d4['Frequency'][6]}", f"{d4['Amplitude'][6]}", f"{d4['Amplitude_g'][6]}", f"{d4['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B45:E52", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d5['Frequency'][0]}", f"{d5['Amplitude'][0]}", f"{d5['Amplitude_g'][0]}", f"{d5['Phase_Angle'][0]}"],
            [f"{d5['Frequency'][1]}", f"{d5['Amplitude'][1]}", f"{d5['Amplitude_g'][1]}", f"{d5['Phase_Angle'][1]}"],
            [f"{d5['Frequency'][2]}", f"{d5['Amplitude'][2]}", f"{d5['Amplitude_g'][2]}", f"{d5['Phase_Angle'][2]}"],
            [f"{d5['Frequency'][3]}", f"{d5['Amplitude'][3]}", f"{d5['Amplitude_g'][3]}", f"{d5['Phase_Angle'][3]}"],
            [f"{d5['Frequency'][4]}", f"{d5['Amplitude'][4]}", f"{d5['Amplitude_g'][4]}", f"{d5['Phase_Angle'][4]}"],
            [f"{d5['Frequency'][5]}", f"{d5['Amplitude'][5]}", f"{d5['Amplitude_g'][5]}", f"{d5['Phase_Angle'][5]}"],
            [f"{d5['Frequency'][6]}", f"{d5['Amplitude'][6]}", f"{d5['Amplitude_g'][6]}", f"{d5['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B56:E63", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d6['Frequency'][0]}", f"{d6['Amplitude'][0]}", f"{d6['Amplitude_g'][0]}", f"{d6['Phase_Angle'][0]}"],
            [f"{d6['Frequency'][1]}", f"{d6['Amplitude'][1]}", f"{d6['Amplitude_g'][1]}", f"{d6['Phase_Angle'][1]}"],
            [f"{d6['Frequency'][2]}", f"{d6['Amplitude'][2]}", f"{d6['Amplitude_g'][2]}", f"{d6['Phase_Angle'][2]}"],
            [f"{d6['Frequency'][3]}", f"{d6['Amplitude'][3]}", f"{d6['Amplitude_g'][3]}", f"{d6['Phase_Angle'][3]}"],
            [f"{d6['Frequency'][4]}", f"{d6['Amplitude'][4]}", f"{d6['Amplitude_g'][4]}", f"{d6['Phase_Angle'][4]}"],
            [f"{d6['Frequency'][5]}", f"{d6['Amplitude'][5]}", f"{d6['Amplitude_g'][5]}", f"{d6['Phase_Angle'][5]}"],
            [f"{d6['Frequency'][6]}", f"{d6['Amplitude'][6]}", f"{d6['Amplitude_g'][6]}", f"{d6['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B67:E74", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d7['Frequency'][0]}", f"{d7['Amplitude'][0]}", f"{d7['Amplitude_g'][0]}", f"{d7['Phase_Angle'][0]}"],
            [f"{d7['Frequency'][1]}", f"{d7['Amplitude'][1]}", f"{d7['Amplitude_g'][1]}", f"{d7['Phase_Angle'][1]}"],
            [f"{d7['Frequency'][2]}", f"{d7['Amplitude'][2]}", f"{d7['Amplitude_g'][2]}", f"{d7['Phase_Angle'][2]}"],
            [f"{d7['Frequency'][3]}", f"{d7['Amplitude'][3]}", f"{d7['Amplitude_g'][3]}", f"{d7['Phase_Angle'][3]}"],
            [f"{d7['Frequency'][4]}", f"{d7['Amplitude'][4]}", f"{d7['Amplitude_g'][4]}", f"{d7['Phase_Angle'][4]}"],
            [f"{d7['Frequency'][5]}", f"{d7['Amplitude'][5]}", f"{d7['Amplitude_g'][5]}", f"{d7['Phase_Angle'][5]}"],
            [f"{d7['Frequency'][6]}", f"{d7['Amplitude'][6]}", f"{d7['Amplitude_g'][6]}", f"{d7['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B78:E85", 
            [["Frequency", "Amplitude", "Amplitude_g", "Phase_Angle"],
            [f"{d8['Frequency'][0]}", f"{d8['Amplitude'][0]}", f"{d8['Amplitude_g'][0]}", f"{d8['Phase_Angle'][0]}"],
            [f"{d8['Frequency'][1]}", f"{d8['Amplitude'][1]}", f"{d8['Amplitude_g'][1]}", f"{d8['Phase_Angle'][1]}"],
            [f"{d8['Frequency'][2]}", f"{d8['Amplitude'][2]}", f"{d8['Amplitude_g'][2]}", f"{d8['Phase_Angle'][2]}"],
            [f"{d8['Frequency'][3]}", f"{d8['Amplitude'][3]}", f"{d8['Amplitude_g'][3]}", f"{d8['Phase_Angle'][3]}"],
            [f"{d8['Frequency'][4]}", f"{d8['Amplitude'][4]}", f"{d8['Amplitude_g'][4]}", f"{d8['Phase_Angle'][4]}"],
            [f"{d8['Frequency'][5]}", f"{d8['Amplitude'][5]}", f"{d8['Amplitude_g'][5]}", f"{d8['Phase_Angle'][5]}"],
            [f"{d8['Frequency'][6]}", f"{d8['Amplitude'][6]}", f"{d8['Amplitude_g'][6]}", f"{d8['Phase_Angle'][6]}"]])









def write_dfs_to_google_sheets__velocity_deformation(df_namedtuple: NamedTuple) -> None:
    """
    Writes the velocity and deformation data to Google Sheets.
    """
    from stuff import GoogleSheets
    sheet = GoogleSheets("PythonTest")
    sheet.clear_worksheet()
    d1, d2, d3, d4, d5, d6, d7, d8 = df_namedtuple
    sheet.set_acell_contents_range("B1:D8", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d1['Frequency'][0]}", f"{d1['Amplitude'][0]}", f"{d1['Phase_Angle'][0]}"],
            [f"{d1['Frequency'][1]}", f"{d1['Amplitude'][1]}", f"{d1['Phase_Angle'][1]}"],
            [f"{d1['Frequency'][2]}", f"{d1['Amplitude'][2]}", f"{d1['Phase_Angle'][2]}"],
            [f"{d1['Frequency'][3]}", f"{d1['Amplitude'][3]}", f"{d1['Phase_Angle'][3]}"],
            [f"{d1['Frequency'][4]}", f"{d1['Amplitude'][4]}", f"{d1['Phase_Angle'][4]}"],
            [f"{d1['Frequency'][5]}", f"{d1['Amplitude'][5]}", f"{d1['Phase_Angle'][5]}"],
            [f"{d1['Frequency'][6]}", f"{d1['Amplitude'][6]}", f"{d1['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B12:D19", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d2['Frequency'][0]}", f"{d2['Amplitude'][0]}", f"{d2['Phase_Angle'][0]}"],
            [f"{d2['Frequency'][1]}", f"{d2['Amplitude'][1]}", f"{d2['Phase_Angle'][1]}"],
            [f"{d2['Frequency'][2]}", f"{d2['Amplitude'][2]}", f"{d2['Phase_Angle'][2]}"],
            [f"{d2['Frequency'][3]}", f"{d2['Amplitude'][3]}", f"{d2['Phase_Angle'][3]}"],
            [f"{d2['Frequency'][4]}", f"{d2['Amplitude'][4]}", f"{d2['Phase_Angle'][4]}"],
            [f"{d2['Frequency'][5]}", f"{d2['Amplitude'][5]}", f"{d2['Phase_Angle'][5]}"],
            [f"{d2['Frequency'][6]}", f"{d2['Amplitude'][6]}", f"{d2['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B23:D30", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d3['Frequency'][0]}", f"{d3['Amplitude'][0]}", f"{d3['Phase_Angle'][0]}"],
            [f"{d3['Frequency'][1]}", f"{d3['Amplitude'][1]}", f"{d3['Phase_Angle'][1]}"],
            [f"{d3['Frequency'][2]}", f"{d3['Amplitude'][2]}", f"{d3['Phase_Angle'][2]}"],
            [f"{d3['Frequency'][3]}", f"{d3['Amplitude'][3]}", f"{d3['Phase_Angle'][3]}"],
            [f"{d3['Frequency'][4]}", f"{d3['Amplitude'][4]}", f"{d3['Phase_Angle'][4]}"],
            [f"{d3['Frequency'][5]}", f"{d3['Amplitude'][5]}", f"{d3['Phase_Angle'][5]}"],
            [f"{d3['Frequency'][6]}", f"{d3['Amplitude'][6]}", f"{d3['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B34:D41", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d4['Frequency'][0]}", f"{d4['Amplitude'][0]}", f"{d4['Phase_Angle'][0]}"],
            [f"{d4['Frequency'][1]}", f"{d4['Amplitude'][1]}", f"{d4['Phase_Angle'][1]}"],
            [f"{d4['Frequency'][2]}", f"{d4['Amplitude'][2]}", f"{d4['Phase_Angle'][2]}"],
            [f"{d4['Frequency'][3]}", f"{d4['Amplitude'][3]}", f"{d4['Phase_Angle'][3]}"],
            [f"{d4['Frequency'][4]}", f"{d4['Amplitude'][4]}", f"{d4['Phase_Angle'][4]}"],
            [f"{d4['Frequency'][5]}", f"{d4['Amplitude'][5]}", f"{d4['Phase_Angle'][5]}"],
            [f"{d4['Frequency'][6]}", f"{d4['Amplitude'][6]}", f"{d4['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B45:D52", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d5['Frequency'][0]}", f"{d5['Amplitude'][0]}", f"{d5['Phase_Angle'][0]}"],
            [f"{d5['Frequency'][1]}", f"{d5['Amplitude'][1]}", f"{d5['Phase_Angle'][1]}"],
            [f"{d5['Frequency'][2]}", f"{d5['Amplitude'][2]}", f"{d5['Phase_Angle'][2]}"],
            [f"{d5['Frequency'][3]}", f"{d5['Amplitude'][3]}", f"{d5['Phase_Angle'][3]}"],
            [f"{d5['Frequency'][4]}", f"{d5['Amplitude'][4]}", f"{d5['Phase_Angle'][4]}"],
            [f"{d5['Frequency'][5]}", f"{d5['Amplitude'][5]}", f"{d5['Phase_Angle'][5]}"],
            [f"{d5['Frequency'][6]}", f"{d5['Amplitude'][6]}", f"{d5['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B56:D63", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d6['Frequency'][0]}", f"{d6['Amplitude'][0]}", f"{d6['Phase_Angle'][0]}"],
            [f"{d6['Frequency'][1]}", f"{d6['Amplitude'][1]}", f"{d6['Phase_Angle'][1]}"],
            [f"{d6['Frequency'][2]}", f"{d6['Amplitude'][2]}", f"{d6['Phase_Angle'][2]}"],
            [f"{d6['Frequency'][3]}", f"{d6['Amplitude'][3]}", f"{d6['Phase_Angle'][3]}"],
            [f"{d6['Frequency'][4]}", f"{d6['Amplitude'][4]}", f"{d6['Phase_Angle'][4]}"],
            [f"{d6['Frequency'][5]}", f"{d6['Amplitude'][5]}", f"{d6['Phase_Angle'][5]}"],
            [f"{d6['Frequency'][6]}", f"{d6['Amplitude'][6]}", f"{d6['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B67:D74", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d7['Frequency'][0]}", f"{d7['Amplitude'][0]}", f"{d7['Phase_Angle'][0]}"],
            [f"{d7['Frequency'][1]}", f"{d7['Amplitude'][1]}", f"{d7['Phase_Angle'][1]}"],
            [f"{d7['Frequency'][2]}", f"{d7['Amplitude'][2]}", f"{d7['Phase_Angle'][2]}"],
            [f"{d7['Frequency'][3]}", f"{d7['Amplitude'][3]}", f"{d7['Phase_Angle'][3]}"],
            [f"{d7['Frequency'][4]}", f"{d7['Amplitude'][4]}", f"{d7['Phase_Angle'][4]}"],
            [f"{d7['Frequency'][5]}", f"{d7['Amplitude'][5]}", f"{d7['Phase_Angle'][5]}"],
            [f"{d7['Frequency'][6]}", f"{d7['Amplitude'][6]}", f"{d7['Phase_Angle'][6]}"]])
    sheet.set_acell_contents_range("B78:D85", 
            [["Frequency", "Amplitude", "Phase_Angle"],
            [f"{d8['Frequency'][0]}", f"{d8['Amplitude'][0]}", f"{d8['Phase_Angle'][0]}"],
            [f"{d8['Frequency'][1]}", f"{d8['Amplitude'][1]}", f"{d8['Phase_Angle'][1]}"],
            [f"{d8['Frequency'][2]}", f"{d8['Amplitude'][2]}", f"{d8['Phase_Angle'][2]}"],
            [f"{d8['Frequency'][3]}", f"{d8['Amplitude'][3]}", f"{d8['Phase_Angle'][3]}"],
            [f"{d8['Frequency'][4]}", f"{d8['Amplitude'][4]}", f"{d8['Phase_Angle'][4]}"],
            [f"{d8['Frequency'][5]}", f"{d8['Amplitude'][5]}", f"{d8['Phase_Angle'][5]}"],
            [f"{d8['Frequency'][6]}", f"{d8['Amplitude'][6]}", f"{d8['Phase_Angle'][6]}"]])





def write_acceleration_descriptions_to_google_sheets(axis: str, sim_folder_name: str) -> None:
    """
    Writes the X, Y, and Z acceleration data descriptions to Google Sheets.

    ## Parameters
    `axis` : str
        The axis of the acceleration data. Either "X", "Y", or "Z".
    `sim_folder_name` : str
        The name of the simulation folder (e.g. "sim1", "sim2", etc.).
    """
    data_files = load_dfs_from_description__acceleration(f"{sim_folder_name.lower()}/data/acceleration_{axis.lower()}_description.txt")
    write_dfs_to_google_sheets__acceleration(data_files)



def write_deformation_descriptions_to_google_sheets(axis: str, sim_folder_name: str) -> None:
    """
    Writes the X, Y, and Z deformation data descriptions to Google Sheets.

    ## Parameters
    `axis` : str
        The axis of the deformation data. Either "X", "Y", or "Z".
    `sim_folder_name` : str
        The name of the simulation folder (e.g. "sim1", "sim2", etc.).
    """
    data_files = load_dfs_from_description__velocity_deformation(f"{sim_folder_name.lower()}/data/deformation_{axis.lower()}_description.txt")
    write_dfs_to_google_sheets__velocity_deformation(data_files)



def write_velocity_descriptions_to_google_sheets(axis: str, sim_folder_name: str) -> None:
    """
    Writes the X, Y, and Z velocity data descriptions to Google Sheets.

    ## Parameters
    `axis` : str
        The axis of the velocity data. Either "X", "Y", or "Z".
    `sim_folder_name` : str
        The name of the simulation folder (e.g. "sim1", "sim2", etc.).
    """
    data_files = load_dfs_from_description__velocity_deformation(f"{sim_folder_name.lower()}/data/velocity_{axis.lower()}_description.txt")
    write_dfs_to_google_sheets__velocity_deformation(data_files)














def bookmark_pdf(pdf_filepath: str, bookmark_structure: dict, view_structure: bool = False) -> None:
    """
    Bookmarks a PDF file and saves it to the same directory as the original PDF file.

    ## Parameters
    `pdf_filepath` : str
        The filepath of the PDF file to bookmark.
    `bookmark_structure` : dict
        The bookmark structure to use. The keys are the bookmark names and the values are the page numbers or nested dictionaries.
    `view_structure` : bool
        Whether or not to view the bookmark structure before bookmarking the PDF file.
    """
    from stuff import File
    if '.pdf' not in pdf_filepath:
        pdf_filepath += '.pdf'
    pdf = File(pdf_filepath)
    if view_structure:
        from stuff import view
        view(bookmark_structure)
    pdf.bookmark_pdf(bookmark_structure, output_file_name=f"{pdf_filepath[:-4]}_bookmarked.pdf")






def get_modal_frequencies(sim_folder_name: str) -> list[float]:
    """
    Get the modal frequencies from the simulation folder, saved in `modes.txt`.

    ## Parameters
    `sim_folder_name` : str
        The name of the simulation folder (e.g. "sim1", "sim2", etc.).
    """
    with open(f"{sim_folder_name}/modes.txt") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines]
    col_names = lines[0].split('\t')
    rows = [line.split('\t') for line in lines[1:]]
    df = pd.DataFrame(rows, columns=col_names)
    modes = [float(mode) for mode in df['Frequency'].tolist()]
    return modes







if __name__ == "__main__":
    SIM_FOLDER_NAME = "sim5"

    # data_files = load_dfs_from_description__acceleration("sim5/data/acceleration_z_description.txt")
    # write_dfs_to_google_sheets__acceleration(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/velocity_x_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/velocity_y_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/velocity_z_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/deformation_x_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/deformation_y_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
    # data_files = load_dfs_from_description__velocity_deformation("sim5/data/deformation_z_description.txt")
    # write_dfs_to_google_sheets__velocity_deformation(data_files)
