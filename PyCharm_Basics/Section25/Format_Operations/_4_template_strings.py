"""
4- Template Strings

* Template Class under 'string' module
* $ is the place holder

"""

from string import Template

# Ex 1
name = 'Bruce Wayne'
hero = 'Batman'

template = Template('$h is $n')
print(template.substitute(h=hero, n=name))

# Ex 2
num_1 = 5
num_2 = 8
result = num_1 + num_2

template = Template('$a + $b = $c')
print(template.substitute(a=num_1, b=num_2, c=result))

