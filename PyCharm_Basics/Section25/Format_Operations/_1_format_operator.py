"""
% operator

placeholders:
- %s -> string
- %d -> integer
- %f -> float
    - %.<n>f -> n decimal places

"""

import math

day = 'Monday'
print('Today is %s' % day)

num = 28
print('%d is a perfect number.' % num)

pi = math.pi
# text = 'pi number in math: %f' % pi
text = 'pi number in math: %.2f' % pi
print(text)

# More than one %
info = 'Python released at %d and being used more than %.1f years' % (1991, 30)
print(info)

# Tuple with % operator
info = ('Peter', 'Parker', 28)
question = "Hi %s %s. How old are you? It's %d isn't it?" % info
print(question)

# Dictionary with % operator
file = {
    'path': './com/pty.py',
    'version': 1.8,
    'author': 'Musa ARDA'
}
file_info = "Path of file: %(path)s, the version: %(version).1f and the author: %(author)s" % file
print(file_info)





