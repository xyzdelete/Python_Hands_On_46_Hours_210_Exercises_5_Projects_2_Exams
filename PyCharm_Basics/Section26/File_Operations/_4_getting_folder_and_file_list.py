"""
Content Types inside a folder:
1- File
2- Folder (Directory)
"""

# --------------- Get All Content  ---------------#

# Way 1 -> os.listdir()
import os

# the project
path = os.getcwd()

# content = os.listdir(path)
# print(content)
# for c in content:
#     print(c)

# Way 2 -> os.scandir()
# folder = os.scandir(path)
# for f in folder:
#     print(f)

# Way 3 -> pathlib.Path.iterdir()
# from pathlib import Path
#
# path_content = Path(path)
#
# for inner_content in path_content.iterdir():
#     print(inner_content)


# --------------- Get All Files  ---------------#

# Way 1 -> os.listdir()
# os.path.isfile()

content = os.listdir(path)
# print(content)
# for c in content:
#     if os.path.isfile(c):
#         print(c)


# Way 2 -> os.scandir()
# folder = os.scandir(path)
# for f in folder:
#     if f.is_file():
#         print(f)


# Way 3 -> pathlib.Path.iterdir()
# from pathlib import Path
#
# path_content = Path(path)
#
# for inner_content in path_content.iterdir():
#     if inner_content.is_file():
#         print(inner_content)


# --------------- Get All Folders (Directories)  ---------------#

# Way 1 -> os.listdir()
# os.path.isfile()

# content = os.listdir(path)
# print(content)
# for c in content:
#     if os.path.isdir(c):
#         print(c)


# Way 2 -> os.scandir()
# folder = os.scandir(path)
# for f in folder:
#     if f.is_dir():
#         print(f)


# Way 3 -> pathlib.Path.iterdir()
from pathlib import Path

path_content = Path(path)

for inner_content in path_content.iterdir():
    if inner_content.is_dir():
        print(inner_content)