"""
 [10 Questions] QUIZ - Modules and Packages
"""
# --------------------------------------------------------------------------------------#

# Q 1:
"""
Define a function named 'random_printer'.
It will import random module and will print a random number between 100 and 200.

Hints:
* randint()
"""

# S 1:

import random

def random_printer():
    print(random.randint(100, 200))


# --------------------------------------------------------------------------------------#

# Q 2:
"""
Define a function named 'random_list'.
It will import random module with custom name 'rnd'.
And it will create a list of size 10.
The items in the list are random values between 100 and 200.
The function will print the list all at once.

Then it will randomly select 4 of the items in this list and print them.

Hints:
* randint()
* sample()
"""

# S 2:

def random_list():
    import random as rnd
    a_list = [rnd.randint(100, 200) for i in range(10)]
    print(a_list)
    a_new_list = rnd.sample(a_list, 4)
    print(a_new_list)

# random_list()
# --------------------------------------------------------------------------------------#

# Q 3:
"""
Print the current project path via os module.

Hints:
* getcwd()
"""

# S 3:

import os

print(os.getcwd())


# --------------------------------------------------------------------------------------#

# Q 4:
"""
Print your computers:
* Operating System
* Processor
using standard Python modules.

Hints:
* platform
"""

# S 4:

import platform

print(platform.system())
print(platform.processor())



# --------------------------------------------------------------------------------------#

# Q 5:
"""
Print the Python Search Path via sys module.
Python Search Path is the list of paths which Python uses when looking for modules.
Print the items one by one via a for loop.

Hints:
* path
"""

# S 5:

import sys

print(sys.path)


# --------------------------------------------------------------------------------------#

# Q 6:
"""
Create a module named 'consonants' in the current project.
Define a function named 'get_consonants' in this module.
This function take a text as parameter and it will return a set of consonants in this text.
Call this function with a text and print the consonants in this text.

Hints:
* your module should implement it's own exception handling

Expected Output:
'Pyton Programming Language.... /@*-'

{'r', 'P', 'L', 'y', 'm', 'n', 't', 'g'}
"""

# S 6:

import consonants

# print(consonants.get_consonants("AbraKadabra"))


# --------------------------------------------------------------------------------------#

# Q 7:
"""
Define a module named 'vowel' and make it available for all files in this project.
In this module define a function named 'get_vowels'.
This function take a text as parameter and it will return a set of vowels in this text.
Call this function with a text and print the vowels in this text.

Hints:
* your module should implement it's own exception handling
* inspect sys.path

Expected Output:
'Pyton Programming Language.... /@*-'

{'a', 'e', 'i', 'o', 'u'}
"""

# S 7:

import vowel

# print(vowel.get_vowels("AbraKadabra"))


# --------------------------------------------------------------------------------------#

# Q 8:
"""
Create a Python Package named 'quiz_packages' in the current project folder.
Copy the modules you created in Q6 (consonants) and Q7 (vowel) in this package.
Import these modules from quiz_packages package and use their functions (get_consonants, get_vowels)

Hints:
* Python Package (__init__.py)
* global variables in the __init__.py file.

Expected Output:
text = 'Pyton Programming Language.... /@*-'

get_consonants(text) -> {'n', 'm', 'P', 'L', 'r', 'g', 'y', 't'}
get_vowels(text) -> {'i', 'o', 'u', 'a', 'e'}
"""

# S 8:

from quiz_packages import consonants
from quiz_packages import vowel
text = 'Pyton Programming Language.... /@*-'
print(consonants.get_consonants(text))
print(vowel.get_vowels(text))

# --------------------------------------------------------------------------------------#

# Q 9:
"""
Copy the 'quiz_packages' Python Package you created in Q8.
Now make it available for all Python projects on your machine.
In other words, make it a global package.
And rename it as 'quiz_packages_global'.

Hints:
* create a global Python Package
* sys.path
* to see where Python is installed on your machine:
    * command prompt (cmd) -> where python

Expected Output:
text = 'Pyton Programming Language.... /@*-'

get_consonants(text) -> {'r', 'P', 'y', 'm', 'n', 'L', 't', 'g'}
get_vowels(text) -> {'i', 'a', 'o', 'e', 'u'}
"""

# S 9:

# Nononoon no global installations



# --------------------------------------------------------------------------------------#

# Soru 10:
"""
Which one below is NOT True for Python Modules?

A- In Python, a module is a file with .py extension.
B- We use 'import' keyword to access the modules.
C- In Python, a Package is a container containing modules
D- Python packages are ordinary folders. It is enough to create a folder to define a Python package.
"""

# S 10:

# A - True
# B - True
# C - True
# D - False (__init__.py)


# --------------------------------------------------------------------------------------#
