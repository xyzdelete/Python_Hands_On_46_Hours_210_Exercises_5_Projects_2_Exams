"""

try:
    ......
    ......
    ......

except Ex1:
    ......
    ......

except Ex2:
    .......

else:
    .......
    no-errors


Python Interpreter runs the code in try block.
If there is an error, the execution goes into the related except block.
If there is no error, then it will move on to else block.

"""

# Ex:

def open_file(path):

    try:
        file = open(path, encoding='utf-8')
    except FileNotFoundError:
        print('No file in path:', path)
    else:
        print(file.read())


# path = 'example.txt'
# open_file(path)

"""
Get the standard error text:
    
    except ExceptionType as <name>:

"""


def open_file_as_exc(path):

    try:
        file = open(path, encoding='utf-8')
    except FileNotFoundError as ex:
        print(ex)
    else:
        print(file.read())


# path = 'exampleeee.txt'
# open_file_as_exc(path)


"""
In some situations you just want to pass.
You don't want to implement any code.

pass

"""

# Ex:
def open_file_as_pass(path):

    try:
        file = open(path, encoding='utf-8')
    except FileNotFoundError as ex:
        # Do nothing if the file doesn't exist
        pass
    else:
        print(file.read())


path = 'exampleee.txt'
open_file_as_pass(path)



