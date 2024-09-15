"""
We have covered so far:

try:
    ......
    ......
    ......

except Ex1:
    error
    ......
    ......

except Ex2:
    error
    .......

else:
    .......
    no-errors

finally:
    whether error or not
    .......

"""

# Ex:
def division(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('Result:', result)
    finally:
        print('Operation succeeded...')


# division(12, 0)
# division(12, 4)


# Ex:
# close the file in finally

def open_file(path):
    try:
        file = open(path, encoding='utf-8')
    except Exception as ext:
        print(ext)
    else:
        print(file.read())
    finally:
        try:
            file.close()
            print('Closing the file.')
        except:
            pass


# open_file('example.txt')
open_file('exampleeee.txt')








