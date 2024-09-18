"""
Reading - Writing
"""

"""
Reading Methods:
* read() -> all content_up_to at once
* readline() -> reads single line and waits for the next one
* readlines() -> reads all the remaining lines
"""

# Ex -> Reading

# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     content = lorem.read()
#     print(content)

# read the first 50 chars
# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     content_up_to = lorem.read(50)  # read 50 chars
#     print(content_up_to)

# read the file line by line -> first line
# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     line_1 = lorem.readline()
#     print(line_1)


# read the file line by line -> first two lines
# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     line_1 = lorem.readline()
#     print(line_1)
#     line_2 = lorem.readline()
#     print(line_2)

# read all the lines one by one -> for loop
# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     for line in lorem:
#         print(line)

# read all the lines one by one -> for loop
# with open('lorem_ipsum.txt', mode='rt', encoding='utf-8') as lorem:
#     for line in lorem:
#         # copy the whole line -> Ctrl+D (windows) , ⌘+D (Mac)
#         line_content = line.split()  # splits the text from space chars -> ' ', \n, \t
#
#         # comment and uncomment -> Ctrl + /
#         # line_content = line.split(' ')  # splits the text from space chars -> ' ', \n, \t
#         print(line_content)




"""
Writing Modes:
* w: write   -> clear all the content and open as blank file (DANGEROUS)
* a: append  -> appends the new content to the existing one  (SAFE)
"""

# open with w mode
# with open('lorem_ipsum.txt', mode='w') as lorem:
#     lorem.write('New Line from Code')

# open with a mode
# with open('lorem_ipsum.txt', mode='a') as lorem:
#     lorem.write('New Line with append mode...')

# append it as a new line -> \n
# with open('lorem_ipsum.txt', mode='a') as lorem:
#     lorem.write('\nNew Actual Line with append mode...')


# append multiple lines at once
with open('lorem_ipsum.txt', mode='a') as lorem:
    list_to_append = ['\nMulti Line 1', '\nMulti Line 2', '\nMulti Line 3']
    lorem.writelines(list_to_append)



















