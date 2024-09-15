"""
try-except

try:
    ....
    ............
    .......error...
    ........ will not be executed
    .....    will not be executed
    .......  will not be executed
except:
    ....
    ....


try:
    - Python tries to run the code
    - if no errors, it will finalize the try-except block
    - if there is an error, the execution will jump into the except block
except:
    - where you catch the exception
    - you do the necessary operations

"""

# Ex:
# the case with no exception handling
def get_squares():
    user_input = input('Enter a number: ')
    num = int(user_input)
    print(num**2)

# get_squares()


# with exception handling
def get_squares_try():
    try:
        user_input = input('Enter a number: ')
        num = int(user_input)
        print(num**2)
    except:
        print('Not a number...')

# get_squares_try()


# call the function -> recursion
def get_squares_try_recursion():
    try:
        user_input = input('Enter a number: ')
        num = int(user_input)
        print(num**2)
    except:
        print('Not a number...')
        get_squares_try_recursion()


# get_squares_try_recursion()

# Ex:
# Open a file.

# open which doesn't exist
def open_file(path):
    # open()
    file = open(path)

    # loop over file line by line
    for line in file:
        print(line.split())


# FileNotFoundError: [Errno 2] No such file or directory: 'serieeees.txt'
# path = 'serieeees.txt'
# open_file(path)


# handle the case where file not exist
def open_file_try(path):
    try:
        # open()
        file = open(path)

        # loop over file line by line
        for line in file:
            print(line.split())
    except:
        print('No such file in the path:', path)


# path = 'serieeees.txt'
# open_file_try(path)


"""
Handle more than one except blocks:
 - Multiple exceptions
 
except ExceptionType 1:

except ExceptionType 2:


"""

# Ex:
# divide by zero


def divide_number():

    try:
        # ValueError
        number_to_divide = int(input('Please enter a number to divide: '))
        divisor = int(input('Please enter the divisor: '))

        # ZeroDivisionError
        result = number_to_divide / divisor
        print(result)

    except ValueError:
        print('The inputs are not numeric...')

    except ZeroDivisionError:
        print('Second number can not be ZERO....')


divide_number()















