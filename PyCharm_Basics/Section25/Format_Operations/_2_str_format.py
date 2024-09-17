"""
2- String Format

str.format()
formatting with {}
"""

# without indexing
hi = 'Hi there {} {}'
print(hi.format('Peter', 'Parker'))

# with indexing
statement = '{0} word has {1} number of letters.'
print(statement.format('Python', len('Python')))

# parameter names
text_with_parameter_names = '{n} comes from {s}'
language_source = text_with_parameter_names.format(n='Python', s='Monthy Python and Holly Grail')
print(language_source)

language_source = text_with_parameter_names.format(n='Java', s='Java Coffee type, in Java Island')
print(language_source)


