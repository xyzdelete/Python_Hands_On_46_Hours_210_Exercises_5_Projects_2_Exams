"""
ARCHIVE FILE Opeations
zipfile
"""

import os
import shutil
import zipfile

# for d in os.listdir():
#     print(d)

# let's open zip file
archive = zipfile.ZipFile('neural_style_transfer.zip', 'r')
print(archive)

# let's see what's in it
for d in archive.filelist:
    print(d)

# extract it
archive.extractall()

archive.close()

# CREATE ZIP FILES
# shutil.make_archive()

shutil.make_archive('new_archive_folder', 'zip', 'neural_style_transfer')