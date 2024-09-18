"""
We use os module to:
* rename
* delete
* create
files
"""

import os

# RENAME
# os.rename('file_to_delete.txt', 'file_to_rename.txt')

# FileNotFoundError  -> if the file not exists

# exception handling
# try:
#     os.rename('file_to_delete.txt', 'file_to_rename.txt')
# except:
#     print('File not found with this name.')


# DELETE -> remove(), unlink()

# os.remove('file_to_rename.txt')

# os.unlink('unlink.txt')


# CREATE -> mode='x'

# with open('file_not_exist.txt', mode='x') as new_file:
#     new_file.write('This is a new file with mode x....')

# FileExistsError -> if you try to create an existing file

try:
    with open('file_not_exist.txt', mode='x') as new_file:
        new_file.write('This is a new file with mode x....')
except:
    print('File already exist....')