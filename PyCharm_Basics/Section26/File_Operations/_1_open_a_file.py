"""
File is a set of bytes that store data.
"""

"""
File Types:
1- Binary Types
    * pdf, doc, jpg, png

2- Text Types
    * txt, xml, html, .py, .java
"""

"""
Encoding defines how data is stored in a file.

Common encodings:
1- ASCII (128 characters)
2- UNICODE (1.114.112 characters)
"""

# Open a file in Python -> open()

# without encoding
# file = open('words.txt')
# print(file.read())

# without encoding -> € => â‚¬
# with encoding
# file = open('words.txt', encoding='utf-8')
# print(file.read())

# Important
# You should always close the file you open.
# file.close()


# What happens if the file doesn't exist -> Raises error
# FileNotFoundError: [Errno 2] No such file or directory: 'wordssss.txt'
# file = open('wordssss.txt', encoding='utf-8')


# exception handling
# try:
#     file = open('words.txt', encoding='utf-8')
# except:
#     print('No such file in the path....')
# else:
#     print(file.read())
#     file.close()


"""
with

Context Manager
It handles file open and close operations automatically.

"""

# with keyword -> opened and closed
# with open('words.txt', encoding='utf-8') as file:
#     content_up_to = file.read()
#     print(content_up_to)


# If the file doesn't exist -> FileNotFoundError
# try:
#     with open('wordsss.txt', encoding='utf-8') as file:
#         content_up_to = file.read()
#         print(content_up_to)
# except FileNotFoundError:
#     print('No such file in the path....')


"""
File Opening Modes:
* r: read
* w: write
* a: append
* x: create
* t: text file
* b: binary file
* +: update (read + write)
"""

# Ex
# r -> read
# mode='r'
# mode='rt'  read as text
# with open('words.txt', encoding='utf-8', mode='rt') as file:
#     content_up_to = file.read()
#     print(content_up_to)


# read a binay file
# mode='rb'
with open('python_logo.png', mode='rb') as file:
    content = file.read()
    print(content)













