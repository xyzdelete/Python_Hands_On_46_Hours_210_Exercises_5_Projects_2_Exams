"""
1 - Exception vs. Syntax Error:

A Python program stops execution when it encounters an error.
The process of managing these situations is called Exception Handling.

There are two types of errors in Python:
 * Syntax Error (Desing-Time error)
 * Exception (Run-Time error)
"""

"""
Syntax Error (Desing-Time error):

If the code you write doesn't comply with Python syntax, the Python Parser will raise 'Syntax Error'.

Error Type: SyntaxError
"""

# Ex:
# SyntaxError
# print('Python Parser error'))

# Ex:
# SyntaxError: EOL while scanning string literal
# a = "12'
# print(a)

# Ex:
# ommitted indt
# def myFunc():
#     # function scope
#
# print('A')


"""
Exception: 
Let's say, your code is syntactically correct.
So it will start execution.
It it causes en error during the execution (run-time), Python Interpreter will raise an error.
This is error is called Exception in general.
"""

# Ex:
# ZeroDivisionError: division by zero
# a = 7 / 0


# Ex:
# NameError: name 't' is not defined
# print(t)


# Ex:
a = 12
b = 'B'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(a + b)
