"""
3. f-strings (String Interpolation)

* Python 3
* f".... string ... {}"

"""

x = 2
y = 3

multiplication = x * y
print(f"{x} * {y} = {multiplication}")

# more pythonic -> in {} you write Python statements
print(f"{x} * {y} = {x * y}")

# list
info = ['Klark Kent', 'Metropolis', 'Daily Planet']
print(f'{ info[0] } lives in { info[1] } and works for { info[2] }')

# Note:
# f-strings come up with 3.6