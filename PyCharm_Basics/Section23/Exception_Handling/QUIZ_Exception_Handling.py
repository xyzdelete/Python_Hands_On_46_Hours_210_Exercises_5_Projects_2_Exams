"""
 [10 Questions] QUIZ Exception Handling
"""
from webbrowser import Error

# --------------------------------------------------------------------------------------#

# Q 1:
"""
Define a function named "is_list".
It will take a list as parameter.
And it will check if this parameter actually of list type or not.
If the type of the parameter is not List, it will raise an exception as:
"The parameter type is not List."
If the type of the parameter is List, then it will print the it and 'pass'.

Hints:
* assert
* pass
* do not use try-except
"""

# S 1:

def is_list(a_list):
    assert isinstance(a_list, list), Exception("The parameter type is not List.")
    print(a_list)

# call with a Tuple
# is_list(('a', 'b', 'c'))

# call with a List
# is_list(['a', 'b', 'c'])

# --------------------------------------------------------------------------------------#

# Q 2:
"""
Define a function named 'sum_of_list'.
It will take a list as parameter and calculate the sum of numbers in this list.

If it encounters an error during summation, it will raise an Exception.
Otherwise, it will return the summation.

The exception type will be 'TypeError' and the text will be the standard error text.

Hints:
* try-except
* except .... as ....
"""


# S 2:

def sum_of_list(a_list):
    try:
        return sum(a_list)
    except TypeError as ex:
        print(ex)


# print(sum_of_list([1, 'b', 3]))
# print(sum_of_list([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Q 3:
"""
Define a function named 'sum_of_list_else'.
It will take a list as parameter and calculate the sum of numbers in this list.

If it encounters an error during summation, it will raise an Exception.
Otherwise, it will return the summation.

The exception type will be 'TypeError' and the text will be the standard error text.

Hints:
* try-except-else
* except .... as ....
"""


# S 3:

def sum_of_list_else(a_list):
    my_sum = 0
    try:
        my_sum = sum(a_list)
    except TypeError as ex:
        print(ex)
    else:
        return my_sum


# print(sum_of_list_else([1, 'b', 3]))
# print(sum_of_list_else([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Q 4:
"""
Define a function named 'sum_of_numbers_in_list'.
It will take a list as parameter.
And it will add the numbers in that list.
If any item is not a number it will ignore that item, but it will print as:
"item 'x' is not a number"

The function will return the summation result.

Hints:
* try-except-else
* assert
* pass
* try-except-else inside for loop

Expected Output:
sum_of_numbers_in_list([1, 'a', 'b', 3])

item a is not a number
item b is not a number
4
"""


# S 4:

def sum_of_numbers_in_list(a_list):
    my_sum = 0
    for item in a_list:
        try:
            assert int(item)
        except Exception:
            print("item 'x' is not a number")
            pass
        else:
            my_sum += item
    return my_sum



# this time, since we will check every element one by one, we will place try-except-else inside the for loop.

# print(sum_of_numbers_in_list([1, 'a', 'b', 3]))
# print(sum_of_numbers_in_list([1, 2, 3]))

# --------------------------------------------------------------------------------------#

# Q 5:
"""
Below, you see a function named "total_likes".
This function creates a dictionary of reviews.
And it returns total number of likes in this dictionary.

But there is a problem.
If you run the function as it is currently, you will see it raises an exception.

Fix this bug in the function by using try-except-else structure.

Hints:
* examine carefully each review :)
"""

def total_likes():
    reviews = [{'Image': 4, 'Like': 20, 'Comment': 12},
               {'Like': 15, 'Comment': 8, 'Share': 10},
               {'Image': 7, 'Comment': 16, 'Share': 37},
               {'Image': 6, 'Like': 10, 'Comment': 9}]

    total = 0

    for review in reviews:
        try:
            total += review['Like']
        except Exception:
            print("No Like key in Dict")
            pass
        else:
            pass

    return total

# total_number_of_likes = total_likes()
# print(total_number_of_likes)



# S 5:




# total_number_of_likes = total_likes()
# print(total_number_of_likes)

# --------------------------------------------------------------------------------------#

# Q 6:
"""
Define a function named 'calculator'.
It will ask for a mathematical operation from the user.
An operation is something like this: 6 * 5

The function will get this input and do the necessary calculation,
and return the result as follows:
6 * 5 = 30

The operation type can only be one of these: +, -, *, / 

Possible errors during the function execution:
1- The user might not include spaces between elements.
    - You must check the number of elements in the input
2- The user might use an operation type which is included in (+, -, *, /).
    - Check operation type
3- The first item and the third item (the operands) should be cast into float.
    - Check if the operands can cast to float
4- If the operation type is division (/) then the 3rd element can not be zero (0).
    - Check for the second operand not to be zero.

Define a working calculator by taking these possibilities into account.
Use try-except-else structure.
"""


# S 6:

def calculator():
    result = None
    try:
        user_input_operation_str = input("Enter a mathematical operation like 6 * 6:")
        operands_list = user_input_operation_str.split()
        assert len(operands_list) == 3, Exception("Operands amount != 3")
        assert operands_list[1] in ("+", "-", "*", "/"), Exception("Unknown math operation")
        try:
            float(operands_list[0])
            float(operands_list[2])
        except Exception as ex:
            print(ex)
            result = calculator()
        if operands_list[1] == "/" and float(operands_list[2]) == 0:
            raise Exception("Division by 0 is not allowed")
    except Exception as ex:
        print(ex)
        result = calculator()
    else:
        operands_list[0] = float(operands_list[0])
        operands_list[2] = float(operands_list[2])
        if operands_list[1] == "+":
            result = operands_list[0] + operands_list[2]
        elif operands_list[1] == "-":
            result = operands_list[0] - operands_list[2]
        elif operands_list[1] == "*":
            result = operands_list[0] * operands_list[2]
        elif operands_list[1] == "/":
            result = operands_list[0] / operands_list[2]
    finally:
        return result
# result = calculator()
# print(result)

# --------------------------------------------------------------------------------------#

# Q 7:
"""
Define a function named 'give_me_a_key'.
It will ask for the user to press any key on the keyboard.
If the key that the user pressed is:
1- a number -> return its square
2- a letter -> return ist capital form
3- neither a number nor a letter -> return the key itself

Define this function by using try-except-else-finally structure.
"""


# S 7:

def give_me_a_key():
    try:
        user_input = input("Press key: ")
        if user_input.isdigit():
            return float(user_input)**2
        elif user_input.isalpha():
            return user_input.upper()
        else:
            return user_input
    except Exception as ex:
        print(ex)
        pass
    else:
        pass
    finally:
        pass

# print(give_me_a_key())

# --------------------------------------------------------------------------------------#

# Q 8:
"""
Define a function named 'item_at_index'.
It will take a list and and index as parameters.
It will search for the item at this index in the list.
If it doesn't find the item, it will raise a standard exception.
It it finds, it will return the result.

* Hints:
* try-except-else
* raise only (no exception type declaration)
"""


# S 8:

def item_at_index(a_list, an_index):
    try:
        a_list[an_index]
    except Exception as ex:
        print(ex)
    else:
        pass


# my_list = ['x', 'y', 'z', 't']
# ind = 7
# result = item_at_index(my_list, ind)
# print(result)

# --------------------------------------------------------------------------------------#

# Q 9:
"""
Define a function named 'file_reader'.
It will take a file path as the parameter.
If the file doesn't exist at the specified path it will raise an exception.
Exception type will be standard exception.
It the file exists, it will read the content and print.
In any case (finally) it will close the file.

Hints:
* try-except-else-finally
* you need to check for the file in finally block

Expected Output:
file_reader('serieeees.txt')

FileNotFoundError: [Errno 2] No such file or directory: 'serieeees.txt'
"""


# S 9:
def file_reader(file_path):
    try:
        file = open(file_path)
    except Exception as ex:
        print(ex)
    else:
        for line in file:
            print(line)
    finally:
        try:
            file.close()
        except:
            pass


# file which doesn't exist
# path = "serieeees.txt"
# file_reader(path)

# file which exists
# path = "series.txt"
# file_reader(path)

# --------------------------------------------------------------------------------------#

# Q 10:
"""
We have a dictionary of TV series and number of seasons.

series = {
    'Game of Thrones ': 8,
    'Fargo': 4,
    'Dark': 3,
    'True Detective': 3,
    'Dogs of Berlin': 1,
    'The Crown': 6    
}

Define a function named 'series_and_seasons' that will use this dictionary.
It will ask for the name of a series and check if this series exists in the dictionary.
If it is not in the series dictionary the function will raise an exception as:
'No such series in the dictionary. Please try again: '
And it will ask again and again.
It will ask until it finds the given name in the dictionary.
Otherwise it will keep asking :)

Hints:
* while (infinite loop)
* try-except-else-finally
"""


# S 10:
def series_and_seasons(a_dict):
    try:
        user_input_key = input("Enter a name of a series: ")
        assert user_input_key in a_dict, Exception("No such series in the dictionary. Please try again:")
    except Exception as ex:
        print(ex)
        series_and_seasons(a_dict)
    else:
        print(a_dict[user_input_key])
    finally:
        pass

series = {
    'Game of Thrones ': 8,
    'Fargo': 4,
    'Dark': 3,
    'True Detective': 3,
    'Dogs of Berlin': 1,
    'The Crown': 6
}

# series_and_seasons(series)

# --------------------------------------------------------------------------------------#
