"""
 [10 Questions] QUIZ - Format Operations
"""
# from pipes import Template

#--------------------------------------------------------------------------------------#

# Q 1:
"""
Define a function named 'day_names'.
It will ask for a day name from the user.
And will return a Tuple including the day name and number of letters in it.
Ex: (Sunday, 6)

Call this function and get the result Tuple, and then print the string below:
'Sunday has 6 letters.'

Hints:
* use % operator
"""

# S 1:

def day_names():
    user_input = str(input("Enter a day name: "))
    return (user_input, len(user_input))

# print("%s has %d letters" % day_names())
#--------------------------------------------------------------------------------------#

# Q 2:
"""
Call the function in Q1 and print the result with str.format() as follows:
'day: Monday, length: 6'
"""

# S 2:

# result = day_names()
# print("day: {DayName}, length: {LettersAmount}".format(DayName=result[0], LettersAmount=result[1]))


#--------------------------------------------------------------------------------------#

# Q 3:
"""
Call the function in Q1 and print the result with f-strings as follows:
'day: Monday, length: 6'
"""

# S 3:

# result = day_names()
# print(f"day: {result[0]}, length: {result[1]}")


#--------------------------------------------------------------------------------------#

# Q 4:
"""
Call the function in Q1 and print the result with Template Strings as follows:
'day: Monday, length: 6'
"""

# S 4:
from string import Template  # This is the correct module, not pipes

# templateStr = Template("day: $DayName, length: $LettersAmount")
# result = day_names()
# print(templateStr.substitute(DayName=result[0], LettersAmount=result[1]))


#--------------------------------------------------------------------------------------#

# Use the dictionary below for Questions 5, 6, 7, 8, 9, 10:
capitals = {
    'USA': 'Washington',
    'China': 'Beijing',
    'Germany': 'Berlin',
    'UK': 'London'
}

#--------------------------------------------------------------------------------------#

# Q 5:
"""
Use the capitals dictionary and % operator to print as follows:
"The capital city of USA is Washington"
'USA' will be constant, 'Washington' will be a variable.
"""

# S 5:

# print("The capital city of the USA is %(USA)s" % capitals)
#--------------------------------------------------------------------------------------#

# Q 6:
"""
Use the capitals dictionary and str.format() to print as follows:
"The capital city of Germany is Berlin"
Both 'Germany' and 'Berlin' will be variables.
"""

# S 6:

# print("The capital city of Germany is {CapitalCity}".format(CapitalCity=capitals.get("Germany")))


#--------------------------------------------------------------------------------------#

# Q 7:
"""
Use the capitals dictionary and f-strings to print as follows:
"The capital city of UK is London"
Both 'UK' and 'London' will be variables.
"""

# S 7:

# print(f"The capital city of UK is {capitals.get("UK")}")


#--------------------------------------------------------------------------------------#

# Q 8:
"""
Use the capitals dictionary and Template Strings to print as follows:
"The capital city of USA is Washington"
Both 'USA' and 'Washington' will be variables.
"""

# S 8:

templateStr = Template("The capital city of the USA is $CapitalCity")
# print(templateStr.substitute(CapitalCity=capitals.get("USA")))


#--------------------------------------------------------------------------------------#

# Q 9:
"""
Print the country names and capitals by using a for loop and f-strings as follows:
'<capital> is the capital of <country>'

Expected Output:
Washington is the capital of USA
Beijing is the capital of China
Berlin is the capital of Germany
London is the capital of UK
"""

# S 9:

# for eachCountry, eachCapital in capitals.items():
#     print(f"{eachCapital} is the capital of {eachCountry}")


# --------------------------------------------------------------------------------------#

# Q 10:
"""
Print the country names and capitals by using Comprehension and f-strings as follows:
'<capital> is the capital of <country>'

Expected Output:
Washington is the capital of USA
Beijing is the capital of China
Berlin is the capital of Germany
London is the capital of UK
"""

# S 10:

strList = [f"{eachCapital} is the capital of {eachCountry}"
           for eachCountry, eachCapital in capitals.items()]
print('\n'.join(strList))

# --------------------------------------------------------------------------------------#

