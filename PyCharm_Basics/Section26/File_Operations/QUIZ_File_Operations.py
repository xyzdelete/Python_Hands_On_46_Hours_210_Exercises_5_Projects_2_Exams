"""
 [10 Questions] QUIZ - File Operations
"""

# --------------------------------------------------------------------------------------#

# Q 1:
"""
Open the 'quiz_files/flower_names.txt' file in this project with Python.
And print the flower names.

Hints:
* os
* read mode ('r')
"""

# S 1:

import os

# with open("quiz_files/flower_names.txt", mode="r", encoding="utf-8") as file:
#     print(file.read())


# --------------------------------------------------------------------------------------#

# Q 2:
"""
Open the 'quiz_files/flower_names.txt' file in this project with Python.
And append the name below to this file:

'Z: Zinnia elegans'

Finally print all the file content.

Hints:
* os
* append mode ('a')
"""

# S 2:

# with open(f"{os.getcwd()}/quiz_files/flower_names.txt", mode="a", encoding="utf-8") as file:
#     file.write("\nZ: Zinnia Elegans")
#
# with open(f"{os.getcwd()}/quiz_files/flower_names.txt", mode="r", encoding="utf-8") as file:
#     print(file.read())

# --------------------------------------------------------------------------------------#

# Q 3:
"""
Create a file named 'quiz_files/file_to_delete.txt'.
And add the content below into this file:
'This file will be deleted in the Quiz.'

Hints:
* os
* to create file -> mode='x'
* encoding
"""

# S 3:

# with open("quiz_files/file_to_delete.txt", mode="x") as file:
#     file.write("This file will be deleted in the Quiz.")

# --------------------------------------------------------------------------------------#

# Q 4:
"""
Delete the file 'quiz_files/file_to_delete.txt' you created in Q3.
Add exception handling to handle the case of not finding such a file.

Hints:
* os
* try-except
* to delete -> os.remove()
"""

# S 4:

# try:
#     os.remove(r"quiz_files/file_to_delete.txt")
# except Exception as ex:
#     print(ex)

# --------------------------------------------------------------------------------------#

# Q 5:
"""
Get the list of all content (files and folders) in this project directory.
Use this methods:
1- os.listdir()
2- os.scandir()
3- pathlib.Path.iterdir()

Hints:
* os
* pathlib
"""

# S 5:

import pathlib

# for item in os.listdir(os.getcwd()):
#     print(item)

# for item in os.scandir(os.getcwd()):
#     print(item)

# for item in pathlib.Path(os.getcwd()).iterdir():
#     print(item)
# --------------------------------------------------------------------------------------#

# Q 6:
"""
Create the folder tree below in the 'quiz_files' directory:

- quiz_files
    - folder 1
        - sub folder 1
        - sub folder 2
    - folder 2
    - folder 3
        - sub folder 3

Create all of them one by one with os.mkdir().

Hints:
* os
* os.mkdir()
"""

# S 6:

# os.mkdir("quiz_files/folder_1")
# os.mkdir("quiz_files/folder_1/sub_folder_1")
# os.mkdir("quiz_files/folder_1/sub_folder_2")
# os.mkdir("quiz_files/folder_2")
# os.mkdir("quiz_files/folder_3")
# os.mkdir("quiz_files/folder_3/sub_folder_3")
# --------------------------------------------------------------------------------------#

# Q 7:
"""
Create the folder tree below in the 'quiz_files' directory.
This time create with the methods described in parenthesis.

- quiz_files

    (os.makedirs)
    - folder 10
        - sub folder 10
        - sub folder 20
    
    (pathlib.Path.mkdir)
    - folder 20
    
    (pathlib.Path.mkdir)
    - folder 30
        - sub folder 30
        
Handle 'FileExistsError' exception if the file already exists.

Hints:
* os
* os.makedirs()
* pathlib.Path.mkdir()
* exist_ok=True
* parents
"""

# Çözüm 7:

# os.makedirs("quiz_files/folder_10/sub_folder_10", exist_ok=True)
# os.makedirs("quiz_files/folder_10/sub_folder_20", exist_ok=True)
# pathlib.Path("quiz_files/folder_20").mkdir(parents=True, exist_ok=True)
# pathlib.Path("quiz_files/folder_30/sub_folder_30").mkdir(parents=True, exist_ok=True)
# --------------------------------------------------------------------------------------#

# Q 8:
"""
Find all the files which has '*a*d*.py' in the file name.
Use Comprehension both getting the list and printing it.

Hints:
* os
* os.scandir()
* os.getcwd()
* fnmatch
"""

# S 8:

import fnmatch

pattern = "*a*d*.py"

# for eachItem in os.scandir(os.getcwd()):
#     if eachItem.is_file() and fnmatch.fnmatch(eachItem.name, pattern):
#         print(eachItem.name)

# [
#     print(eachItem.name)
#     for eachItem in os.scandir(os.getcwd())
#     if eachItem.is_file() and fnmatch.fnmatch(eachItem.name, pattern)
# ]
# --------------------------------------------------------------------------------------#

# Q 9:
"""
Delete all the files and folders which has '1' in its name.

Use os.path.join to join the current project path (os.getcwd) and 'quiz_files'.
And make it as your search path.

Use single Comprehension to find and delete them.

Hints:
* shutil.rmtree()
* os.getcwd()
* os.path.join()
"""

# S 9:

import shutil

searchPath = os.path.join(os.getcwd(), "quiz_files")

# [
#     shutil.rmtree(eachItem)
#     for eachItem in os.scandir(searchPath)
#     if eachItem.name.count("1") >= 1
# ]



# --------------------------------------------------------------------------------------#

# Q 10:
"""
Create an archive (zip) folder out of 'quiz_files' folder.
The name of the archive folder is going to be 'quiz_folder_archive.zip'.

Hints:
* shutil.make_archive()
"""

# S 10:

import zipfile

shutil.make_archive("quiz_files", "zip", "quiz_files")

# --------------------------------------------------------------------------------------#