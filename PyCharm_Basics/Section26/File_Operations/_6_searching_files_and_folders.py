"""
Two ways to search:

1- String Methods -> startswith, endswith, find

2- fnmatch module (recommended)
"""

import os
from pathlib import Path
import fnmatch

# Ex
# String Methods

# seach path
# if your string contains \ char -> r in front of string => raw string
search_path = r'C:\Windows'
# print(search_path)

# for k in os.listdir(search_path):
#     print(k)

# let's get .exe files

# with -> context manager
# path = Path(search_path)
# path.iterdir()

# long way
# with Path(search_path) as path:
#     # get content
#     for content in path.iterdir():
#         # check type -> file
#         if content.is_file() and content.name.endswith('.exe'):
#             print(content.name)


# fnmatch module
# recommended

pattern = '*.exe'

with Path(search_path) as folder:
    for f in folder.iterdir():
        if f.is_file() and fnmatch.fnmatch(f.name, pattern):
            print(f.name)




