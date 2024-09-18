"""
To create directory / directories:

1- os.mkdir()
    * mkdir()    -> creates single directory
    * makedirs() -> multiple directories

2- pathlib.Path.mkdir() -> single and multiple directories

"""

# SINGLE DIRECTORY
import os
from pathlib import Path

# get the main directory path
main_path = os.getcwd()

# print(main_path)

# Ex
# Way 1 -> os.mkdir()

# FileExistsError -> if you create again
# os.mkdir('example_dir_1')
# os.mkdir('example_dir_2')


# Way 2 -> Path

# p = Path('path_folder_1')
# p.mkdir()

# FileExistsError
# try:
#     p = Path('path_folder_1')
#     p.mkdir()
# except FileExistsError as file_error:
#     # print('This folder exists.')
#     print(file_error)


# MULTIPLE DIRECTORIES
"""
    - level 1
        - level 2
            - level 3
"""

# Way 1 -> os.makedirs()

# folder tree
# os.makedirs('level 1/level 2/level 3')

# FileExistsError -> to overcome -> exist_ok
os.makedirs('level 1/level 2/level 3', exist_ok=True)


# Way 2 -> pathlib.Path.mkdir()
p2 = Path('path_level_1/path_level_2/path_level_3/path_level_4')
# parents=True -> create all the parents
# p2.mkdir(parents=True)

# create again
p2.mkdir(parents=True, exist_ok=True)



