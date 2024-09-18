import os
import pathlib
import shutil

# 1- DELETE FOLDERS
"""
1- os.rmdir()           -> if empty
2- pathlib.Path.rmdir() -> if empty
3- shutil.rmtree()      -> removes all
"""

# create two folder to delete
# os.mkdir('folder_to_delete_1')
# os.mkdir('folder_to_delete_2')

# os
# os.rmdir('folder_to_delete_1')
# OSError: [WinError 145] The directory is not empty: 'folder_to_delete_2'
# pathlib.Path('folder_to_delete_2').rmdir()

# shutil
# shutil.rmtree('folder_to_delete_2')


# 2- COPY FILES and FOLDER
# FILES
# shutil.copy()
# shutil.copy2()
# Source -> Destination

src = 'source/source_file.txt'
dest = 'dest/final_file.txt'

# shutil.copy2(src, dest)

# FOLDERS
# shutil.copytree()
# shutil.copytree('source', 'source_copy_with_shutil')

# 3- MOVE FILES and FOLDERS
# shutil.move(src, dest)

shutil.move('source', 'example_dir_1')



